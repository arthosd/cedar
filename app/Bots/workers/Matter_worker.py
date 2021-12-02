"""
This worker get all the data from youmatter website and clean them

    1-> Connect to mongoDB 
    2-> Retrieve all youmatter datas
    3-> Clean data
    4-> Connect to Mysql
    5-> Add clean data in Database
"""
from app.log.log import lprint
from database_pipeline import get_mongoDB,get_mysql, get_mongo_collection_name

import pandas as pd

def start_matter():
    # Connnecting to MongoDB
    db = get_mongoDB()

    # Get Youmatter datas
    raw_data = db.get_data(get_mongo_collection_name(), {"website" : "youmatter","treated":False})

    if raw_data.count() != 0:

        # Transforming json format to pandas format
        df = pd.DataFrame(list(raw_data))
        # Cleaning data
        """
            1 -> Removing the "by" before the author.
            2 -> Removing all decoration in the text.
        """
        df["author"] = df.author.str.replace("by ", "")
        df["category"] = df.category.str.replace(" change and global warming: all the news", "")
        df["text"] = df.text.str.replace("\n", ".")
        df["text"] = df.text.str.replace("\t", ".")
        df["article_date"] = None

        # Processing data 
        """
            1- Summurizing text
        """

        # Connecting to MYSQL database
        sql_database = get_mysql()
        
        # Adding processed and cleaned data to MYSQL
        for index, row in df.iterrows():
            sql_database.insert_article_database(row.article_date,row.category,row.title,row.text,row.link,row.cover_image,row.author,row.website)
            lprint("MYSQL -> ADDED ARTICLE TO DATABASE", 1)

        sql_database.commit_change() 
        lprint("MYSQL ----> Commit all changes")

        # changing treated to True
        db.update_many_data(
            get_mongo_collection_name(),
            {
                "treated":False,
                "website":"youmatter"
            },
            {
                "treated" : True
            }
        )

    else :
        lprint("Matter_Worker -> No new article to process",1)

# ENDING