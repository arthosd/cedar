import mysql.connector
from mysql.connector import cursor

class SQL :

    def __init__(self, hostname,user,pwd,database,table_name):
        self._db = mysql.connector.connect(
                        host=hostname,
                        user=user,
                        password=pwd,
                        database=database,
                        auth_plugin='mysql_native_password'
                    )
        self.__table_name = table_name

    def insert_article_database (self, article_date, category, title, text, link, image_link, author_name, website):

        cursor = self._db.cursor()

        sql = """INSERT INTO """+ self.__table_name +""" (article_date, category, title, text, link, image_link, author_name, website) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"""
        values = (article_date, category, title, text, link, image_link, author_name, website)

        cursor.execute(sql,values)


    def commit_change(self):
        self._db.commit()