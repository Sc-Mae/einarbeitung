import mysql.connector
import json

# Connect to MySQL without selecting a database 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Superhelden"  #Change to select a Database (database="Name of Database")
)

#! cursor must be added to enter SQL commands
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





#! Adds (add/delete/update/read)
while True:
    print(f"Möchtest du einen Wert in eine der drei Tabellen hinzufügen, löschen, bearbeiten oder auslesen? \n\nZur Auswahl stehen |squad|member|powers|.\n\nBitte wähle eine der Tabellen aus: \n\nMit >Quit< kannst du jederzeit abbrechen.")
    user_input = input()
    try:
        match user_input.lower():
            case "quit":
                print("Programm wird beendet...")
                exit()
            #! Anything to edit the squad
            case "squad":
                action = input("Möchtest du hinzufügen, löschen, bearbeiten oder auslesen? (add/delete/update/read): ").lower()
                match action:
                    case "add":
                        squad_name = input("Bitte gib den Squad Namen ein: ")
                        home_town = input("Bitte gib die Heimatstadt ein: ")
                        formed = input("Bitte gib das Gründungsjahr ein: ")
                        position = input("Bitte gib ein, ob der Squad >good<, >evil<, >neutral< ist: ")
                        secret_base = input("Bitte gib das Geheimversteck ein: ")
                        active = input("Bitte gib ein, ob der Squad aktiv ist (true/false): ")

                        sql = """INSERT INTO squad 
                                    (SquadName, HomeTown, formed, position, SecretBase, active) 
                                    VALUES (%s, %s, %s, %s, %s, %s)"""

                        values = (squad_name, home_town, formed, position, secret_base, active)

                    case "delete":
                        squad_id = input("Bitte gib die ID des Squads ein, der gelöscht werden soll: ")
                        sql = "DELETE FROM squad WHERE SquadID = %s"
                        values = (squad_id,)

                    case "update":
                        squad_id = input("Bitte gib die ID des Squads ein, das bearbeitet werden soll: ")
                        column = input("Welches Feld möchtest du bearbeiten (SquadName, HomeTown, formed, position, SecretBase, active)? ")
                        new_value = input(f"Bitte gib den neuen Wert für {column} ein: ")
                        sql = f"UPDATE squad SET {column} = %s WHERE SquadID = %s"
                        values = (new_value, squad_id)

                    case "read":
                        sql = "SELECT * FROM squad"
                        values = None
                        mycursor.execute(sql)
                        results = mycursor.fetchall()
                        for row in results:
                            print(row)

                    case _:
                        print("Ungültige Eingabe für die Aktion!")
                        exit()

            #! Anything to edit the members
            case "member":
                action = input("Möchtest du hinzufügen, löschen, bearbeiten oder auslesen? (add/delete/update/read): ").lower()
                match action:
                    case "add":
                        member_name = input("Name des Helden: ")
                        squad_id = input("Squad ID: ")
                        age = input("Alter: ")
                        secret_identity = input("Geheime Identität: ")

                        sql = """INSERT INTO member 
                                (name, squad_id, age, SecretIdentity) 
                                VALUES (%s, %s, %s, %s)"""

                        values = (member_name, squad_id, age, secret_identity)

                    case "delete":
                        member_id = input("Bitte gib die ID des Mitglieds ein, das gelöscht werden soll: ")
                        sql = "DELETE FROM member WHERE MemberID = %s"
                        values = (member_id,)

                    case "update":
                        member_id = input("Bitte gib die ID des Mitglieds ein, das bearbeitet werden soll: ")
                        column = input("Welches Feld möchtest du bearbeiten (name, squad_id, age, SecretIdentity)? ")
                        new_value = input(f"Bitte gib den neuen Wert für {column} ein: ")
                        sql = f"UPDATE member SET {column} = %s WHERE MemberID = %s"
                        values = (new_value, member_id)

                    case "read":
                        sql = "SELECT * FROM member"
                        values = None
                        mycursor.execute(sql)
                        results = mycursor.fetchall()
                        for row in results:
                            print(row)

                    case _:
                        print("Ungültige Eingabe für die Aktion!")
                        exit()

            #! Anything to edit the powers
            case "powers":
                action = input("Möchtest du hinzufügen, löschen, bearbeiten oder auslesen? (add/delete/update/read): ").lower()
                match action:
                    case "add":
                        member_id = input("Member ID: ")
                        power = input("Superkraft: ")

                        sql = """INSERT INTO powers 
                                (mid, power) 
                                VALUES (%s, %s)"""

                        values = (member_id, power)

                    case "delete":
                        power_id = input("Bitte gib die ID der Superkraft ein, die gelöscht werden soll: ")
                        sql = "DELETE FROM powers WHERE PowerID = %s"
                        values = (power_id,)

                    case "update":
                        power_id = input("Bitte gib die ID der Superkraft ein, die bearbeitet werden soll: ")
                        new_value = input("Bitte gib die neue Superkraft ein: ")
                        sql = "UPDATE powers SET power = %s WHERE PowerID = %s"
                        values = (new_value, power_id)

                    case "read":
                        sql = "SELECT * FROM powers"
                        values = None
                        mycursor.execute(sql)
                        results = mycursor.fetchall()
                        for row in results:
                            print(row)

                    #!Handles an invalid input and exits the programm
                    case _:
                        print("Ungültige Eingabe für die Aktion!")
                        exit()

            case _:
                print("Ungültige Eingabe! Wähle squad, member oder powers.")
                exit()
        #! checks if the values are filled
        if values:
            mycursor.execute(sql, values)
            mydb.commit()
            print("Aktion erfolgreich ausgeführt!")
    
    #! intercepts error messages, passes them to err and prints them out
    except mysql.connector.Error as err:
        print(f"Fehler: {err}")
    
    #! closes the cursor and database connection 
    finally:
        mycursor.close()
        mydb.close()














##! creates the table with its structure
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
    
    
    #! loads the json in the data variable
    # Load and insert Json in data variable 
    with open('hero.json') as file:
        data = json.load(file)


    #! takes the data and inserts into the squad table     
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
        
        #! takes the data and inserts into the member table  
        for member in squad['members']:
            member_sql = "INSERT INTO member (sid, name, age, SecretIdentity) VALUES (%s, %s, %s, %s)"
            member_values = (squad_id, member['name'],
                            member['age'],
                            member['SecretIdentity'])
            
            mycursor.execute(member_sql, member_values)
            member_id = mycursor.lastrowid
            
            #! takes the data and inserts into the power table  
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