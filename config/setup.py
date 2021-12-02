"""
Setup script to downlaod and install all the necessary librairies and packages
"""

import pip # Pip librairy for installing packages
import platform # To determine platform 
import configparser # Reading config file

import os

cfg = configparser.ConfigParser()
cfg.read('config/config.cfg')  # Open config file

selenium_version = cfg.get("SELENIUM", "chromedriver_version") # selenium version
sql_database = cfg.get("MYSQL", "database_name") # sql_database

def install (package_name) :
    if hasattr(pip, 'main'):
        pip.main(['install', package_name])
    else:
        pip._internal.main(['install', package_name])

def install_packages (bool):
    if bool :
        install('pymongo') # Pymongo
        install('mysql-connector-python') # Mysql
        install('nltk') # Nltk
        install('scrapy') # Scrapy
        install('selenium') # Selenium
        install('bs4') # Beautifull soup
        install('zipfile') # zip
        install('urllib') # downlaod
        install('pandas') # downlaod
    else :
        print ("Requirements already satisfied")


# Installing all the librairies
install_packages(True)

from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO


def download_selenium_driver (version):

    if version is None :
        print("Warning there is no version entered")
        return None

    url = 'https://chromedriver.storage.googleapis.com/'+version+'/'

    if platform.system() == 'Linux':
        url += "chromedriver_linux64.zip"
        print (url)
    elif platform.system() == "Darwin":
        url += "chromedriver_linux64.zip"

    response = urlopen(url)

    # Getting zip file
    zipRef = ZipFile(BytesIO(response.read()))

    # Un-zipping file
    zipRef.extractall("app/Bots/bots/")
    os.chmod('app/Bots/bots/chromedriver', 755)


# Downloading and Installing selenium
download_selenium_driver(selenium_version)

import mysql.connector # Connectors

# connexion to mysql serveur

server = mysql.connector.connect(
    user = cfg.get("MYSQL","database_user"),
    host = cfg.get("MYSQL","database_host"),
    password = cfg.get("MYSQL","database_pwd")
)

cursor = server.cursor() # Init cursor

cursor.execute("CREATE DATABASE "+sql_database) # Creating database
cursor.execute("USE "+sql_database) # Using this the database

create_table = """CREATE TABLE ARTICLE
(
    article_id      INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    article_date    VARCHAR(255),
    category		VARCHAR(255),
    title           TEXT,
    text			LONGTEXT,
    link            TEXT NOT NULL,
    image_link      TEXT,
    author_name     TEXT,
    tweeted         TINYINT DEFAULT 0,
    website         VARCHAR(255),
    resume_sentence TEXT
);"""

cursor.execute(create_table) # Using this the database