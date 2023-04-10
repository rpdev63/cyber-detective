from math import floor
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from app.Book import Book
from app.db import insert_book_into_db
import pandas as pd


RATING_DICT = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5}


class Scrapper_Book():
    """Initialize scrapper for site https://books.toscrape.com/
    Keyword arguments:
    base_url -- Site to scrap
    data_folder -- The folder where files are saved
    Return: a selenium web scrapper via firefox
    """

    def __init__(self, base_url: str, data_folder: str) -> webdriver.Firefox:
        options = Options()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", data_folder)
        # set up the Chrome driver
        self.base_url = base_url
        self.data_folder = data_folder
        self.driver = webdriver.Firefox(options=options)
        self.total_books = self.__get_number_total_of_books()
        self.books_per_page = self.__get_books_per_page()
        self.total_pages = floor(
            self.total_books / self.books_per_page) if self.total_books > self.books_per_page else 1

    def __get_number_total_of_books(self) -> int:
        self.driver.get(self.base_url)
        try:
            total_books = self.driver.find_element(
                By.XPATH, '//*[@id="default"]/div/div/div/div/form/strong[1]').text
        except:
            print("Erreur : le nombre total de livres introuvable")
            return -1
        else:
            return int(total_books)

    def __get_books_per_page(self) -> int:
        self.driver.get(self.base_url)
        try:
            total_books = self.driver.find_element(
                By.XPATH, '//*[@id="default"]/div/div/div/div/form/strong[3]').text
        except:
            print("Erreur : le nombre livres par page introuvable")
            return -1
        else:
            return int(total_books)

    def __get_links_for_one_page(self, url="https://books.toscrape.com/") -> List[str]:
        """return all links in one page

        Keyword arguments:
        url -- url to scrp
        Return: list of links
        """

        links = []
        self.driver.get(url)
        try:
            elements = self.driver.find_element(
                By.CSS_SELECTOR, 'ol.row').find_elements(By.CSS_SELECTOR, '.image_container a')
            for el in elements:
                links.append(el.get_attribute("href"))
        except NoSuchElementException:
            print("Erreur : impossible de localiser le ou les liens pour cette page.")
        return links

    def get_all_links(self) -> List[str]:
        """Get all links for all books

        Return: list of links for each book
        """
        all_links = []
        for i in range(1, self.total_pages + 1):
            if i == 1:
                all_links.extend(self.__get_links_for_one_page())
            else:
                url_to_scrap = self.base_url + f'catalogue/page-{str(i)}.html'
                all_links.extend(
                    self.__get_links_for_one_page(url=url_to_scrap))
        if len(all_links) == self.total_books:
            print("Tous les livres ont été trouvé")
        elif len(all_links) > self.total_books:
            print("Trop de liens ont été trouvé")
        else:
            print("Attention : tous les livres n'ont pas été trouvé !")
        return all_links

    def scrap_everything(self):
        """ Create a database with data off all books in the site 
        """
        # initialize a dataframe
        book_links = self.get_all_links()
        for book_url in book_links:
            book_tmp = self.scrap_book_page(book_url)
            book_tmp.display_values()
            insert_book_into_db(book_tmp)

    def scrap_book_page(self, url):
        self.driver.get(url=url)
        title = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1').text
        price = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[1]').text
        rating_classes = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[3]').get_attribute("class")
        rating_string = rating_classes.split()[-1]
        rating = RATING_DICT[rating_string.lower()]
        availability = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[2]').text
        img_url = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[1]/div/div/div/div/img').get_attribute("src")
        book = Book(title, price, rating, availability, img_url)
        return book
