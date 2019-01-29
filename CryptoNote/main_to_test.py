import database

### This file for testing some functions ###

database.CreateKeysDB()   
database.InsertKey("id1", "super_key", "29.01.2019")
print (database.GetData("id1"))