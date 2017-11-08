"""Choose random weapons that an NPC is proficient in"""

import random

SIMPLE_MELEE = [
    {"Club": {"Damage": "1d4", "Type": "bludgeoning", "Notes": "Light",
              "Average": 2.5}},
    {"Dagger": {"Damage": "1d4", "Type": "piercing", "Average": 2.5,
                "Notes": "Finesse, light, thrown (range 20/60)"}},
    {"Greatclub": {"Damage": "1d8", "Type": "bludgeoning",
                   "Average": 4.5, "Notes": "Two-handed"}},
    {"Handaxe": {"Damage": "1d6", "Type": "slashing", "Average": 3.5,
                 "Notes": "Light, thrown (range 20/60)"}},
    {"Javelin": {"Damage": "1d6", "Type": "piercing", "Average": 3.5,
                 "Notes": "Thrown (range 30/120)"}},
    {"Light Hammer": {"Damage": "1d4", "Type": "bludgeoning", "Average": 2.5,
                      "Notes": "Light, thrown (range 20/60)"}},
    {"Mace": {"Damage": "1d6", "Type": "bludgeoning", "Notes": "",
              "Average": 3.5,}},
    {"Quarterstaff": {"Damage": "1d6", "Type": "bludgeoning", "Average": 3.5,
                      "Notes": "Versatile (1d8)"}},
    {"Sickle": {"Damage": "1d4", "Type": "slashing", "Notes": "Light",
                "Average": 2.5,}},
    {"Spear": {"Damage": "1d6", "Type": "piercing", "Average": 3.5,
               "Notes": "Thrown (range 20/60), versatile (1d8)"}},
]
SIMPLE_RANGED = [
    {"Crossbow, light": {"Damage": "1d8", "Type": "piercing", "Average": 4.5,
                         "Notes":
                         "Ammunition (range 80/320), loading, two-handed"}},
    {"Dart": {"Damage": "1d4", "Type": "piercing", "Average": 2.5,
              "Notes": "Finesse, thrown (range 20/60)"}},
    {"Shortbow": {"Damage": "1d6", "Type": "piercing", "Average": 3.5,
                  "Notes": "Ammunition (range 80/320), two-handed"}},
    {"Sling": {"Damage": "1d4", "Type": "bludgeoning", "Average": 2.5,
               "Notes": "(range 30/120)"}},
]
MARTIAL_MELEE = [
    {"Battleaxe": {"Damage": "1d8", "Type": "slashing", "Average": 4.5,
                   "Notes": "Versatile (1d10)"}},
    {"Flail": {"Damage": "1d8", "Type": "bludgeoning", "Notes": "",
               "Average": 4.5,}},
    {"Glaive": {"Damage": "1d10", "Type": "slashing", "Average": 5.5,
                "Notes": "Heavy, reach, two-handed"}},
    {"Greataxe": {"Damage": "1d12", "Type": "slashing", "Average": 6.5,
                  "Notes": "Heavy, two-handed"}},
    {"Greatsword": {"Damage": "2d6", "Type": "slashing", "Average": 7,
                    "Notes": "Heavy, two-handed"}},
    {"Halberd": {"Damage": "1d10", "Type": "slashing", "Average": 5.5,
                 "Notes": "Heavy, reach, two-handed"}},
    {"Lance": {"Damage": "1d12", "Type": "piercing", "Average": 6.5,
               "Notes": "Reach, special"}},
    {"Longsword": {"Damage": "1d8", "Type": "slashing", "Average": 4.5,
                   "Notes": "Versatile (1d10)"}},
    {"Maul": {"Damage": "2d6", "Type": "bludgeoning", "Average": 7,
              "Notes": "Heavy, two-handed"}},
    {"Morningstar": {"Damage": "1d8", "Type": "piercing", "Notes": "",
                     "Average": 4.5,}},
    {"Pike": {"Damage": "1d10", "Type": "piercing", "Average": 5.5,
              "Notes": "Heavy, reach, two-handed"}},
    {"Rapier": {"Damage": "1d8", "Type": "piercing", "Notes": "Finesse",
                "Average": 4.5}},
    {"Scimitar": {"Damage": "1d6", "Type": "slashing", "Average": 3.5,
                  "Notes": "Finesse, light"}},
    {"Shortsword": {"Damage": "1d6", "Type": "piercing", "Average": 3.5,
                    "Notes": "Finesse, light"}},
    {"Trident": {"Damage": "1d6", "Type": "piercing", "Average": 3.5,
                 "Notes": "Thrown (range 20/60), versatile (1d8)"}},
    {"War Pick": {"Damage": "1d8", "Type": "piercing", "Notes": "",
                  "Average": 4.5,}},
    {"Warhammer": {"Damage": "1d8", "Type": "bludgeoning", "Average": 4.5,
                   "Notes": "Versatile (1d10)"}},
    {"Whip": {"Damage": "1d4", "Type": "slashing", "Average": 2.5,
              "Notes": "Finesse, reach"}},
]
MARTIAL_RANGED = [
    {"Blowgun": {"Damage": "1", "Type": "piercing", "Average": 1,
                 "Notes": "Ammunition (range 25/100), loading"}},
    {"Crossbow, hand": {"Damage": "1d6", "Type": "piercing", "Average": 3.5,
                        "Notes":
                        "Ammunition (range 30/120), light, loading"}},
    {"Crossbow, heavy": {"Damage": "1d10", "Type": "piercing", "Average": 5.5,
                         "Notes":
                         "Ammunition (range 100/400), heavy, loading,"}},
    # Longbow avg is 9 to make it preferable for classes with extra attack
    {"Longbow": {"Damage": "1d8", "Type": "piercing", "Average": 9,
                 "Notes": "Ammunition (range 150/600), heavy, two-handed"}},
    {"Net": {"Damage": "—", "Type": "-", "Average": 0,
             "Notes": "Special, thrown (range 5/15) "}},
]
RANGED_WEAPONS = SIMPLE_RANGED + MARTIAL_RANGED
MELEE_WEAPONS = SIMPLE_MELEE + MARTIAL_MELEE


def choose_melee(proficiencies, strength, dexterity):
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
        return "No melee weapon"
    best_damage = 0
    for choice in choices:
        for item in choice:
            damage = choice[item]["Average"]
            notes = choice[item]["Notes"].lower()
            if int(dexterity) > int(strength):
                if "finesse" in notes:
                    damage += int(dexterity)
                else:
                    damage += int(strength)
            else:
                damage += int(strength)
            if damage > best_damage:
                best_damage = damage
                best_choice = choice
            elif damage == best_damage:
                if "versatile" in notes:
                    best_choice = choice
    return best_choice


def choose_ranged(proficiencies, strength, dexterity):
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
        return "No ranged weapon"
    best_damage = 0
    for choice in choices:
        for item in choice:
            damage = choice[item]["Average"]
            notes = choice[item]["Notes"].lower()
            if int(strength) > int(dexterity):
                if "thrown" in notes:
                    damage += int(strength)
                else:
                    damage += int(dexterity)
            else:
                damage += int(dexterity)
            if damage > best_damage:
                best_damage = damage
                best_choice = choice
    return best_choice
