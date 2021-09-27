from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, WriteError,ServerSelectionTimeoutError
from app.log.log import lprint

class Mongo :

    def __init__(self,collection_name):
        self.__client = MongoClient('localhost',27017)
        self.__db = self.__client[collection_name]

    def get_db (self):
        return self.__db

    def add_data (self,collection_name, data_to_add):
        try : 
            self.__db[collection_name].insert_many(data_to_add)
        except DuplicateKeyError:
            lprint("MONGODB. COULDN'T INSERT DATA. DUPLICATE KEY.", 1)


    def add_one_data (self,collection, data_to_add):

        post_id = None

        try :
            post_id = self.__db[collection].insert_one(data_to_add).inserted_id
        except DuplicateKeyError:
            lprint("MONGODB. COULDN'T INSERT DATA. DUPLICATE KEY FOR : "+str(data_to_add), 2)

        return post_id

    def get_data (self,collection, filter=None):

        if filter == None :
            return self.__db[collection].find()
        else:
            return self.__db[collection].find(filter)

    def get_one_data (self,collection, filter=None):
        if filter == None:
            return self.__db[collection].find_one()
        else:
            return self.__db[collection].find_one(filter)

    def update_data (self, collection,query, new_data):

        count = 0

        try : 
            count = self.__db[collection].update_one(query, { "$set" : new_data })
        except :
            print("ERROR : Could not update data")
        
        return count

    def update_many_data (self,collection,query, new_data):

        count = 0

        try : 
            count = self.__db[collection].update_many(query, { "$set" : new_data })
        except :
            print("ERROR : Could not update data")
        
        return count

    def delete_one (collection, filter):
        pass

    def delete_many (self,collection, filter):
        try :
            self.__db[collection].delete_many (filter)
        except:
            lprint("MONGOD -> ERROR WHILE DELETING DOCUMENT",1)