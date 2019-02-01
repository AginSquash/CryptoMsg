import database
import auth

### This file for testing some functions ###

#database.CreateKeysDB()
auth.Register()
print (database.GetData("ServerKey"))