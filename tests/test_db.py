import mariadb
from app.db import read_sql_file, insert_book_into_db
from app.Book import Book
import pytest


# Define some test data
TEST_GOOD_BOOKS = [
    Book(title="Book 1", price=25, rating=4, availability="yes",
         img_url="https://example.com/book1"),
    Book(title="Book 2", price="12.99f", rating=3,
         availability="", img_url="https://example.com/book2"),
    Book(title="Book 3", price=" ", rating=4, availability="noono",
         img_url="https://example.com/book3"),
    Book(title="Book 4", price=15.2, rating=4.5,
         availability="maybe", img_url="https://example.com/book4"),
]

TEST_BAD_BOOKS = [
    Book(title="Book 1", price=None, rating=4, availability="yes",
         img_url="https://example.com/book1"),
]


def test_connect_to_db(db_conn):
    assert db_conn is not None
    assert isinstance(db_conn, mariadb.Connection)


def test_create_table_from_sql_file(db_conn: mariadb.Connection):
    filename = 'tests/test.sql'
    sql = read_sql_file(filename)
    cur = db_conn.cursor()
    print(type(cur))
    # Execute the SQL query
    for statement in sql.split(';'):
        cur.execute(statement)
    cur.execute(
        "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'test_books'")
    total_tables = cur.fetchone()[0]
    assert total_tables == 1


@pytest.mark.parametrize("book", TEST_GOOD_BOOKS)
def test_insert_good_books_into_db(db_conn: mariadb.Connection, book):
    cur = db_conn.cursor()
    response = insert_book_into_db(book, table_name="test_library.test_books")
    assert response == True


@pytest.mark.parametrize("book", TEST_BAD_BOOKS)
def test_insert_bad_books_into_db(db_conn: mariadb.Connection, book):
    cur = db_conn.cursor()
    response = insert_book_into_db(book, table_name="test_library.test_books")
    assert response == False
