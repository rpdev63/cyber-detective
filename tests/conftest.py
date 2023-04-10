import os
from app.Scrapper import Scrapper_Book
import pytest
from app.db import connect_to_db


BASE_URL = "https://books.toscrape.com/"
DATA_FOLDER = os.path.join(os.getcwd(), 'data')


@pytest.fixture
def scrapper():
    return Scrapper_Book(BASE_URL, DATA_FOLDER)


@pytest.fixture
def db_conn():
    conn = connect_to_db()
    yield conn
    conn.close()
