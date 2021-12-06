# Project Cedar
Project cedar is a bot that crawl the web for ressources related to ecology and climate change. It is an open source project that is mainly maintained by BIOS association.

## Why project Cedar
The purpose of this project is to ***get***, ***analyse***, ***process*** and ***give access*** to ecology and climate change ressources. Till now the project is used on some websites to crawl articles and tweet 1 article a day so that people can read them.   
The finality of this project is to form a ***GREEN data warehouse*** and a big ontology so that investers and readers can centralize everything they need.   
This project is now open-sourced so that everyone can improve the bot to its ending point.    ***DO NOT HESITATE TO ACTIVELY PUSH TO THIS REPOT***  


## Getting Started
### Install Mysql and MongoDB

Project cedars uses MongoDB to store crawled data and mysql to store processed data.   
Thus, you'll need to install them and make sure they are up and running on your machine.   
- [MongoDB](https://docs.mongodb.com/manual/installation/) installation process.
- [Mysql](https://www.mysql.com/downloads/) installation process.   

***NOTICE :*** The project is attented to be used in local only. Next version will add host functionalities.   

### Configure project
Create the file in the following path `/config/config.cfg. This file is required to run the installer
```
[MONGO]:

db_name = article
collection_name = article

[MYSQL]:

database_host = host
database_user = user
database_pwd = pwd
database_name = db_name
database_table = table_name

[SELENIUM]:

chromedriver_version = 95.0.4638.69
```    
   
***WARNING :*** You'll need the enter ALL THE fields otherwise project will crash.

### Run installer
After creating and configuring `config.cfg` run the following command :

```bash
python /config/setup.py
```

## Start project
To start the whole pipeline just run the following line at the root of the project :
```bash
python pipeline.py
```

If you don't want to run the whole pipeline you can run them separatly.
