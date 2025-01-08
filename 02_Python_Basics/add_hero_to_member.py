from class_gen_info_member import Members

# Einen neuen Helden durch Benutzereingabe hinzufügen
def add_hero_to_member(squad_data):
    add_hero = input("Möchtest du einen neuen Helden zu diesem Squad hinzufügen? (ja/nein): ").lower()
    
    if add_hero == 'ja':
        # Benutzereingabe für den neuen Helden
        name = input("Name des Helden: ")
        age = int(input("Alter des Helden: "))
        secret_identity = input("Geheimidentität des Helden: ")
        
        # Kräfte hinzufügen
        powers_input = input("Kräfte des Helden (durch Kommas getrennt): ")
        powers = [power.strip() for power in powers_input.split(",")]

        # Erstelle ein neues Member-Objekt
        new_member = Members(
            name=name,
            age=age,
            secretIdentity=secret_identity,
            powers=powers
        )
        # Fügt den Helden zur Liste hinzu
        squad_data["members"].append({
            "name": new_member.name,
            "age": new_member.age,
            "secretIdentity": new_member.secretIdentity,
            "powers": new_member.powers
        })
        
        # Gibt den hinzugefügten Helden aus
        print(f"\n{new_member.name} wurde erfolgreich zum Team {squad_data['squadName']} hinzugefügt!")
    
    else:
        print("Kein neuer Held wurde hinzugefügt. Weiter zum nächsten Squad.")