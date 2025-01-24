import mysql.connector
import json

# Connect to MySQL without selecting a database 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Superhelden"  #Change to select a Database (database="Name of Database")
)

mycursor = mydb.cursor()

#! Show all Databases
#mycursor.execute("SHOW DATABASES")
#
#for x in mycursor:
#  print(x)

#! Show one Table
#
#mycursor.execute("SELECT * FROM squad")
#anzeige = mycursor.fetchall()





#! inserts a record in the Table you choose

print(f"Möchtest du einen Wert in eine der drei Tabellen hinzufügen? \n\nZur Auswahl stehen >squad<, >member<, >powers<.\n\nBitte wähle eine der Tabellen aus: \n\nMit >Quit< kannst du jederzeit das abbrechen.")
user_input = input()
try:
    match input().lower():
        case "quit":
              exit()
    
        case "squad":
            squad_name = input("Bitte gib den Squad Namen ein: ")
            home_town = input("Bitte gib die Heimatstadt ein: ")
            formed = input("Bitte gib das Grundüngsjahr ein: ")
            position = input("Bitte gib ein ob der Squad >good<, >evil<, >neutral< ist: ")
            secret_base = input("Bitte gib das Geheimversteck ein: ")
            active = input("Bitte gib ein ob : ")

            sql = """INSERT INTO squad 
                        (SquadName, HomeTown, formed, position, SecretBase, active) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            
            values = (squad_name, home_town, formed, position, secret_base, active)

        case "member":
            member_name = input("Name des Helden: ")
            squad_id = input("Squad ID: ")
            age = input("Alter: ")
            secret_identity = input("Geheime Identität: ")

            sql = """INSERT INTO member 
                    (name, squad_id, age, SecretIdentity) 
                    VALUES (%s, %s, %s, %s)"""
            
            values = (member_name, squad_id, age, secret_identity)

        case "powers":
            member_id = input("Member ID: ")
            power = input("Superkraft: ")
            
            sql = """INSERT INTO powers 
                    (mid, power) 
                    VALUES (%s, %s)"""
            
            values = (member_id, power)
        
        case _:
            print("Ungültige Eingabe! Wähle squad, member oder powers.")
            exit()
    
    mycursor.execute(sql, values)
    mydb.commit()
    print("Datensatz erfolgreich eingefügt!")

except mysql.connector.Error as err:
        print(f"Fehler beim Einfügen: {err}")

finally:
    mycursor.close()
    mydb.close()
















##!formates the print auf the table 
#print("\nSquad Information:")
#print("-" * 1)
#for x in anzeige:
#   print(f"Squad: {x[1]:<24} | Location: {x[2]:<12} | Formed: {x[3]:<6} | Position: {x[4]:<8} | Base: {x[5]:<15} | Active: {x[6]} |")
#   print("-" * 1)
#



'''try:
    # Create database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Superhelden")
    mycursor.execute("CREATE DATABASE Superhelden")
    # Uses a speciffic Database ("USE Name of Database)
    mycursor.execute("USE Superhelden")
    
    # Create tables
    mycursor.execute("""
        CREATE TABLE squad (
            sid INT AUTO_INCREMENT PRIMARY KEY,
            SquadName VARCHAR(255),
            HomeTown VARCHAR(255),
            formed INT,
            position VARCHAR(255),
            SecretBase VARCHAR(255),
            active BOOLEAN
        )
    """)
    
    mycursor.execute("""
        CREATE TABLE member (
            mid INT AUTO_INCREMENT PRIMARY KEY,
            sid INT,
            name VARCHAR(255),
            age INT,
            SecretIdentity VARCHAR(255),
            FOREIGN KEY (sid) REFERENCES squad(sid)
        )
    """)
    
    mycursor.execute("""
        CREATE TABLE powers (
            pid INT AUTO_INCREMENT PRIMARY KEY,
            mid INT,
            power VARCHAR(255),
            FOREIGN KEY (mid) REFERENCES member(mid)
        )
    """)
    
    
    # Load and insert Json in data variable 
    with open('hero.json') as file:
        data = json.load(file)
        
    for squad in data:
        # Insert squad
        squad_sql = "INSERT INTO squad (SquadName, HomeTown, formed, position, SecretBase, active) VALUES (%s, %s, %s, %s, %s, %s)"
        squad_values = (squad['SquadName'],
                        squad['HomeTown'],
                        squad['formed'],
                        squad['position'],
                        squad['SecretBase'],
                        squad['active'])
        
        mycursor.execute(squad_sql, squad_values)
        squad_id = mycursor.lastrowid
        
        # Insert members and their powers
        for member in squad['members']:
            member_sql = "INSERT INTO member (sid, name, age, SecretIdentity) VALUES (%s, %s, %s, %s)"
            member_values = (squad_id, member['name'],
                            member['age'],
                            member['SecretIdentity'])
            
            mycursor.execute(member_sql, member_values)
            member_id = mycursor.lastrowid
            
            # Insert powers
            for power in member['power']:
                power_sql = "INSERT INTO powers (mid, power) VALUES (%s, %s)"
                mycursor.execute(power_sql, (member_id, power))
    
    mydb.commit()
    print("Database 'Superhelden' created and data imported successfully!")

except Exception as e:
    print(f"Error: {e}")
    mydb.rollback()

finally:
    mycursor.close()
    mydb.close()'''