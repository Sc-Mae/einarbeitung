"""Bearbeitung Aufgabe 02"""

import uuid
import json

with open("base.json", "r", encoding="utf-8") as data_file:
    data = json.load(data_file)


class Member:
    """Initierung der Member Klasse"""

    def __init__(self, name: str, age: int, secretidentity: str, powers: list) -> None:
        self._name = name
        self._age = age
        self._secretidentity = secretidentity
        self._powers = powers
        self._uuid = str(uuid.uuid4())

    def __str__(self) -> str:
        return f"Name:{self._name}, Age: {self._age}, \
             Secret Identity: {self._secretidentity}, Powers: {', '.join(self._powers)}"

    def get_name(self) -> str:
        return self._name

    def get_uuid(self) -> str:
        return self._uuid


class Squad:
    """Initierung der Squad Klasse"""

    def __init__(
        self,
        squad_name: str,
        home_town: str,
        formed: int,
        status: str,
        secret_base: str,
        active: bool,
    ) -> None:
        self._squad_name = squad_name
        self._home_town = home_town
        self._formed = formed
        self._status = status
        self._secret_base = secret_base
        self._active = active
        self._members = []

    def add_member(
        self, name: str, age: int, secretidentity: str, powers: list
    ) -> None:
        """Funktion zum Hinzufügen eines neuen Members"""
        new_member = Member(name, age, secretidentity, powers)
        self._members.append(new_member)

    def output_squad(self, squad_number) -> None:
        """Ausgabe eines Squads und dessen Member"""
        if squad_number < len(squads):
            squad = squads[squad_number]
            print(
                f"Squad Name: {squad._squad_name}, Home Town: {squad._home_town}, \
                Formed: {squad._formed}\n"
                + "-" * 70
            )
            for member in squad._members:
                print(f"  {member}\n")

    def list_members_with_uuid(self) -> None:
        """Erstelle eine Liste der member und zeigt ihre uuid"""
        for member in self._members:
            print(f"Name: {member.get_name()}, UUID: {member.get_uuid()}")

    def remove_member_by_uuid(self, member_uuid) -> None:
        """Methoode zum löschen eines Members anhand der uuid"""
        self._members = [
            member for member in self._members if member.get_uuid() != member_uuid
        ]


squads = []
for squad_data in data:
    squad_int = Squad(
        squad_data["squadName"],
        squad_data["homeTown"],
        squad_data["formed"],
        "active",
        squad_data["secretBase"],
        True,
    )
    for member_data in squad_data["members"]:
        squad_int.add_member(
            member_data["name"],
            member_data["age"],
            member_data["secretIdentity"],
            member_data["powers"],
        )
    squads.append(squad_int)

x = int(input("zu welchem Team soll Ironman hinzugefügt werden(0-10): "))
squads[x].add_member("Ironman", 41, "Tony Stark", ["Fighting", "Lasers"])

squads[0].list_members_with_uuid()

squads[0].remove_member_by_uuid(input("gebe die ID des zu löschenden Members an: "))

squads[0].output_squad(0)
