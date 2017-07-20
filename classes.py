"""Module to hold 5e Class definitions"""

import random

CLASSES = {"1": "Barbarian"}


class Barbarian(object):
    """Barbarian Class definition"""
    def __init__(self):
        self.primary = "Strength"
        self.secondary = "Constitution"
        self.armor_proficiencies = ["Light", "Medium", "Shields"]
        self.weapon_proficiencies = ["Simple", "Martial"]
        self.tool_proficiencies = []
        self.saves = ["Strength", "Constitution"]
        self.hit_dice = 12

    def get_skills(self, level=0):
        """Figure out what skills a Barbaian has"""
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
        skills = [first_skill, second_skill]
        return skills

    def find_powers(self, level):
        """Figure out what powers they have for their level"""
        powers = [
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
        acquired = []
        for power in powers:
            if power["Level"] <= level:
                acquired.append(power)
        return acquired
