"""Module to hold 5e Race definitions"""

import random

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

DWARF = {
    "Name": "Dwarf",
    "Abilities": {"Constitution": 2},
    "Size": "Medium",
    "Speed": 25,
    "Darkvision": 60,
    "Weapon Proficiencies": [
        "Battleaxe",
        "Handaxe",
        "Throwing Hammer",
        "Warhammer",
        ],
    "Tool Proficiencies": get_dwarf_tools(),
    "Languages": ["Dwarvish", "Common"],
    "Powers": [
        {
            "Name": "Dwarven Resilience",
            "Text": "You have advantage on saving throws against poison, and "
                    "you have resistance against poison damage"
        },
        {
            "Name": "Stonecunning",
            "Text": "Whenever you make an Intelligence (History) check "
                    "related to the origin of stonework, you are considered "
                    "proficient in the History skill and add double your "
                    "proficiency bonus to the check, instead of your normal "
                    "proficiency bonus."
        }
    ],
    "Subraces": ["Hill", "Mountain"]
}

ELF = {
    "Name": "Elf",
    "Abilities": {"Dexterity": 2},
    "Size": "Medium",
    "Speed": 30,
    "Darkvision": 60,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["Elvish", "Common"],
    "Powers": [
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
    ],
    "Subraces": ["High Elf", "Wood Elf", "Drow"]
}

HALFLING = {
    "Name": "Halfling",
    "Abilities": {"Dexterity": 2},
    "Size": "Small",
    "Speed": 25,
    "Darkvision": 0,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["Halfling", "Common"],
    "Powers": [
        {
            "Name": "Lucky",
            "Text": "When you roll a 1 on an attack roll, ability check, or "
                    "saving throw, you can reroll the die and must use the "
                    "new roll."
        },
        {
            "Name": "Brave",
            "Text": "You have advantage on saving throws against being "
                    "frightened."
        },
        {
            "Name": "Halfling Nimbleness",
            "Text": "You can move through the space of any creature that is "
                    "of a size larger than yours."
        },
    ],
    "Subraces": ["Lightfoot", "Stout"]
}

HUMAN = {
    "Name": "Human",
    "Abilities": {
        "Strength": 1, "Dexterity": 1, "Constitution": 1,
        "Intelligence": 1, "Wisdom": 1, "Charisma": 1
        },
    "Size": "Medium",
    "Speed": 30,
    "Darkvision": 0,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["One more", "Common"],
    "Powers": [],
}

DRAGONBORN = {
    "Name": "Dragonborn",
    "Abilities": {"Strength": 2, "Charisma": 1},
    "Size": "Medium",
    "Speed": 30,
    "Darkvision": 0,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["Draconic", "Common"],
    "Powers": [
        {
            "Name": "Draconic Ancestry",
            "Text": "You have draconic ancestry. Choose one type of dragon "
                    "from the Draconic Ancestry table."
        },
        {
            "Name": "Breath Weapon",
            "Text": "You can use your action to exhale destructive energy. "
                    "Your draconic ancestry determines the size, shape, and "
                    "damage type of the exhalation. When you use your breath "
                    "weapon, each creature in the area of the exhalation must "
                    "make a saving throw, the type of which is determined by "
                    "your draconic ancestry. The DC for this saving throw "
                    "equals 8 + your Constitution modifier + your proficiency "
                    "bonus. A creature takes 2d6 damage on a failed save, and "
                    "half as much damage on a successful one. The damage "
                    "increases to 3d6 at 6th level, 4d6 at 11th level, and "
                    "5d6 at 16th level."

        },
        {
            "Name": "Damage Resistance",
            "Text": "You have resistance to the damage type associated with "
                    "your draconic ancestry."
        },
    ],
}

GNOME = {
    "Name": "Gnome",
    "Abilities": {"Intelligence": 2},
    "Size": "Small",
    "Speed": 25,
    "Darkvision": 60,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["Gnomish", "Common"],
    "Powers": [
        {
            "Name": "Gnome Cunning",
            "Text": "You have advantage on all Intelligence, Wisdom, and "
                    "Charisma saving throws against magic."
        },
        {
            "Name": "Stonecunning",
            "Text": "Whenever you make an Intelligence (History) check "
                    "related to the origin of stonework, you are considered "
                    "proficient in the History skill and add double your "
                    "proficiency bonus to the check, instead of your normal "
                    "proficiency bonus."
        }
    ],
    "Subraces": ["Forest", "Rock"]
}

HALFELF = {
    "Name": "Half-Elf",
    "Abilities": halfelf_abilities(),
    "Size": "Medium",
    "Speed": 30,
    "Darkvision": 60,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["Elvish", "Common", "One more"],
    "Skills": halfelf_skills(),
    "Powers": [
        {
            "Name": "Fey Ancestry",
            "Text": "You have advantage on saving throws against being"
                    " charmed, and magic can’t put you to sleep."
        },
    ],
}

HALFORC = {
    "Name": "Half-Orc",
    "Abilities": {"Strength": 2, "Constitution": 1},
    "Size": "Medium",
    "Speed": 30,
    "Darkvision": 60,
    "Weapon Proficiencies": [],
    "Tool Proficiencies": [],
    "Languages": ["Orc", "Common"],
    "Skills": ["Intimidation"],
    "Powers": [
        {
            "Name": "Relentless Endurance",
            "Text": "When you are reduced to 0 hit points but not killed "
                    "outright, you can drop to 1 hit point instead. You can’t "
                    "use this feature again until you finish a long rest."
        },
        {
            "Name": "Savage Attacks",
            "Text": "When you score a critical hit with a melee weapon "
                    "attack, you can roll one of the weapon’s damage dice one "
                    "additional time and add it to the extra damage of the "
                    "critical hit."
        }
    ],
}

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

RACES = {
    "Dwarf": DWARF,
    "Elf": ELF,
    "Halfling": HALFLING,
    "Human": HUMAN,
    "Dragonborn": DRAGONBORN,
    "Gnome": GNOME,
    "Half-Elf": HALFELF,
    "Half-Orc": HALFORC,
    "Tiefling": TIEFLING,
    }


def subrace_dwarf(subrace):
    """Set Dwarf subrace values"""
    if "Hill" in subrace:
        RACES["Dwarf"]["Abilities"]["Wisdom"] = 1
    elif "Mountain" in subrace:
        RACES["Dwarf"]["Abilities"]["Strength"] = 2
        RACES["Dwarf"]["Armor Proficiencies"] = ["Light", "Medium"]
    else:
        return "Invalid subrace choice"


def subrace_elf(subrace):
    """Set Elf subrace values"""
    if "High" in subrace:
        RACES["Elf"]["Abilities"]["Intelligence"] = 1
        RACES["Elf"]["Weapon Proficiencies"] = [
            "Longsword", "Shortsword", "Shortbow", "Longbow"
            ]
        RACES["Elf"]["Powers"].append({
            "Name": "Extra cantrip",
            "Text": "You know one extra cantrip of your choice from the "
                    "wizard spell list. Intelligence is your spellcasting "
                    "ability for it"
            })
        RACES["Elf"]["Languages"].append("One extra")
    elif "Wood" in subrace:
        RACES["Elf"]["Abilities"]["Wisdom"] = 1
        RACES["Elf"]["Weapon Proficiencies"] = [
            "Longsword", "Shortsword", "Shortbow", "Longbow"
            ]
        RACES["Elf"]["Powers"].append({
            "Name": "Mask of the Wild",
            "Text": "You can attempt to hide even when you are only "
                    "lightly obscured by foliage, heavy rain, falling "
                    "snow, mist, and other natural phenomena."
            })
    elif "Drow" in subrace:
        RACES["Elf"]["Abilities"]["Charisma"] = 1
        RACES["Elf"]["Darkvision"] = 120
        RACES["Elf"]["Powers"].append({
            "Name": "Sunlight Sensitivity",
            "Text": "You have disadvantage on attack rolls and on Wisdom "
                    "(Perception) checks that rely on sight when you, "
                    "the target of your attack, or whatever you are "
                    "trying to perceive is in direct sunlight."
            })
        RACES["Elf"]["Powers"].append({
            "Name": "Drow Magic",
            "Text": "You know the dancing lights cantrip. When you reach "
                    "3rd level, you can cast the faerie fire spell once "
                    "per day. When you reach 5th level, you can also cast "
                    "the darkness spell once per day. Charisma is your "
                    "spellcasting ability for these spells."
            })
        RACES["Elf"]["Weapon Proficiencies"] = [
            "Rapier", "Shortsword", "Crossbow, hand"
            ]
    else:
        return "Invalid subrace choice"


def subrace_halfling(subrace):
    """Set Halfling subrace values"""
    if "Lightfoot" in subrace:
        RACES["Halfling"]["Abilities"]["Charisma"] = 1
        RACES["Halfling"]["Powers"].append({
            "Name": "Naturally Stealthy",
            "Text": "You can attempt to hide even when you are obscured "
                    "only by a creature that is at least one size larger "
                    "than you."
            })
    elif "Stout" in subrace:
        RACES["Halfling"]["Abilities"]["Constitution"] = 1
        RACES["Halfling"]["Powers"].append({
            "Name": "Stout Resilience",
            "Text": "You have advantage on saving throws against poison, "
                    "and you have resistance against poison damage"
            })
    else:
        return "Invalid subrace choice"


def subrace_gnome(subrace):
    """Set Gnome subrace values"""
    if "Forest" in subrace:
        RACES["Gnome"]["Abilities"]["Dexterity"] = 1
        RACES["Gnome"]["Powers"].append({
            "Name": "Natural Illusionist",
            "Text": "You know the minor illusion cantrip. Intelligence is "
                    "your spellcasting ability for it."
            })
        RACES["Gnome"]["Powers"].append({
            "Name": "Speak with Small Beasts",
            "Text": "Through sounds and gestures, you can communicate "
                    "simple ideas with Small or smaller beasts. Forest "
                    "gnomes love animals and often keep squirrels, "
                    "badgers, rabbits, moles, woodpeckers, and other "
                    "creatures as beloved pets."
            })
    elif "Rock" in subrace:
        RACES["Gnome"]["Abilities"]["Constitution"] = 1
        RACES["Gnome"]["Powers"].append({
            "Name": "Artificer's Lore",
            "Text": "Whenever you make an Intelligence (History) check "
                    "related to magic items, alchemical objects, or "
                    "technological devices, you can add twice your "
                    "proficiency bonus, instead of any proficiency bonus "
                    "you normally apply."
            })
        RACES["Gnome"]["Powers"].append({
            "Name": "Tinker",
            "Text": "You have proficiency with artisan’s tools (tinker’s "
                    "tools). Using those tools, you can spend 1 hour and "
                    "10 gp worth of materials to construct a Tiny "
                    "clockwork device (AC 5, 1 hp)."
            })
    else:
        return "Invalid subrace choice"


def get_subrace(race, subrace):
    """Method to add subracial characteristics"""
    if race == "Dwarf":
        subrace_dwarf(subrace)
    elif race == "Elf":
        subrace_elf(subrace)
    elif race == "Halfling":
        subrace_halfling(subrace)
    elif race == "Gnome":
        subrace_gnome(subrace)
