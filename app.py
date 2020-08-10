from database import Database
# from models.blog import Blog
#
# import pymongo
#
# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client["test"]
# collection = database["students"]
from menu import Menu

Database.initialize()

menu = Menu()
menu.run_menu()
