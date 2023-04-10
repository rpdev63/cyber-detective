import os
from app.Scrapper import Scrapper_Book
from app.db import create_csv_from_database


BASE_URL = "https://books.toscrape.com/"
DATA_FOLDER = os.path.join(os.getcwd(), 'data')


def main():

    # open the browser window
    scrapper = Scrapper_Book(BASE_URL, DATA_FOLDER)

    # Use scrapper
    scrapper.scrap_everything()

    # close the browser window
    scrapper.driver.quit()
    create_csv_from_database()


if __name__ == '__main__':
    main()
