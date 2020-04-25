"""
WEC
Author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
Has the class and tools for communicating with the database
"""
import sqlite3
from sqlite3 import Error


class Database:
    """
    A database handler class
    """

    def __init__(self, path):
        """
        Database class

        Parameter:
        ------
        - path: string
            the path where the database is to be added
        """

        # establishing connection
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        self.connection = connection
        self.cursor = connection.cursor()
        self.number_of_emails = 0

        # setting up the database table
        try:
            self.cursor.execute(
                """CREATE TABLE email (
            Id int NOT NULL PRIMARY KEY,
            Email varchar(255) NOT NULL UNIQUE,
            Link varchar(255) NOT NULL
            );"""
            )
        except Exception as err:
            print(err)

    def add(self, email, link):
        """
        Adds the email and link into he database with a primary id

        Parameters:
        ------
        - email: string
            the email to be added
        - link: string
            the page from where the link was picked up

        Return:
        ------
        - nothing
        """
        self.number_of_emails += 1
        try:
            self.cursor.execute(
                f"INSERT INTO email VALUES ({self.number_of_emails},'{email}','{link}')"
            )
        except Exception as err:
            print(f"Error:{err} \n for: {email} at {link}")
            return
        self.connection.commit()

    def count_emails(self):
        """
        Return the number of emails entered into the database
        """
        return self.number_of_emails


def test():
    """
    Tests the class functionality
    """
    DB = Database("database.db")
    DB.add("test3@testmail.com", "www.testwebsite3.com")
    print(DB.count_emails())
    DB.add("test2@testmail.com", "www.testwebsite2.com")
    print(DB.count_emails())


if __name__ == "__main__":
    test()
