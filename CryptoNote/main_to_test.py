import database
import auth

### This file for testing some functions ###

auth.Register()
print (database.GetData("ServerKey"))