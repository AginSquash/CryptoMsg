import database
import auth

### This file for testing some functions ###

database.CreateKeysDB()   
database.InsertKey("id1", "super_key", "29.01.2019")
auth.Register()
print (database.GetData("ServerKey"))