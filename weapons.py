"""Choose random weapons that an NPC is proficient in"""

import random

SIMPLE_MELEE = [
    {"Club": {"Damage": "1d4", "Type": "bludgeoning", "Notes": "Light"}},
    {"Dagger": {"Damage": "1d4", "Type": "piercing",
                "Notes": "Finesse, light, thrown (range 20/60)"}},
    {"Greatclub": {"Damage": "1d8", "Type": "bludgeoning",
                   "Notes": "Two-handed"}},
    {"Handaxe": {"Damage": "1d6", "Type": "slashing",
                 "Notes": "Light, thrown (range 20/60)"}},
    {"Javelin": {"Damage": "1d6", "Type": "piercing",
                 "Notes": "Thrown (range 30/120)"}},
    {"Light Hammer": {"Damage": "1d4", "Type": "bludgeoning",
                      "Notes": "Light, thrown (range 20/60)"}},
    {"Mace": {"Damage": "1d6", "Type": "bludgeoning", "Notes": ""}},
    {"Quarterstaff": {"Damage": "1d6", "Type": "bludgeoning",
                      "Notes": "Versatile (1d8)"}},
    {"Sickle": {"Damage": "1d4", "Type": "slashing", "Notes": "Light"}},
    {"Spear": {"Damage": "1d6", "Type": "piercing",
               "Notes": "Thrown (range 20/60), versatile (1d8)"}},
]
SIMPLE_RANGED = [
    {"Crossbow, light": {"Damage": "1d8", "Type": "piercing",
                         "Notes":
                         "Ammunition (range 80/320), loading, two-handed"}},
    {"Dart": {"Damage": "1d4", "Type": "piercing",
              "Notes": "Finesse, thrown (range 20/60)"}},
    {"Shortbow": {"Damage": "1d6", "Type": "piercing",
                  "Notes": "Ammunition (range 80/320), two-handed"}},
    {"Sling": {"Damage": "1d4", "Type": "bludgeoning",
               "Notes": "(range 30/120)"}},
]
MARTIAL_MELEE = [
    {"Battleaxe": {"Damage": "1d8", "Type": "slashing",
                   "Notes": "Versatile (1d10)"}},
    {"Flail": {"Damage": "1d8", "Type": "bludgeoning", "Notes": ""}},
    {"Glaive": {"Damage": "1d10", "Type": "slashing",
                "Notes": "Heavy, reach, two-handed"}},
    {"Greataxe": {"Damage": "1d12", "Type": "slashing",
                  "Notes": "Heavy, two-handed"}},
    {"Greatsword": {"Damage": "2d6", "Type": "slashing",
                    "Notes": "Heavy, two-handed"}},
    {"Halberd": {"Damage": "1d10", "Type": "slashing",
                 "Notes": "Heavy, reach, two-handed"}},
    {"Lance": {"Damage": "1d12", "Type": "piercing",
               "Notes": "Reach, special"}},
    {"Longsword": {"Damage": "1d8", "Type": "slashing",
                   "Notes": "Versatile (1d10)"}},
    {"Maul": {"Damage": "2d6", "Type": "bludgeoning",
              "Notes": "Heavy, two-handed"}},
    {"Morningstar": {"Damage": "1d8", "Type": "piercing", "Notes": ""}},
    {"Pike": {"Damage": "1d10", "Type": "piercing",
              "Notes": "Heavy, reach, two-handed"}},
    {"Rapier": {"Damage": "1d8", "Type": "piercing", "Notes": "Finesse"}},
    {"Scimitar": {"Damage": "1d6", "Type": "slashing",
                  "Notes": "Finesse, light"}},
    {"Shortsword": {"Damage": "1d6", "Type": "piercing",
                    "Notes": "Finesse, light"}},
    {"Trident": {"Damage": "1d6", "Type": "piercing",
                 "Notes": "Thrown (range 20/60), versatile (1d8)"}},
    {"War Pick": {"Damage": "1d8", "Type": "piercing", "Notes": ""}},
    {"Warhammer": {"Damage": "1d8", "Type": "bludgeoning",
                   "Notes": "Versatile (1d10)"}},
    {"Whip": {"Damage": "1d4", "Type": "slashing",
              "Notes": "Finesse, reach"}},
]
MARTIAL_RANGED = [
    {"Blowgun": {"Damage": "1", "Type": "piercing",
                 "Notes": "Ammunition (range 25/100), loading"}},
    {"Crossbow, hand": {"Damage": "1d6", "Type": "piercing",
                        "Notes":
                        "Ammunition (range 30/120), light, loading"}},
    {"Crossbow, heavy": {"Damage": "1d10", "Type": "piercing",
                         "Notes":
                         "Ammunition (range 100/400), heavy, loading,"}},
    {"Longbow": {"Damage": "1d8", "Type": "piercing",
                 "Notes": "Ammunition (range 150/600), heavy, two-handed"}},
    {"Net": {"Damage": "—", "Type": "-",
             "Notes": "Special, thrown (range 5/15) "}},
]
RANGED_WEAPONS = SIMPLE_RANGED + MARTIAL_RANGED
MELEE_WEAPONS = SIMPLE_MELEE + MARTIAL_MELEE


def choose_melee(proficiencies):
    """Choose a melee weapon"""
    choices = []
    pros_to_process = proficiencies
    if "Simple" in pros_to_process:
        choices += SIMPLE_MELEE
    if "Martial" in pros_to_process:
        choices += MARTIAL_MELEE
    for proficiency in pros_to_process:
        for item in MELEE_WEAPONS:
            if proficiency in item:
                choices.append(item)
    if choices == []:
        choices = "No melee weapon"
    return random.choice(choices)


def choose_ranged(proficiencies):
    """Choose a ranged weapon"""
    choices = []
    pros_to_process = proficiencies
    if "Simple" in pros_to_process:
        choices += SIMPLE_RANGED
    if "Martial" in pros_to_process:
        choices += MARTIAL_RANGED
    for proficiency in pros_to_process:
        for item in RANGED_WEAPONS:
            if proficiency in item:
                choices.append(item)
    if choices == []:
        choices = ["No ranged weapon"]
    return random.choice(choices)
