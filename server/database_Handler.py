import sqlite3
 
def ConnectToDB():  #FIXME Name for database
    conn = sqlite3.connect("_temp_Userkeys.db") # :memory: RAM
    cursor = conn.cursor()
    return conn, cursor

def CreateUserKeysDB(): 
    conn, cursor = ConnectToDB()
 
    try:
        cursor.execute("""CREATE TABLE _temp_Userkeys
                        (id text, email text, key text, status TINYTEXT, create_date text)
                    """)
        conn.commit()
    except:
        pass

def InsertData(id, email, key, status, create_date):
    conn, cursor = ConnectToDB()

    cursor.execute("INSERT INTO _temp_Userkeys VALUES (?,?,?,?,?)", [id, email, key, status, create_date])

    conn.commit()

def GetKey(id):

    conn, cursor = ConnectToDB()

    key = cursor.execute("SELECT key FROM _temp_Userkeys WHERE id=(?);", [id]).fetchone()
    
    conn.close()
    return key[0]

def GetUserId(email):
    conn, cursor = ConnectToDB()

    id = cursor.execute("SELECT id FROM _temp_Userkeys WHERE email=(?);", [str(email)]).fetchone()
    
    conn.close()
    if id==None:
        return None
    else:
        return str(id[0])