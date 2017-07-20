"""Choose armor that an NPC is proficient in"""

import math

LIGHT_ARMOR = [
    {"Name": "Padded", "AC": 11, "Dex_max": 10, "Strength": 0, "Disadvantage": True},
    {"Name": "Leather", "AC": 11, "Dex_max": 10, "Strength": 0,
        "Disadvantage": False},
    {"Name": "Studded Leather", "AC": 12, "Dex_max": 10, "Strength": 0,
        "Disadvantage": False},
    ]
MEDIUM_ARMOR = [
    {"Name": "Hide", "AC": 12, "Dex_max": 2, "Strength": 0, "Disadvantage": False},
    {"Name": "Chain Shirt", "AC": 13, "Dex_max": 2, "Strength": 0,
        "Disadvantage": False},
    {"Name": "Scale Mail", "AC": 14, "Dex_max": 2, "Strength": 0,
        "Disadvantage": True},
    {"Name": "Breastplate", "AC": 14, "Dex_max": 2, "Strength": 0,
        "Disadvantage": False},
    {"Name": "Half Plate", "AC": 15, "Dex_max": 2, "Strength": 0,
        "Disadvantage": True},
    ]
HEAVY_ARMOR = [
    {"Name": "Ring Mail", "AC": 14, "Dex_max": 0, "Strength": 0,
        "Disadvantage": True},
    {"Name": "Chain Mail", "AC": 16, "Dex_max": 0, "Strength": 13,
        "Disadvantage": True},
    {"Name": "Splint", "AC": 17, "Dex_max": 0, "Strength": 15, "Disadvantage": True},
    {"Name": "Plate", "AC": 18, "Dex_max": 0, "Strength": 15, "Disadvantage": True},
    ]
SHIELD = [
    {"Name": "Shield", "AC": 2, "Dex_max": 0, "Strength": 0, "Disadvantage": False},
]

def choose_armor(proficiencies, level, strength):
    """Pick some armor for the NPC"""
    if "Heavy" in proficiencies:
        available_armor = []
        for armor in HEAVY_ARMOR:
            if strength >= armor["Strength"]:
                available_armor.append(armor)
    elif "Medium" in proficiencies:
        available_armor = MEDIUM_ARMOR
    elif "Light" in proficiencies:
        available_armor = LIGHT_ARMOR
    armor_potency = math.floor((level-1)/3)
    if len(available_armor) > armor_potency:
        armor_choice = available_armor[armor_potency]
    elif len(available_armor) <= armor_potency:
        armor_choice = available_armor[-1]
        remaining_potency = math.floor(
            (armor_potency - len(available_armor))/2
            )
        if remaining_potency != 0:
            armor_choice["AC"] += remaining_potency
            armor_choice["Name"] += " +" + str(remaining_potency)
    if "Shield" in proficiencies:
        return ([armor_choice, SHIELD[0]])
    else:
        return [armor_choice]
    