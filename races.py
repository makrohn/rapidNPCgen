"""Module to hold 5e Race definitions"""

import random
import json

RACE_LIST = [
    "Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf",
    "Half-Orc", "Tiefling"
    ]


def get_dwarf_tools():
    """Method to get dwarf tools"""
    tools = ["Smith's Tools", "Brewer's Tools", "Mason's Tools"]
    tools = [random.choice(tools)]
    return tools


def halfelf_abilities():
    """Pick two ability bonuses for the Half-Elf"""
    abilities = {"Charisma": 2}
    options = ["Strength", "Dexterity", "Intelligence", "Constitution",
               "Wisdom"]
    stat_one = random.choice(options)
    options.remove(stat_one)
    stat_two = random.choice(options)
    abilities[stat_one] = 1
    abilities[stat_two] = 1
    return abilities


def halfelf_skills():
    """Figure out what skills a Half-Elf has"""
    skills_list = [
        'Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
        'Deception', 'History', 'Insight', 'Intimidation',
        'Investigation', 'Medicine', 'Nature', 'Perception',
        'Performance', 'Persuasion', 'Religion', 'Sleight of Hand',
        'Stealth', 'Survival'
        ]
    first_skill = random.choice(skills_list)
    skills_list.remove(first_skill)
    second_skill = random.choice(skills_list)
    skills = [first_skill, second_skill]
    return skills

TIEFLING = {
    "Name": "Tiefling",
    "Abilities": {"Charisma": 2, "Intelligence": 1},
    "Size": "Medium",
    "Speed": 30,
    "Darkvision": 60,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["Infernal", "Common"],
    "Powers": [
        {
            "Name": "Hellish Resistance",
            "Text": "You have resistance to fire damage."
        },
        {
            "Name": "Infernal Legacy",
            "Text": "You know the thaumaturgy cantrip. Once you reach 3rd "
                    "level, you can cast the hellish rebuke spell once per "
                    "day as a 2nd-level spell. Once you reach 5th level, you "
                    "can also cast the darkness spell once per day. Charisma "
                    "is your spellcasting ability for these spells."
        }
    ],
}


def subrace_dwarf(race_def, subrace):
    """Set Dwarf subrace values"""
    if "Hill" in subrace:
        race_def["Abilities"]["Wisdom"] = 1
    elif "Mountain" in subrace:
        race_def["Abilities"]["Strength"] = 2
        race_def["Armor Proficiencies"] = ["Light", "Medium"]
    else:
        print("Invalid subrace choice")
    return race_def

def subrace_elf(race_def, subrace):
    """Set Elf subrace values"""
    if "High" in subrace:
        race_def["Abilities"]["Intelligence"] = 1
        race_def["Weapon Proficiencies"] = [
            "Longsword", "Shortsword", "Shortbow", "Longbow"
            ]
        race_def["Powers"].append({
            "Name": "Extra cantrip",
            "Text": "You know one extra cantrip of your choice from the "
                    "wizard spell list. Intelligence is your spellcasting "
                    "ability for it"
            })
        race_def["Languages"].append("One extra")
    elif "Wood" in subrace:
        race_def["Abilities"]["Wisdom"] = 1
        race_def["Weapon Proficiencies"] = [
            "Longsword", "Shortsword", "Shortbow", "Longbow"
            ]
        race_def["Powers"].append({
            "Name": "Mask of the Wild",
            "Text": "You can attempt to hide even when you are only "
                    "lightly obscured by foliage, heavy rain, falling "
                    "snow, mist, and other natural phenomena."
            })
    elif "Drow" in subrace:
        race_def["Abilities"]["Charisma"] = 1
        race_def["Darkvision"] = 120
        race_def["Powers"].append({
            "Name": "Sunlight Sensitivity",
            "Text": "You have disadvantage on attack rolls and on Wisdom "
                    "(Perception) checks that rely on sight when you, "
                    "the target of your attack, or whatever you are "
                    "trying to perceive is in direct sunlight."
            })
        race_def["Powers"].append({
            "Name": "Drow Magic",
            "Text": "You know the dancing lights cantrip. When you reach "
                    "3rd level, you can cast the faerie fire spell once "
                    "per day. When you reach 5th level, you can also cast "
                    "the darkness spell once per day. Charisma is your "
                    "spellcasting ability for these spells."
            })
        race_def["Weapon Proficiencies"] = [
            "Rapier", "Shortsword", "Crossbow, hand"
            ]
    else:
        print("Invalid subrace choice")
    return race_def


def subrace_halfling(race_def, subrace):
    """Set Halfling subrace values"""
    if "Lightfoot" in subrace:
        race_def["Abilities"]["Charisma"] = 1
        race_def["Powers"].append({
            "Name": "Naturally Stealthy",
            "Text": "You can attempt to hide even when you are obscured "
                    "only by a creature that is at least one size larger "
                    "than you."
            })
    elif "Stout" in subrace:
        race_def["Abilities"]["Constitution"] = 1
        race_def["Powers"].append({
            "Name": "Stout Resilience",
            "Text": "You have advantage on saving throws against poison, "
                    "and you have resistance against poison damage"
            })
    else:
        print("Invalid subrace choice")
    return race_def


def subrace_gnome(race_def, subrace):
    """Set Gnome subrace values"""
    if "Forest" in subrace:
        race_def["Abilities"]["Dexterity"] = 1
        race_def["Powers"].append({
            "Name": "Natural Illusionist",
            "Text": "You know the minor illusion cantrip. Intelligence is "
                    "your spellcasting ability for it."
            })
        race_def["Powers"].append({
            "Name": "Speak with Small Beasts",
            "Text": "Through sounds and gestures, you can communicate "
                    "simple ideas with Small or smaller beasts. Forest "
                    "gnomes love animals and often keep squirrels, "
                    "badgers, rabbits, moles, woodpeckers, and other "
                    "creatures as beloved pets."
            })
    elif "Rock" in subrace:
        race_def["Abilities"]["Constitution"] = 1
        race_def["Powers"].append({
            "Name": "Artificer's Lore",
            "Text": "Whenever you make an Intelligence (History) check "
                    "related to magic items, alchemical objects, or "
                    "technological devices, you can add twice your "
                    "proficiency bonus, instead of any proficiency bonus "
                    "you normally apply."
            })
        race_def["Powers"].append({
            "Name": "Tinker",
            "Text": "You have proficiency with artisan’s tools (tinker’s "
                    "tools). Using those tools, you can spend 1 hour and "
                    "10 gp worth of materials to construct a Tiny "
                    "clockwork device (AC 5, 1 hp)."
            })
    else:
        print("Invalid subrace choice")
    return race_def


def load_race_file(racename, subrace=""):
    """Load a race's json file and sets other attributes as needed"""
    filename = "races/" + racename.lower() + '.json'
    with open(filename) as race_file:
        race_definition = json.loads(race_file.read())
    if racename == "Dwarf":
        race_definition["Tool Proficiencies"] = get_dwarf_tools()
        race_definition = subrace_dwarf(race_definition, subrace)
    if racename == "Elf":
        race_definition = subrace_elf(race_definition, subrace)
    if racename == "Halfling":
        race_definition = subrace_halfling(race_definition, subrace)
    if racename == "Gnome":
        race_definition = subrace_gnome(race_definition, subrace)
    if racename == "Half-Elf":
        race_definition["Abilities"] = halfelf_abilities()
        race_definition["Skills"] = halfelf_skills()
    return race_definition
