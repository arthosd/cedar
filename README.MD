# Project Cedar
Project cedar is a bot that crawl the web for ressources related to ecology and climate change. It is an open source project that is mainly maintained by BIOS association.

## Why project Cedar
The purpose of this project is to ***get***, ***analyse***, ***process*** and ***give access*** to ecology and climate change ressources. Till now the project is used on some websites to crawl articles and tweet 1 article a day so that people can read them.   
The finality of this project is to form a ***GREEN data warehouse*** and a big ontology so that investers and readers can centralize everything they need.   
This project is now open-sourced so that everyone can improve the bot to its ending point.    ***DO NOT HESITATE TO ACTIVELY PUSH TO THIS REPOT***  


## Getting Started
******
### Install librairies   

Run the following commands on a terminal :

```bash
pip install pymongo
pip install scrapy
pip install bs4
pip install selenium
pip install tweepy
pip install nltk
```
***WARNING :*** If you're using the built-in text summurizer you'll need to install the stopwords librairy from nltk.
### Download chromedriver

You can download chromedriver [here](https://chromedriver.chromium.org/downloads).   
Make sure you'll download the ***same version as your chrome installation on your local device***. Extract the file in `"app/Bots/bots/"`.

### Install Mysql and MongoDB

Project cedars uses MongoDB to store crawled data and mysql to store processed data.   
Thus, you'll need to install them and make sure they are up and running on your machine.   
- [MongoDB](https://docs.mongodb.com/manual/installation/) installation process.
- [Mysql](https://www.mysql.com/downloads/) installation process.   

***NOTICE :*** The project is attented to be used in local only. Next version will add host functionalities.   

### Configure project
Located in `/config` folder are all the config files needed to run the project. 
- application.cfg : Selenium configurations and other.
- database.cfg : Mongo and mysql configurations.
- twitter.cfg : Twitter's API configuration.     
   
***WARNING :*** Make sure you've entered all necessary field otherwise project will crash.

## Start project
To start the whole pipeline just run the following line at the root of the project :
```bash
python pipeline.py
```

If you don't want to run the whole pipeline you can run them separatly.