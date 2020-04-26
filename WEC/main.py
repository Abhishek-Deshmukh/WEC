"""
WEC
Author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
"""
import requests
from bs4 import BeautifulSoup
import scraper
from checker import find_text
from database_handler import Database


SCRAPED_LINKS = []
SAVED_MAILS = []
DB = Database("./database.db")


def finder_helper(root, branch, level, words):
    """
    The helper thing coz recursion

    Parameters:
    ------
    - root: string
        the main page from where this all started
    - branch: string
        the page to inspect
    - level: int
        the number of links away from root
    - words: string[]
        the list of words to look for

    Return:
    ------
    - list of link found across all the pages from that branch
    """
    # if link has already been visited go back
    if branch in SCRAPED_LINKS:
        return []

    # store link as visited
    prefix = ""
    for _ in range(level):
        prefix += "  "
    print(prefix + "scraping " + branch + ":")
    SCRAPED_LINKS.append(branch)

    # get the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    req = requests.get(branch, timeout=(5, 25), headers=headers)
    branch_soup = BeautifulSoup(req.text, "html.parser")

    # looking for the words
    if find_text(branch_soup.get_text(), words):
        # saving email if not in saved previously
        emails = scraper.get_emails(branch_soup)
        for email in emails:
            if not email in SAVED_MAILS:
                print(email)
                DB.add(email, branch)
                SAVED_MAILS.append(email.strip())
            else:
                return []

    # taking out links on this page and continuing
    leaves = scraper.get_links(branch_soup, branch, root)

    # just to avoid escaping into other websites and hell
    if level < 4:
        for leaf in leaves:
            try:
                leaves.extend(finder_helper(root, leaf, level + 1, words))
            except Exception as err:
                print(err)
        leaves = list(set(leaves))
    return leaves


def finder(root, words):
    """
    Finds out the list of email saves them in the Database and stuff on the given website

    Parameter:
    ------
    - root: string
        the link of hte website which is to be scraped
    - words: string[]
        a list of words to look for

    Return:
    ------
    - a list of websites visited
    """
    return finder_helper(root, root, 0, words)


def main(website_file_loc, word_file_loc):
    """
    Goes through all the website from the websites file and looks for the words from word file
    and
    saves the email found on pages which have those words

    Parameter:
    ------
    - website_file_loc: string
        the relative/absolute path to the file which has the list websites
    - word_file_loc: string
        the relative/absolute path to the file which has the list of words to look for

    Return:
    ------
    - nothing
    """

    # importing websites
    with open(website_file_loc, "r") as website_file:
        websites = list(website_file.read().split("\n"))[0:-1]

    # importing words
    with open(word_file_loc, "r") as word_file:
        words = list(word_file.read().split("\n"))[0:-1]

    print(f"websites: {websites}")
    print(f"words: {words}")
    for website in websites:
        finder(website, words)


if __name__ == "__main__":
    from sys import argv

    main(argv[1], argv[2])
