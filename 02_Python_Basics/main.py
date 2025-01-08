import json
from class_gen_info_member import Members
from add_hero_to_member import add_hero_to_member
from class_gen_info_squad import Squad
from remove_member import remove_hero


# JSON-Datei wird ausgelesen 
with open('Hero.json', 'r') as file:
    json_hero = json.load(file)



# Durch alle Einträge in der JSON-Datei loopen
for squad_data in json_hero:  
    

    # Überprüfen, ob "members" existiert
    if "members" not in squad_data:
        print("Fehler: 'members' ist nicht in den JSON-Daten vorhanden.")
        continue  

    # Liste der Mitglieder verarbeiten
    members = []
    for member_data in squad_data["members"]:
        member = Members(
            name=member_data["name"],
            age=member_data["age"],
            secretIdentity=member_data["secretIdentity"],
            powers=member_data["powers"]
        )
        members.append(member)

    # Liste des Squads verarbeiten
    squad = Squad(
        squadName=squad_data["squadName"],  
        homeTown=squad_data["homeTown"],
        formed=squad_data["formed"],
        status=squad_data["status"],
        active=squad_data["active"],
        members=members
    )

    # Squad Details ausgeben
    print("\nSquad Details: \n")
    print(f"Squad Name: \t \t \t{squad.squadName}")
    print(f"Home Town: \t \t \t{squad.homeTown}")
    print(f"Formed: \t \t \t{squad.formed}")
    print(f"Status: \t \t \t{squad.status}")
    print(f"Active: \t \t \t{squad.active}")
    
    print("\nZu Diesem Squad Gehören Folgende Superhelden:")
    
    # Mitglieder ausgeben
    print("-------------------------------------------------------------------------------------------------------")
    print("\nMember Details:")
    
    for member in members:
        print(f"Name: \t \t \t \t{member.name}")
        print(f"Secret Identity: \t \t{member.secretIdentity}")
        print(f"Age: \t \t \t \t{member.age}")
        print(f"Powers: \t \t \t{', '.join(member.powers)}")
        print("-------------------------------------------------------------------------------------------------------")

add_hero_to_member(squad_data)
remove_hero(squad_data)
