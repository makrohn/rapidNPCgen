"""Module to hold 5e Race definitions"""

import random

RACES = {"1": "Dwarf"}


class Dwarf(object):
    """Dwarf Class definition"""
    def __init__(self):
        self.abilities = {"Constitution": 2}
        self.size = "Medium"
        self.speed = 25
        self.darkvision = 60
        self.weapon_proficiencies = [
            "Battleaxe",
            "Handaxe",
            "Throwing Hammer",
            "Warhammer",
            ]
        self.tool_proficiencies = [random.choice([
            "Smith's Tools",
            "Brewer's Tools",
            "Mason's Tools",
            ])]
        self.languages = ["Dwarvish", "Common"]
        self.powers = [
            {
                "Name": "Dwarven Resilience",
                "Text": "You have advantage on saving throws against poison, "
                        "and you have resistance against poison damage"
            },
            {
                "Name": "Stonecunning",
                "Text": "Whenever you make an Intelligence (History) check "
                        "related to the origin of stonework, you are "
                        "considered proficient in the History skill and add "
                        "double your proficiency bonus to the check, instead "
                        "of your normal proficiency bonus."
            }
            ]
        self.has_subrace = True
        self.subrace_choices = ["Hill", "Mountain"]

    def subrace(self, subrace_choice):
        """Add subrace attributes"""
        if "Hill" in subrace_choice:
            self.abilities["Wisdom"] = 1
            self.powers.append({
                "Name": "Dwarven Toughness",
                "Text": "Your hit point maximum increases by 1, and "
                               "it increases by 1 every time you gain a level."
                })
        elif "Mountain" in subrace_choice:
            self.abilities["Strength"] = 2
            self.armor_proficiencies = ["Light", "Medium",]
        else:
            return "Invalid subrace choice"
