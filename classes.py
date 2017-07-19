"""Module to hold 5e Class definitions"""

import random

CLASSES = {"1": "Barbarian"}


class Barbarian(object):
    """Barbarian Class definition"""
    def __init__(self):
        self.__name__ = "Barbarian"
        self.primary = "Strength"
        self.secondary = "Constitution"
        self.hit_dice = 12
        self.armor_proficiencies = ["Light", "Medium", "Shields"]
        self.weapon_proficiencies = ["Simple", "Martial"]
        self.tool_proficiencies = []
        self.saves = ["Strength", "Constitution"]
        skills_list = [
            "Animal Handling",
            "Athletics",
            "Intimidation",
            "Nature",
            "Perception",
            "Survival"
            ]
        first_skill = random.choice(skills_list)
        skills_list.remove(first_skill)
        second_skill = random.choice(skills_list)
        self.skills = [first_skill, second_skill]
        self.powers = [
            {
                "Name": "Rage",
                "Text": "On your turn, you can enter a rage as a bonus "
                        "action.",
                "Level": 1,
            },
            {
                "Name": "Unarmored Defense",
                "Text": "While you are not wearing any armor, your Armor "
                        "Class equals 10 + your Dexterity modifier + your "
                        "Constitution modifier.",
                "Level": 1,
            }
            ]
