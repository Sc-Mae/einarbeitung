import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Initial connection without database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create and use database
            cursor.execute("CREATE DATABASE IF NOT EXISTS Superhelden")
            cursor.execute("USE Yigimon")

            mycursor=mydb.curser()

            mycursor.execute("SHOW DATABASES")

            for x in mycursor:
                print(x)
            
#            # Create tables
#            cursor.execute("""
#                CREATE TABLE IF NOT EXISTS squad (
#                    sid INT AUTO_INCREMENT PRIMARY KEY,
#                    SquadName VARCHAR(255),
#                    HomeTown VARCHAR(255),
#                    formed INT,
#                    position VARCHAR(255),
#                    SecretBase VARCHAR(255),
#                    active BOOLEAN
#                )
#            """)
#            
#            cursor.execute("""
#                CREATE TABLE IF NOT EXISTS member (
#                    mid INT AUTO_INCREMENT PRIMARY KEY,
#                    sid INT,
#                    name VARCHAR(255),
#                    age INT,
#                    SecretIdentity VARCHAR(255),
#                    FOREIGN KEY (sid) REFERENCES squad(sid)
#                )
#            """)
#            
#            cursor.execute("""
#                CREATE TABLE IF NOT EXISTS powers (
#                    pid INT AUTO_INCREMENT PRIMARY KEY,
#                    mid INT,
#                    power VARCHAR(255),
#                    FOREIGN KEY (mid) REFERENCES member(mid)
#                )
#            """)
            
            print("Datenbank und Tabellen erfolgreich erstellt")
            
    except Error as e:
        print(f"Fehler: {e}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Datenbankverbindung geschlossen")

if __name__ == "__main__":
    create_database()