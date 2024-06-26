import uuid
import json

with open('base.json', 'r') as data_file:
    data = json.load(data_file)

class Member:
    def __init__(self, name: str, age: int, secretidentity: str, powers: list):
        self.name = name
        self.age = age
        self.secretidentity = secretidentity
        self.powers = powers
        self.uuid = str(uuid.uuid4())

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Secret Identity: {self.secretidentity}, Powers: {', '.join(self.powers)}"

class Squad:
    def __init__(self, squad_name: str, home_town: str, formed: int, status: str, secret_base: str, active: bool):
        self.squad_name = squad_name
        self.home_town = home_town
        self.formed = formed
        self.status = status
        self.secret_base = secret_base
        self.active = active
        self.members = []

    def add_member(self, name: str, age: int, secretidentity: str, powers: list):
        new_member = Member(name, age, secretidentity, powers)
        self.members.append(new_member)

    def output_squad(self, squad_number):
        if squad_number < len(squads):
            squad = squads[squad_number]
            print(f"Squad Name: {squad.squad_name}, Home Town: {squad.home_town}, Formed: {squad.formed}\n" + "-" * 70)
            for member in squad.members:
                print(f"  {member}\n")
        
    def list_members_with_uuid(self):
        for member in self.members:
            print(f"Name: {member.name}, UUID: {member.uuid}")

    def remove_member_by_uuid(self, member_uuid):
        self.members = [member for member in self.members if member.uuid != member_uuid]
          
squads = list()
for squad_data in data:
    squad = Squad(squad_data["squadName"], squad_data["homeTown"], squad_data["formed"], "active", squad_data["secretBase"], True)
    for member_data in squad_data["members"]:
        squad.add_member(member_data["name"], member_data["age"], member_data["secretIdentity"], member_data["powers"])
    squads.append(squad)



'''x = int(input("zu welchem Team soll Ironman hinzugefügt werden(0-10): "))
squads[x].add_member("Ironman", 41, "Tony Stark", ["Fighting", "Lasers"])'''

'''for squad in squads:'''
squads[0].list_members_with_uuid()

squads[0].remove_member_by_uuid(input("gebe die ID des zu löschenden Members an: "))

squads[0].output_squad(0)

'''for squad in squads:
    print(f"Squad Name: {squad.squad_name}, Home Town: {squad.home_town}, Formed: {squad.formed}" "\n", "-" * 70 )
    for member in squad.members:
        print(f"  {member}", "\n")
'''
        
'''squads[1].add_member("Ironman", 31, "Tony Stark", ["Fighting", "Lasers"])'''

'''def add_member_to_avengers(data, name, age, secretidentity, powers):
    for squad in data: 
        if squad['squadName'] == "Avengers":
            new_member = {
                "name": name,
                "age": age,
                "secretidentity": secretidentity,
                "powers": powers
            }
            squad['members'].append(new_member)
            break
'''
'''add_member_to_avengers(data, "Iron Man", 30, "Tony Stark", ["Fighting", "Lasers"])'''

print()
"""Avengers = Squad("Avengers", "New York", 2012, "Stark Tower", "good", True)
Avengers.addMember()"""

'''member_1 = Member("Superman", 2523, "Vorname Nachname", ["Laser Eyes", "Flying"])'''


'''Squad.ausgabe = {
            "squadName": squad_name,
	    "homeTown": home_town,
	    "formed": formed,
	    "status": status,
	    "secretBase": secret_base,
	    "active": active,
	    "members": {
            "name": name,
			"age": age,
			"secretIdentity": secret_identity,
			"powers": powers
            }
        }'''

