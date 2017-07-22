"""Module to hold 5e Class definitions"""

import random
import json

CLASS_LIST = [
    "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
    "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard",
    ]


def get_instruments():
    """Figure out the Bard's instruments"""
    instruments_list = [
        "Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn",
        "Pan flute", "Shawm", "Viol"
        ]
    first_instrument = random.choice(instruments_list)
    instruments_list.remove(first_instrument)
    second_instrument = random.choice(instruments_list)
    instruments_list.remove(second_instrument)
    third_instrument = random.choice(instruments_list)
    instruments = [first_instrument, second_instrument, third_instrument]
    return instruments


def choose_fighter_primary():
    """Choose either Strength or Dex as Fighter's primary stat"""
    primaries = ["Strength", "Dexterity"]
    primary = random.choice(primaries)
    return primary


def choose_fighting_style(styles_list):
    """Choose a character's fighting style"""
    styles = [
        {
            "Name": "Archery",
            "Text": "You gain a +2 bonus to attack rolls you make with ranged "
                    "weapons.",
            "Level": 1
        },
        {
            "Name": "Defense",
            "Text": "While you are wearing armor, you gain a +1 bonus to AC.",
            "Level": 1
        },
        {
            "Name": "Dueling",
            "Text": "When you are wielding a melee weapon in one hand and no "
                    "other weapons, you gain a +2 bonus to damage rolls with "
                    "that weapon.",
            "Level": 1
        },
        {
            "Name": "Great Weapon Fighting",
            "Text": "When you roll a 1 or 2 on a damage die for an attack you "
                    "make with a melee weapon that you are wielding with two "
                    "hands, you can reroll the die and must use the new roll, "
                    "even if the new roll is a 1 or a 2. The weapon must have "
                    "the two-handed or versatile property for you to gain "
                    "this benefit.",
            "Level": 1
        },
        {
            "Name": "Protection",
            "Text": "When a creature you can see attacks a target other than "
                    "you that is within 5 feet of you, you can use your "
                    "reaction to impose disadvantage on the attack roll. You "
                    "must be wielding a shield.",
            "Level": 1
        },
        {
            "Name": "Two-Weapon Fighting",
            "Text": "When you engage in two-weapon fighting, you can add your "
                    "ability modifier to the damage of the second attack.",
            "Level": 1
        },
    ]
    valid = False
    while not valid:
        style = random.choice(styles)
        if style["Name"] in styles_list:
            valid = True
    return style


def get_monk_tools():
    """Figure out the Monk's tool"""
    instruments_list = [
        "Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn",
        "Pan flute", "Shawm", "Viol"
        ]
    artisan_list = []
    monk_tools = instruments_list + artisan_list
    tool = [random.choice(monk_tools)]
    return tool


def load_class_file(classname):
    """Load a class's json file"""
    filename = "classes/" + classname.lower() + '.json'
    with open(filename) as class_file:
        class_definition = json.loads(class_file.read())
    if classname == "Bard":
        class_definition["Tool Proficiencies"] = get_instruments()
    if classname == "Fighter":
        class_definition["Primary"] = choose_fighter_primary()
        class_definition["Powers"].append(
            choose_fighting_style(class_definition["Styles List"])
            )
    if classname == "Monk":
        class_definition["Tool Proficiencies"] = get_monk_tools()
    if classname == "Paladin":
        class_definition["Powers"].append(
            choose_fighting_style(class_definition["Styles List"])
            )
    return class_definition
