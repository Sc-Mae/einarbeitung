import json
from class_gen_info_member import Members

with open('Hero.json', 'r') as file:
    json_hero = json.load(file)

def remove_hero(squad_data):
    # Ausgabe der aktuellen Mitglieder
    print("\nAktuelle Mitglieder:")
    for i, member in enumerate(squad_data["members"]):
        print(f"{i + 1}. {member['name']}")
    
    delete_hero= input("Möchtest du einen  Helden aus diesem Squad löschen? (ja/nein): ").lower()
    
    if delete_hero == 'ja':

        # Abfrage, welchen Helden der Benutzer löschen möchte
        try:
            hero_to_remove = int(input("Gib die Nummer des Helden ein, den du löschen möchtest: ")) - 1

            if 0 <= hero_to_remove < len(squad_data["members"]):
                removed_hero = squad_data["members"].pop(hero_to_remove)
                print(f"\n{removed_hero['name']} wurde erfolgreich aus dem Squad entfernt.")
            else:
                print("Ungültige Nummer, bitte versuche es erneut.")
        except ValueError:
            print("Bitte gib eine gültige Nummer ein.")

    else:
        print("Kein Held wurde gelöscht. Weiter zum nächsten Squad.")

## Beispielaufruf (nach dem Squad-Handling)
#for squad_data in json_hero:
#    remove_hero(squad_data)
