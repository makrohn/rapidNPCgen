"""Module to hold 5e Class definitions"""

import random

CLASS_LIST = ["Barbarian", "Bard", "Cleric"]


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

BARBARIAN = {
    "Name": "Barbarian",
    "Primary": "Strength",
    "Secondary": "Constitution",
    "Armor Proficiencies": ["Light", "Medium", "Shields"],
    "Weapon Proficiencies": ["Simple", "Martial"],
    "Tool Proficiencies": [],
    "Saves": ["Strength", "Constitution"],
    "Hit Dice": 12,
    "Skill List": [
        "Animal Handling", "Athletics", "Intimidation",
        "Nature", "Perception", "Survival"
        ],
    "Skill Picks": 2,
    "Powers": [
        {
            "Name": "Rage",
            "Text": "On your turn, you can enter a rage as a bonus action.",
            "Level": 1,
        },
        {
            "Name": "Unarmored Defense",
            "Text": "While you are not wearing any armor, your Armor Class "
                    "equals 10 + your Dexterity modifier + your Constitution "
                    "modifier.",
            "Level": 1,
        },
        {
            "Name": "Reckless Attack",
            "Text": "You can throw aside all concern for defense to attack "
                    "with fierce desperation. When you make your first attack "
                    "on your turn, you can decide to attack recklessly. Doing "
                    "so gives you advantage on melee weapon attack rolls "
                    "using Strength during this turn, but attack rolls "
                    "against you have advantage until your next turn.",
            "Level": 2,
        },
        {
            "Name": "Danger Sense",
            "Text": "You gain an uncanny sense of when things nearby aren’t "
                    "as they should be, giving you an edge when you dodge "
                    "away from danger. You have advantage on Dexterity saving "
                    "throws against effects that you can see, such as traps "
                    "and spells. To gain this benefit, you can’t be blinded, "
                    "deafened, or incapacitated.",
            "Level": 2
        },
    ],
}

BARD = {
    "Name": "Bard",
    "Primary": "Charisma",
    "Secondary": "Dexterity",
    "Armor Proficiencies": ["Light"],
    "Weapon Proficiencies": [
        "Simple", "Crossbow, hand", "Longsword", "Rapier", "Shortsword"
        ],
    "Tool Proficiencies": get_instruments(),
    "Saves": ["Charisma", "Dexterity"],
    "Hit Dice": 8,
    "Skill List": [
        'Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception',
        'History', 'Insight', 'Intimidation', 'Investigation', 'Medicine',
        'Nature', 'Perception', 'Performance', 'Persuasion', 'Religion',
        'Sleight of Hand', 'Stealth', 'Survival'
        ],
    "Skill Picks": 3,
    "Caster": True,
    "Casting Stat": "Charisma",
    "Powers": [
        {
            "Name": "Bardic Inspiration",
            "Text": "Use a bonus action on your turn to choose one creature "
                    "other than yourself within 60 feet of you who can hear "
                    "you. That creature gains one Bardic Inspiration die, a "
                    "d6.",
            "Level": 1,
        },
        {
            "Name": "Song of Rest",
            "Text": "you can use soothing music or oration to help revitalize "
                    "your wounded allies during a short rest. If you or any "
                    "friendly creatures who can hear your performance regain "
                    "hit points at the end of the short rest, each of those "
                    "creatures regains an extra 1d8 hit points.",
            "Level": 2,
        },
        {
            "Name": "Bardic Inspiration",
            "Text": "Use a bonus action on your turn to choose one creature "
                    "other than yourself within 60 feet of you who can hear "
                    "you. That creature gains one Bardic Inspiration die, a "
                    "d8.",
            "Level": 5,
        },
        {
            "Name": "Bardic Inspiration",
            "Text": "Use a bonus action on your turn to choose one creature "
                    "other than yourself within 60 feet of you who can hear "
                    "you. That creature gains one Bardic Inspiration die, a "
                    "d10.",
            "Level": 10,
        },
    ]
}

CLERIC = {
    "Name": "Cleric",
    "Primary": "Wisdom",
    "Secondary": "Charisma",
    "Armor Proficiencies": ["Light", "Medium", "Shields"],
    "Weapon Proficiencies": ["Simple"],
    "Tool Proficiencies": [],
    "Saves": ["Wisdom", "Charisma"],
    "Hit Dice": 8,
    "Skill List": ["History", "Insight", "Medicine", "Persuasion", "Religon"],
    "Skill Picks": 2,
    "Caster": True,
    "Casting Stat": "Wisdom",
    "Powers": [
        {
            "Name": "Channel Divinity",
            "Text": "You gain the ability to channel divine energy directly"
                    "from your deity, using that energy to fuel magical "
                    "effects. You start with two such effects: Turn Undead and"
                    " an effect determined by your domain. When you use your "
                    "Channel Divinity, you choose which effect to create. You "
                    "must then finish a short or long rest to use your "
                    "Channel Divinity again.",
            "Level": 2,
        },
        {
            "Name": "Channel Divinity: Turn Undead",
            "Text": "As an action, you present your holy symbol and speak a "
                    "prayer censuring the undead. Each undead that can see or "
                    "hear you within 30 feet of you must make a Wisdom saving "
                    "throw. If the creature fails its saving throw, it is "
                    "turned for 1 minute or until it takes any damage. A "
                    "turned creature must spend its turns trying to move as "
                    "far away from you as it can, and it can’t willingly move "
                    "to a space within 30 feet of you. It also can’t take "
                    "reactions. For its action, it can use only the Dash "
                    "action or try to escape from an effect that prevents it "
                    "from moving. If there’s nowhere to move, the creature "
                    "can use the Dodge action.",
            "Level": 2,
        },
    ],
}

CLASSES = {
    "Barbarian": BARBARIAN,
    "Bard": BARD,
    "Cleric": CLERIC,
    }
