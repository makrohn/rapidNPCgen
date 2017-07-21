"""Module to hold 5e Class definitions"""

import random
import json

CLASS_LIST = ["Barbarian", "Bard", "Cleric", "Druid"]


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


def load_class_file(classname):
    """Load a class's json file"""
    filename = "classes/" + classname.lower() + '.json'
    with open(filename) as class_file:
        class_definition = json.loads(class_file.read())
    if classname == "Bard":
        class_definition["Tool Proficiencies"] = get_instruments()
    return class_definition
