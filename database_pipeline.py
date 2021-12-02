"""
    Init all database (Mongo + sql)
"""

from app.Database.mongo.mongo import Mongo
from app.Database.sql.mysql import SQL
from app.log.log import lprint
import configparser

config = configparser.ConfigParser()
config.read("config/config.cfg")

# Mongo database
mongo_name = config.get("MONGO", "db_name")
mongo_collection = config.get("MONGO", "collection_name")

# Mysql database
host = config.get("MYSQL", "database_host")
username = config.get("MYSQL", "database_user")
pwd = config.get("MYSQL", "database_pwd")
db_name = config.get("MYSQL", "database_name")
article_name = config.get("MYSQL","database_table")

# Initialize all database
mongoDB = Mongo(mongo_name)
lprint("Connected to "+mongo_name, 1)
mysql = SQL(
    host,
    username,
    pwd,
    db_name,
    article_name
)
lprint("Connected to "+db_name, 1)

def get_mongoDB():
    return mongoDB

def get_mysql():
    return mysql

def get_mongo_collection_name():
    return mongo_collection

def get_mysql_table():
    return article_name