# WEC
A Web Crawling email collector

## how to use
- connect to the WIFI (You do not wanna do this on your mobile data).
- clone or download the repository
- install requirements (`pip install -r requirements.txt`).
- go into the WEC folder `cd WEC`.
- write down the list of all website too search through in a .txt file.
- write down the list of all words too search for in a .txt file.
- on the command line:
  - `python3 main.py <websites file path> <words file path>`
  - wait (can take a while)(recommended to leave over night)
- when done it will have created a [sqlite](https://sqlite.org/index.html) database which can be accessed using various tools e.g.: [sqlite browser](https://sqlitebrowser.org/dl) etc.

### requirements
- [ python3 ](https://www.python.org/)
- [ bs4 ](https://pypi.org/project/beautifulsoup4/)
- [ requests ](https://2.python-requests.org/en/master/)
- [ validate_email ](https://pypi.org/project/validate_email/)
- [ sqlite browser ](https://sqlitebrowser.org/dl) (optional)

### List of institutes
list of institutes can be selected from [ nature index ](https://www.natureindex.com/institution-outputs) and many other places

### future prospects
- write tests
- make institute selection a part of the script
- fine tune the algorithm as little
- G.U.I.
- M.L.

##### note
Developers of the code are not responsible if you send an email you were not supposed to someone who was not supposed to get it.
Therefore, it is recommended that you look at page form where the email has been picked before sending the email.
