import sqlite3
 
def ConnectToDB():
    conn = sqlite3.connect("keys.db") # :memory: RAM
    cursor = conn.cursor()
    return conn, cursor

def CreateKeysDB(): 
    conn, cursor = ConnectToDB()
 
    try:
        cursor.execute("""CREATE TABLE keys
                        (id text, key text, create_date text)
                    """)
        conn.commit()
    except:
        pass

def InsertKey(id, key, create_date):
    conn, cursor = ConnectToDB()

    cursor.execute("INSERT INTO keys VALUES (?,?,?)", [id, key, create_date])

    conn.commit()
def GetData(id):

    conn, cursor = ConnectToDB()

    key = cursor.execute("SELECT key FROM keys WHERE id=(?);", [id]).fetchone()
    return key[0]