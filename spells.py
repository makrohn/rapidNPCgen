"""Module to handle rapid spell assignation"""

import random
import math
import json

SPELL_SLOTS_MATRIX = {
    "0": [],
    "1": [2],
    "2": [3],
    "3": [4, 2],
    "4": [4, 3],
    "5": [4, 3, 2],
    "6": [4, 3, 3],
    "7": [4, 3, 3, 1],
    "8": [4, 3, 3, 2],
    "9": [4, 3, 3, 3, 1],
    "10": [4, 3, 3, 3, 2],
    "11": [4, 3, 3, 3, 2, 1],
    "12": [4, 3, 3, 3, 2, 1],
    "13": [4, 3, 3, 3, 2, 1, 1],
    "14": [4, 3, 3, 3, 2, 1, 1],
    "15": [4, 3, 3, 3, 2, 1, 1, 1],
    "16": [4, 3, 3, 3, 2, 1, 1, 1],
    "17": [4, 3, 3, 3, 2, 1, 1, 1, 1],
    "18": [4, 3, 3, 3, 3, 1, 1, 1, 1],
    "19": [4, 3, 3, 3, 3, 2, 1, 1, 1],
    "20": [4, 3, 3, 3, 3, 2, 2, 1, 1],
    }


def calc_spells_known(classname, level, casting_mod=0):
    """Return number of spells known or prepared"""
    if classname == "Bard":
        spells_per_level = [
            4, 5, 6, 7, 8, 9, 10, 11, 12, 14,
            15, 15, 16, 18, 19, 19, 20, 22, 22, 22
            ]
        spells_known_total = spells_per_level[level-1]
        return spells_known_total
    if classname == "Cleric" or "Druid":
        spells_prepared = level + casting_mod
        return spells_prepared


with open('spells.json') as spell_file:
    SPELL_LISTS = json.loads(spell_file.read())


def spells_known(level, char_class, casting_mod):
    """Create a random spell list for a character"""
    if char_class in ["Paladin", "Ranger"]:
        spell_level = math.ceil(level/2)
        if level == 1:
            spell_level = 0
    else:
        spell_level = level
    highest_known = len(SPELL_SLOTS_MATRIX[str(spell_level)])
    spells_available = []
    counter = highest_known
    while counter > 0:
        spells_available += (SPELL_LISTS[char_class][str(counter)])
        counter -= 1
    remaining_known = calc_spells_known(char_class, level, casting_mod)
    spell_list = []
    while remaining_known > 0:
        new_spell = random.choice(spells_available)
        spell_list.append(new_spell)
        spells_available.remove(new_spell)
        remaining_known -= 1
    return spell_list
