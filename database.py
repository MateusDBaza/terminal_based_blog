import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        # Connect uri with the Database class.
        # we could use self.uri if its define in method
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    # give insert a colection and insert data in that collection.
    def insert(collection, data):  # parameter collection and data
        Database.DATABASE[collection].insert(data)

    @staticmethod
    # give insert a colection and insert data in that collection.
    def find(collection, query):# parameter collection and data
        return Database.DATABASE[collection].find(query)
        # find will return a cursor()

    @staticmethod
    # give insert a colection and insert data in that collection.
    def find_one(collection, query):  # parameter collection and data
        return Database.DATABASE[collection].find_one(query)
    # find_one gets the first element returned by the cursor(in json format)



