"""Module to hold 5e Race definitions"""

import random

RACES = ["Dwarf", "Elf"]


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
        elif "Mountain" in subrace_choice:
            self.abilities["Strength"] = 2
            self.armor_proficiencies = ["Light", "Medium"]
        else:
            return "Invalid subrace choice"


class Elf(object):
    """Elf Class definition"""
    def __init__(self):
        self.abilities = {"Dexterity": 2}
        self.size = "Medium"
        self.speed = 30
        self.darkvision = 60
        self.skill_proficiencies = ["Perception"]
        self.languages = ["Elvish", "Common"]
        self.tool_proficiencies = []
        self.powers = [
            {
                "Name": "Fey Ancestry",
                "Text": "You have advantage on saving throws against being "
                        "charmed, and magic can’t put you to sleep."
            },
            {
                "Name": "Trance",
                "Text": "Elves don’t need to sleep. Instead, they meditate "
                        "deeply, remaining semiconscious, for 4 hours a day."
            }
            ]
        self.has_subrace = True
        self.subrace_choices = ["High Elf", "Wood Elf", "Drow"]

    def subrace(self, subrace_choice):
        """Add subrace attributes"""
        if "High" in subrace_choice:
            self.abilities["Intelligence"] = 1
            self.weapon_proficiencies = ["Longsword", "Shortsword",
                "Shortbow", "Longbow"]
            self.powers.append({
                "Name": "Extra cantrip",
                "Text": "You know one extra cantrip of your choice from the "
                        "wizard spell list. Intelligence is your spellcasting "
                        "ability for it"
                })
            self.languages.append("One extra")
        elif "Wood" in subrace_choice:
            self.abilities["Wisdom"] = 1
            self.weapon_proficiencies = ["Longsword", "Shortsword",
                "Shortbow", "Longbow"]
            self.powers.append({
                "Name": "Mask of the Wild",
                "Text": "You can attempt to hide even when you are only "
                        "lightly obscured by foliage, heavy rain, falling "
                        "snow, mist, and other natural phenomena."
                })
        elif "Drow" in subrace_choice:
            self.abilities["Charisma"] = 1
            self.darkvision = 120
            self.powers.append({
                "Name": "Sunlight Sensitivity",
                "Text": "You have disadvantage on attack rolls and on Wisdom "
                        "(Perception) checks that rely on sight when you, "
                        "the target of your attack, or whatever you are "
                        "trying to perceive is in direct sunlight."
                })
            self.powers.append({
                "Name": "Drow Magic",
                "Text": "You know the dancing lights cantrip. When you reach "
                        "3rd level, you can cast the faerie fire spell once "
                        "per day. When you reach 5th level, you can also cast "
                        "the darkness spell once per day. Charisma is your "
                        "spellcasting ability for these spells."
                })
            self.weapon_proficiencies = ["Rapier", "Shortsword",
                "Crossbow, hand"]
        else:
            return "Invalid subrace choice"

