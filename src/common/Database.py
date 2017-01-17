import pymongo


class Database(object):

    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialise():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['webdev']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        Database.DATABASE[collection].find_one(query)
