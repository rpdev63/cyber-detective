import requests
import pytest
from app.Scrapper import Scrapper_Book
from app.Book import Book


URLS_TO_TEST = [
    "https://books.toscrape.com/",
    "https://books.toscrape.com/catalogue/page-3.html",
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
]


@pytest.mark.parametrize("url", URLS_TO_TEST)
def test_url_are_found(url):
    response = requests.get(url)
    assert response.status_code == 200


def test_total_pages_is_known(scrapper: Scrapper_Book):
    assert scrapper.total_books > 0
    assert scrapper.books_per_page > 0
    assert scrapper.total_pages > 0
    scrapper.driver.quit()


def test_scrap_one_book_page(scrapper: Scrapper_Book):
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    book = scrapper.scrap_book_page(url)
    assert isinstance(book, Book)
    assert isinstance(book.title, str)
    assert isinstance(book.price, str)
    assert isinstance(book.rating, int)
    assert isinstance(book.availability, str)
    assert isinstance(book.img_url, str)
    scrapper.driver.quit()


# def test_links_are_found(scrapper: Scrapper_Book):
#     assert len(scrapper.get_all_links()) == scrapper.total_books
#     scrapper.driver.quit()
