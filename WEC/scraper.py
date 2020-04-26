"""
WEC
Author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
Has tools for scraping things from the soup:
- get_email (returns list of valid emails)
- get_link (returns list of valid links)
"""
from checker import valid_email, valid_link


def get_emails(page_soup):
    """
    Get Email: Extracts all the emails on the page
    - which are links with: `mailto:`
    - have `mail` as word before them
    - have `contact` as word before them

    Parameter:
    ------
    - page_soup: BeautifulSoup.soup
        the soup the page from where the mail addresses are to be extracted

    Return:
    ------
    - list of email found without any repetitions
    """
    a_tags = page_soup.find_all("a")
    emails = []
    for a_tag in a_tags:
        try:
            link = a_tag["href"]
        except Exception:
            continue
        if link.find("mailto:") != -1:
            emails.append(link[7:].replace("[at]", "@").replace("[dot]", "."))

    all_text = page_soup.get_text().casefold().replace("\t", "")
    number_of_emails = all_text.count("[at]")
    number_of_emails += all_text.count("@")
    # print(number_of_emails)
    check_from = 0
    for _ in range(0, number_of_emails):
        loc = min(all_text.find("[at]", check_from), all_text.find("@", check_from))

        # scraping out email and checking validity
        email_start = (
            max(
                all_text.rfind("\n", check_from, loc),
                all_text.rfind(" ", check_from, loc),
            )
            + 1
        )
        email_end = min(all_text.find(" ", loc), all_text.find("\n", loc))
        email = (
            all_text[email_start:email_end].replace("[at]", "@").replace("[dot]", ".")
        )
        if valid_email(email):
            emails.append(email)

        # checking form the end of the new mail in the next iteration
        check_from = email_end
    return list(set(emails))


def get_links(page_soup, link, website):
    """
    Takes links out and converts them to absolute paths
    - takes them out form a_tag["href"]
    - give out link which might have relevant information
    - only returns valid links

    Parameter:
    ------
    - page_soup: BeautifulSoup.soup
        the soup of the page whose links are to scraped

    Return:
    ------
    - list of links to follow
    """
    a_tags = page_soup.find_all("a")

    sublinks = []
    for a_tag in a_tags:
        try:
            raw_link = a_tag["href"].strip()
        except Exception:
            continue

        # checking for relative path
        if not raw_link.startswith("http"):
            if raw_link.startswith("/"):
                sublink = website + raw_link
            else:
                sublink = website + "/" + raw_link
        else:
            sublink = raw_link

        if valid_link(sublink, link):
            sublinks.append(sublink)

    return list(set(sublinks))
