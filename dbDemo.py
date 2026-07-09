import mysql.connector

# Connect to MySQL
class DB:
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="company"
    )

    mycursor = mydb.cursor()

    # Insert query
    # sql = "INSERT INTO customers(actnum,name,ifsc,balance) VALUES (%s, %s, %s,%s)"

    # # Values
    # val = ("SB001","Kiran","IFSC001",10000)

    
    @classmethod
    def runQuery(cls,sql):
        try:
    
            cls.mycursor.execute(sql)
            # Save changes
            cls.mydb.commit()

            print(cls.mycursor.rowcount, " affected")
            return 1
        except Exception as e:
            
            print(e)
            
            return -1