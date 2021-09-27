"""
This Workers get all the data from GlobalForest website and clean them 

1-> Connect to mongoDB 
    2-> Retrieve all youmatter datas
    3-> Clean data
    4-> Connect to Mysql
    5-> Add clean data in Database
"""

from app.log.log import lprint
from database_pipeline import get_mongoDB,get_mysql, get_mongo_collection_name

import pandas as pd

def start_global () :
    # Connecting to database
    db = get_mongoDB()

    # Get GlobalForest datas 
    raw_data = db.get_data(get_mongo_collection_name(), {"website" : "globalforest","treated":False })

    if raw_data.count() !=0:

        # Transforming json format to pandas format
        df = pd.DataFrame(list(raw_data))

        # Cleaning data
        df["article_date"] = None
        df["text"] = None

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

        # Changing treated to True
        db.update_many_data(
            get_mongo_collection_name(),
            {
                "website":"globalforest",
                "treated" : False
            },
            {
                "treated" : True
            }
        )

    else : 
        lprint("Global_work -> No new article to process",1)

# ENDING