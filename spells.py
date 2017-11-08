"""Module to handle rapid spell assignation"""

import random
import math
import json
import collections

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
    classname = classname.lower()
    if classname == "bard":
        spells_per_level = [
            4, 5, 6, 7, 8, 9, 10, 11, 12, 14,
            15, 15, 16, 18, 19, 19, 20, 22, 22, 22
            ]
        spells_known_total = spells_per_level[level-1]
        return spells_known_total
    if classname == "sorceror":
        spells_per_level = [
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            12, 12, 13, 13, 14, 14, 15, 15, 15, 15
            ]
        spells_known_total = spells_per_level[level-1]
        return spells_known_total
    if classname == "warlock":
        spells_per_level = [
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
            11, 11, 12, 12, 13, 13, 14, 14, 15, 15
            ]
        spells_known_total = spells_per_level[level-1]
        return spells_known_total
    elif (classname == "cleric" or
          classname == "druid" or classname == "wizard"):
        spells_prepared = level + casting_mod
        return spells_prepared
    elif classname == "paladin" or classname == "ranger":
        spells_prepared = math.floor(level/2) + casting_mod
        return spells_prepared

with open('rpcg_web/spells.json') as spell_file:
    SPELL_LIST = json.loads(spell_file.read())


def get_highest_spell_slot(char_class, level):
    """Get the highest level spell slot available to the NPC"""
    if char_class in ["Paladin", "Ranger"]:
        spell_level = math.ceil(level/2)
        if level == 1:
            spell_level = 0
    else:
        spell_level = level
    if char_class == "Warlock":
        if level < 10:
            highest_known = math.ceil(level/2)
        elif level >= 10:
            highest_known = 5
    else:
        highest_known = len(SPELL_SLOTS_MATRIX[str(spell_level)])
    return highest_known


def spells_known(level, char_class, casting_mod):
    """Create a random spell list for a character"""
    if (char_class == "Paladin" or char_class == "Ranger") and level == 1:
        return []
    highest_known = get_highest_spell_slot(char_class, level)
    spells_available = []
    counter = highest_known
    class_list = []
    for spell in SPELL_LIST:
        if spell["level"] != "cantrip":
            if (int(spell["level"]) <= highest_known and char_class.lower() in spell["classes"]):
                class_list.append(spell)
    for spell in class_list:
        print(spell["name"])
    # while counter > 0:
    #     spells_available += (SPELL_LISTS[char_class][str(counter)])
    #     counter -= 1
    remaining_known = calc_spells_known(char_class, level, casting_mod)
    spell_list = []
    while remaining_known > 0:
        new_spell = random.choice(class_list)
        spell_list.append(new_spell)
        class_list.remove(new_spell)
        remaining_known -= 1
    if char_class == "Warlock":
        if level > 11:
            spell_list.append(random.choice(SPELL_LISTS["Warlock"]["6"]))
        if level > 13:
            spell_list.append(random.choice(SPELL_LISTS["Warlock"]["7"]))
        if level > 15:
            spell_list.append(random.choice(SPELL_LISTS["Warlock"]["8"]))
        if level > 17:
            spell_list.append(random.choice(SPELL_LISTS["Warlock"]["9"]))
    return spell_list


def spell_slots(level, char_class):
    """Show spell slots"""
    if char_class in ["Paladin", "Ranger"]:
        caster_level = math.ceil(level/2)
        if level == 1:
            caster_level = 0
    else:
        caster_level = level
    if char_class == "Warlock":
        if level < 10:
            slot_level = math.ceil(level/2)
        elif level >= 10:
            slot_level = 5
        if level == 1:
            slots = 1
        elif level < 11:
            slots = 2
        elif level < 17:
            slots = 3
        else:
            slots = 4
        spell_slots = collections.OrderedDict()
        spell_slots[slot_level] = slots
        return spell_slots
    else:
        spell_slots = collections.OrderedDict()
        slots_line = SPELL_SLOTS_MATRIX[str(caster_level)]
        print(slots_line)
        slot_level = 1
        for item in slots_line:
            spell_slots[slot_level] = item
            slot_level += 1
        print(spell_slots)
        return spell_slots
