"""Module to handle rapid spell assignation"""

import random
import math

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
    if classname == "Cleric":
        spells_prepared = level + casting_mod
        return spells_prepared

SPELL_LISTS = {
    "Bard": {
        "1": [
            "Animal Friendship", "Bane", "Charm Person",
            "Comprehend Languages", "Cure Wounds", "Detect Magic",
            "Disguise Self", "Dissonant Whispers", "Faerie Fire",
            "Feather Fall", "Healing Word", "Heroism", "Identify",
            "Illusory Script", "Longstrider", "Silent Image", "Sleep",
            "Speak with Animals", "Tasha’s Hideous Laughter", "Thunderwave",
            "Unseen Servant"
            ],
        "2": [
            "Animal Messenger", "Blindness/Deafness", "Calm Emotions",
            "Cloud of Daggers", "Crown of Madness", "Detect Thoughts",
            "Enhance Ability", "Enthrall", "Heat Metal", "Hold Person",
            "Invisibility", "Knock", "Lesser Restoration",
            "Locate Animals or Plants", "Locate Object", "Magic Mouth",
            "Phantasmal Force", "See Invisibility", "Shatter", "Silence",
            "Suggestion", "Zone of Truth",
            ],
        "3": [
            "Bestow Curse", "Clairvoyance", "Dispel Magic", "Fear",
            "Feign Death", "Glyph of Warding", "Hypnotic Pattern",
            "Leomund’s Tiny Hut", "Major Image", "Nondetection",
            "Plant Growth", "Sending", "Speak with Dead", "Speak with Plants",
            "Stinking Cloud", "Tongues",
            ],
        "4": [
            "Compulsion", "Confusion", "Dimension Door", "Freedom of Movement",
            "Greater Invisibility", "Hallucinatory Terrain", "Locate Creature",
            "Polymorph",
            ],
        "5": [
            "Animate Objects", "Awaken", "Dominate Person", "Dream", "Geas",
            "Greater Restoration", "Hold Monster", "Legend Lore",
            "Mass Cure Wounds", "Mislead", "Modify Memory", "Planar Binding",
            "Raise Dead", "Scrying", "Seeming", "Teleportation Circle",
            ],
        "6": [
            "Eyebite", "Find the Path", "Guards and Wards", "Mass Suggestion",
            "Otto’s Irresistible Dance", "Programmed Illusion", "True Seeing",
            ],
        "7": [
            "Etherealness", "Forcecage", "Mirage Arcane",
            "Mordenkainen’s Magnificent Mansion", "Mordenkainen’s Sword",
            "Project Image", "Regenerate", "Resurrection", "Symbol",
            "Teleport",
            ],
        "8": [
            "Dominate Monster", "Feeblemind", "Glibness", "Mind Blank",
            "Power Word Stun",
            ],
        "9": [
            "Foresight", "Power Word Heal", "Power Word Kill",
            "True Polymorph",
            ],
        },
    "Cleric": {
        "1": [
            "Bane", "Bless", "Command", "Create or Destroy Water",
            "Cure Wounds", "Detect Evil and Good", "Detect Magic",
            "Detect Poison and Disease", "Guiding Bolt", "Healing Word",
            "Inflict Wounds", "Protection from Evil and Good",
            "Purify Food and Drink", "Sanctuary", "Shield of Faith",
            ],
        "2": [
            "Aid", "Augury", "Blindness/Deafness", "Calm Emotions",
            "Continual Flame", "Enhance Ability", "Find Traps",
            "Gentle Repose", "Hold Person", "Lesser Restoration",
            "Locate Object", "Prayer of Healing", "Protection from Poison",
            "Silence", "Spiritual Weapon", "Warding Bond", "Zone of Truth",
            ],
        "3": [
            "Animate Dead", "Beacon of Hope", "Bestow Curse", "Clairvoyance",
            "Create Food and Water", "Daylight", "Dispel Magic", "Feign Death",
            "Glyph of Warding", "Magic Circle", "Mass Healing Word",
            "Meld into Stone", "Protection from Energy", "Remove Curse",
            "Revivify", "Sending", "Speak with Dead", "Spirit Guardians",
            "Tongues", "Water Walk",
            ],
        "4": [
            "Banishment", "Control Water", "Death Ward", "Divination",
            "Freedom of Movement", "Guardian of Faith", "Locate Creature",
            "Stone Shape",
            ],
        "5": [
            "Commune", "Contagion", "Dispel Evil and Good", "Flame Strike",
            "Geas", "Greater Restoration", "Hallow", "Insect Plague",
            "Legend Lore", "Mass Cure Wounds", "Planar Binding", "Raise Dead",
            "Scrying",
            ],
        "6": [
            "Blade Barrier", "Create Undead", "Find the Path", "Forbiddance",
            "Harm", "Heal", "Heroes’ Feast", "Planar Ally", "True Seeing",
            "Word of Recall",
            ],
        "7": [
            "Conjure Celestial", "Divine Word", "Etherealness", "Fire Storm",
            "Plane Shift", "Regenerate", "Resurrection", "Symbol",
            ],
        "8": [
            "Antimagic Field", "Control Weather", "Earthquake", "Holy Aura",
            ],
        "9": [
            "Astral Projection", "Gate", "Mass Heal", "True Resurrection",
            ],
        },
    "Dummy": {
        "1": [
            ],
        "2": [
            ],
        "3": [
            ],
        "4": [
            ],
        "5": [
            ],
        "6": [
            ],
        "7": [
            ],
        "8": [
            ],
        "9": [
            ],
        },
    }


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
