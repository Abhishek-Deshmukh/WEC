"""
WEC
Author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
Has functions set up for checking validity of
- link (valid_link)
- email (valid_email)
"""
from validate_email import validate_email


def valid_link(raw_link, link):
    """
    Valid: returns false for links which are social media or have words which not in the zone

    Parameters:
    ------
    - raw_link: string
        the link whose validity is to be checked
    - link: string
        the link of the page this link was found on

    Return:
    ------
    - true or false based on validity
    """
    raw_link = raw_link.casefold()
    link = link.casefold()
    if (
        raw_link != link
        and link.find(raw_link[5:]) == -1
        and raw_link.find("humanities") == -1
        and raw_link.find("://#") == -1
        and raw_link != link + "/"
        and raw_link + "/" != link
        and raw_link.find(".pdf") == -1
        and raw_link.find("/pdf/") == -1
        and raw_link.find(".exe") == -1
        and raw_link.find(".zip") == -1
        and raw_link.find(".tar.gz") == -1
        and raw_link.find(".mp4") == -1
        and raw_link.find(".mp3") == -1
        and raw_link.find(".png") == -1
        and raw_link.find(".jpg") == -1
        and raw_link.find("mailto:") == -1
        and raw_link.find("tel:") == -1
        and raw_link.find("www.google") == -1
        and raw_link.find("docs.google") == -1
        and raw_link.find("mail.google") == -1
        and raw_link.find("scholar.google") == -1
        and raw_link.find("books.google") == -1
        and raw_link.find("drive.google") == -1
        and raw_link.find("adobe") == -1
        and raw_link.find("youtube") == -1
        and raw_link.find("youtu.be") == -1
        and raw_link.find("facebook") == -1
        and raw_link.find("twitter") == -1
        and raw_link.find("instagram") == -1
        and raw_link.find("soundcloud") == -1
        and raw_link.find("linkedin") == -1
        and raw_link.find("jstor") == -1
        and raw_link.find("librar") == -1
        and raw_link.find("www.github.com") == -1
        and raw_link.find("www.nature.com") == -1
        and raw_link.find(".nature.com") == -1
        and raw_link.find("reach-us") == -1
        and raw_link.find("phd") == -1
        and raw_link.find("sexual") == -1
        and raw_link.find("publications") == -1
        and raw_link.find("publikations") == -1
        and raw_link.find("schedule") == -1
        and raw_link.find("purchase") == -1
        and raw_link.find("guest") == -1
        and raw_link.find("ragging") == -1
        and raw_link.find("advertis") == -1
        and raw_link.find("program") == -1
        and raw_link.find("invite") == -1
        and raw_link.find("history") == -1
        and raw_link.find("sports") == -1
        and raw_link.find("form") == -1
        and raw_link.find("awards") == -1
        and raw_link.find("transport") == -1
        and raw_link.find("facilities") == -1
        and raw_link.find("rules") == -1
        and raw_link.find("funding") == -1
        and raw_link.find("admission") == -1
        and raw_link.find("mission") == -1
        and raw_link.find("vision") == -1
        and raw_link.find("road") == -1
        and raw_link.find("uncategorised") == -1
        and raw_link.find("news") == -1
        and raw_link.find("committee") == -1
        and raw_link.find("fee") == -1
        and raw_link.find("corona") == -1
        and raw_link.find("contact") == -1
        and raw_link.find("/maps") == -1
        and raw_link.find("maps/") == -1
        and raw_link.find("media") == -1
        and raw_link.find("alumni") == -1
        and raw_link.find("jobs") == -1
        and raw_link.find("privacy") == -1
        and raw_link.find("security") == -1
        and raw_link.find("photos") == -1
        and raw_link.find("president") == -1
        and raw_link.find("login") == -1
        and raw_link.find("sign") == -1
        and raw_link.find("donate") == -1
        and raw_link.find("paypal") == -1
        and raw_link.find("gallery") == -1
        and raw_link.find("password") == -1
        and raw_link.find("javascript") == -1
        and raw_link.find("campus") == -1
        and raw_link.find("accessibility") == -1
        and raw_link.find("encyclopedia") == -1
        and raw_link.find("opportunities") == -1
        and raw_link.find("appointments") == -1
        and raw_link.find("questions") == -1
        and raw_link.find("classroom") == -1
        and raw_link.find("givetoqueens") == -1
        and raw_link.find(".queensu.ca") == -1
        and raw_link.find("weebpal") == -1
        and raw_link.find("phone") == -1
        and raw_link.find("grants") == -1
        and raw_link.find("www.sciencedirect.com") == -1
        and raw_link.find("www.connotea.org") == -1
        and raw_link.find("myams.org") == -1
        and raw_link.find("intranet") == -1
        and raw_link.find("sitemap") == -1
        and raw_link.find("site-map") == -1
        and raw_link.find("past-events") == -1
        and raw_link.find("coming-events") == -1
        and raw_link.find("covid") == -1
        and raw_link.find("projecteuclid.org") == -1
        and raw_link.find("ims.") == -1
        and raw_link.find("porn") == -1
        and raw_link.find("eroti") == -1
        and raw_link.find("healthcentre") == -1
        and raw_link.find("auditorium") == -1
        and raw_link.find("holiday") == -1
        and raw_link.find("hostel") == -1
        and raw_link.find("reach") == -1
        and raw_link.find("financ") == -1
        and raw_link.find("visitor") == -1
        and raw_link.find("resource") == -1
        and raw_link.find("location") == -1
        and raw_link.find("employment") == -1
        and raw_link.find("emergency") == -1
        and raw_link.find("calendar") == -1
        and raw_link.find("visit") == -1
        and raw_link.find("exhibition") == -1
        and raw_link.find("itunes") == -1
        and raw_link.find("museum") == -1
        and raw_link.find("copyright") == -1
        and raw_link.find("parents") == -1
        and raw_link.find("certificate") == -1
        and raw_link.find("disclaimer") == -1
        and raw_link.find("exam") == -1
        and raw_link.find("conference") == -1
        and raw_link.find("circulars") == -1
        and raw_link.find("registrar") == -1
        and raw_link.find("governor") == -1
        and raw_link.find("gandhi.gov.in") == -1
        and raw_link.find("facilities") == -1
        and raw_link.find("announcements") == -1
        and raw_link.find("product") == -1
        and raw_link.find("journal") == -1
        and raw_link.find("search") == -1
        and raw_link.find("article") == -1
        and raw_link.find("career") == -1
        and raw_link.find("positions") == -1
        and raw_link.find("publication") == -1
        and raw_link.find("scholarship") == -1
        and raw_link.find("vacancies") == -1
        and raw_link.find("seminar") == -1
        and raw_link.find("courses") == -1
        and raw_link.find("registration") == -1
        and raw_link.find("sponsor") == -1
        and raw_link.find("meeting") == -1
        and raw_link.find("node") == -1
        and raw_link.find("club") == -1
        and raw_link.find("event") == -1
        and raw_link.find("video") == -1
        and raw_link.find("council") == -1
        and raw_link.find("podcast") == -1
        and raw_link.find("/pubs.") == -1
        and raw_link.find("/pub_rights") == -1
        and raw_link.find("premium") == -1
        and raw_link.find("support") == -1
        and raw_link.find("speaker") == -1
        and raw_link.find("accomodation") == -1
        and raw_link.find("intern") == -1
        and raw_link.find("exchange") == -1
        and raw_link.find("participant") == -1
        and raw_link.find("references") == -1
        and raw_link.find("subscription") == -1
        and raw_link.find("membership") == -1
        and raw_link.find("policies") == -1
        and raw_link.find("bibcode") == -1
        and raw_link.find("export") == -1
        and raw_link.find("query") == -1
        and raw_link.find("archive") == -1
        and raw_link.find("training") == -1
        and raw_link.find("submit") == -1
        and raw_link.find("citation") == -1
        and raw_link.find("blog") == -1
        and raw_link.find("press_room") == -1
        and raw_link.find("bookseries") == -1
        and raw_link.find("setting") == -1
        and raw_link.find("glossary") == -1
        and raw_link.find("workshop") == -1
        and raw_link.find("poster") == -1
        and raw_link.find("safety") == -1
        and raw_link.find("snapshots") == -1
        and raw_link.find("pubmed") == -1
        and raw_link.find("kafesohbet") == -1
        and raw_link.find("evimtasnakliyat") == -1
        and raw_link.find("bayansexhatti") == -1
        and raw_link.find("/trends/") == -1
        and raw_link.find("/hindi/") == -1
        and raw_link.find("/help") == -1
        and raw_link.find("/faq") == -1
        and raw_link.find("/issues/") == -1
        and raw_link.find("librarians.asp.org") == -1
        and raw_link.find(".springer.com") == -1
        and raw_link.find(".plants.ox") == -1
        and raw_link.find("orcid.org") == -1
        and raw_link.find("www.fipa.org") == -1
        and raw_link.find("www.scitepress.org") == -1
        and raw_link.find("aip-info.org") == -1
        and raw_link.find("arxiv.org") == -1
        and raw_link.find("sciencemag.org") == -1
        and raw_link.find(".nlm.nih.gov") == -1
        and raw_link.find("moodle.org") == -1
        and raw_link.find("uniprot.org") == -1
        and raw_link.find("citeulike.org") == -1
        and raw_link.find(".ieee.org") == -1
        and raw_link.find("www.emis.de") == -1
        and raw_link.find("www.w3schools.com") == -1
        and raw_link.find("www.gnuplot.info") == -1
        and raw_link.find("www.stackoverflow.org") == -1
        and raw_link.find("www.pmindia.gov.in") == -1
        and raw_link.find("del.ico.us") == -1
        and raw_link.find("doi.org") == -1
        and raw_link.find("nic.in") == -1
        and raw_link.find("info.fuw.edu.pl") == -1
        and raw_link.find("worldscientific.com") == -1
        and raw_link.find("city.ac.uk") == -1
        and raw_link.find("pnas.org") == -1
        and raw_link.find("ecoliwiki.net") == -1
        and raw_link.find("hubmed.org") == -1
        and raw_link.find("thelancet.com") == -1
        and raw_link.find("www.ams.org") == -1
        and raw_link.find("www.cell.com") == -1
        and raw_link.find("unesco.org") == -1
        and raw_link.find("saa.org") == -1
        and raw_link.find("life-science-alliance.org") == -1
        and raw_link.find("nobelprize.org") == -1
        and raw_link.find("/bit.ly/") == -1
        and raw_link.find("/tender") == -1
        and raw_link.find("/address") == -1
        and raw_link.find("jetpack") == -1
        and raw_link.find("credai.org") == -1
        and raw_link.find(" ") == -1
    ):
        return True
    else:
        return False


def find_text(all_text, word_list):
    """
    Looks for the words hard-coded here in the text block

    Parameters:
    ------
    - all_text: string
        the text to look into
    - word_list: string[]
        the list of words to look through
    """
    all_text.casefold()

    # making sure it wasn't found as a compound word
    for word in word_list:
        if all_text.find(word) != -1:
            if all_text.find(" " + word) != -1:
                if (
                    all_text.find(" " + word + " ") != -1
                    or all_text.find(" " + word + ".") != -1
                    or all_text.find(" " + word + ",") != -1
                    or all_text.find(" " + word + "-") != -1
                ):
                    return True
            elif all_text.find("," + word + " ") != -1:
                return True
    return False


def valid_email(mail):
    """
    Checks if the mail is valid

    Parameters:
    ------
    mail: string
        the email address to check

    Return:
    ------
    - true or false
    """
    if (
        validate_email(mail)
        and mail.find("help") == -1
        and mail.find("info") == -1
        and mail.find("support") == -1
        and mail.find("spicmacay") == -1
        and mail.find("media") == -1
        and mail.find("hr") == -1
        and mail.find("office") == -1
        and mail.find("registrar") == -1
        and mail.find("legal") == -1
        and mail.find("skills") == -1
        and mail.find("webmaster") == -1
        and mail.find("test") == -1
        and mail.find("interational") == -1
        and mail.find("@city.ac.uk") == -1
        and mail.find("techsupport") == -1
        and mail.find("staff-council@") == -1
        and mail.find("careers") == -1
        and mail.find("inquiries") == -1
        and mail.find("feedback") == -1
        and mail.find("partners") == -1
        and mail.find("affiliates") == -1
        and mail.find("speaker") == -1
        and mail.find("accessibility") == -1
        and mail.find("service") == -1
        and mail.find("newspack") == -1
        and mail.find("privacy") == -1
        and mail.find("developers") == -1
        and mail.find("communications") == -1
        and mail.find("secretary") == -1
        and mail.find("gnu@gnu.org") == -1
        and mail.find("web@cell.com") == -1
        and mail.find("termsandconditions") == -1
        and mail.find("giving@") == -1
    ):
        return True
    return False
