import mariadb
import sys
import os
import csv
from dotenv import load_dotenv

from app import Book

load_dotenv()

# Connect to MariaDB Platform


def connect_to_db():
    """initialize connexion

    Return: mariadb Connection Object
    """

    try:
        conn = mariadb.connect(
            user=os.getenv('MARIADB_USER'),
            password=os.getenv('MARIADB_PASSWORD'),
            host=os.getenv('MARIADB_HOST'),
            port=int(os.getenv('MARIADB_PORT')),
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    return conn


def read_sql_file(filename):
    # Open the SQL file and read the contents
    with open(filename, 'r') as f:
        sql = f.read()
    return sql


def insert_book_into_db(book: Book, table_name="library.books"):
    """Write a new line in database 

    Keyword arguments:
    book : Book 
    Return: True(insertion ok) or False(insertion failed)
    """

    try:
        # Define the SQL INSERT statement
        query = f"""
        INSERT INTO {table_name} (title, price, rating, availability, img_url)
        VALUES (%s, %s, %s, %s, %s)
        """
        # Execute the SQL INSERT statement
        values = (book.title, book.price, book.rating,
                  book.availability, book.img_url)
        conn = connect_to_db()
        conn.cursor().execute(query, values)

        # Commit the transaction and close the database connection
        conn.commit()
        conn.close()
        return 1
    except:
        print("Erreur lors de l'écriture dans la BDD")
        return 0


def create_csv_from_database(table_name="library.books"):

    conn = connect_to_db()
    cur = conn.cursor()

    # Get columns name
    query = f"""SHOW COLUMNS
        FROM {table_name};"""
    cur.execute(query)
    columns_name = [row[0] for row in cur.fetchall()]

    # Get all books
    query = f"""
    SELECT * FROM {table_name} """
    cur.execute(query)
    books = cur.fetchall()

    # Name of the output file
    if not os.path.exists("data/"):
        os.makedirs("data")
    filename = "data/books.csv"

    # Open the file for writing
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns_name)
        for book in books:
            writer.writerow(list(book))
    print("CSV file written successfully!")
    conn.close()
