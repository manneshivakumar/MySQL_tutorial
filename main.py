import mysql.connector as connection

def open_connection():
    # establishing mysql connection
    try: 
        mydb = connection.connect(host="localhost", user="root", password="mysql@123", use_pure="True")
        print("connection successful")
        print(mydb.is_connected)
        
        # 1. fetch database information
        fetch_db_details(mydb)
        
        # 2. creating a database
        # create_database(mydb)

    except Exception as e:
        print(e)

def create_database(mydb):
    if(mydb.is_connected):
        #creating a database
        query = "Create database School2;"
        cursor = mydb.cursor()
        cursor.execute(query)
        print("school database created successfully")
        mydb.close()
    else:
        print("error")

def fetch_db_details(mydb):
    query = "show databases"
    cursor = mydb.cursor()
    cursor.execute(query)
    print("database details:")
    print(cursor.fetchall())

if __name__ == "__main__":
    open_connection()