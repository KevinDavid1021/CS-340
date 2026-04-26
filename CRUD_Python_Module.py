# Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'Password123' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Create method
    def create(self, data):
        if data is not None: 
            self.collection.insert_one(data)   
            return True
        else: 
            return False

    # Read method
    def read(self, query):
        if query is not None:
            data = self.collection.find(query)
            return list(data)
        else:
            return []
        
    # Update method for Module 5 - Project One
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        else:
            return 0
        
    # Delete method for Module 5 - Project One
    def delete(self, query):
        if query is not None:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            return 0