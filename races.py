"""Module to hold 5e Race definitions"""

import random

RACES = [
    "Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "HalfElf",
    "HalfOrc", "Tiefling"
    ]


class Dwarf(object):
    """Dwarf Class definition"""
    def __init__(self):
        self.abilities = {"Constitution": 2}
        self.size = "Medium"
        self.speed = 25
        self.darkvision = 60
        self.weapon_proficiencies = [
            "Battleaxe",
            "Handaxe",
            "Throwing Hammer",
            "Warhammer",
            ]
        self.tool_proficiencies = [random.choice([
            "Smith's Tools",
            "Brewer's Tools",
            "Mason's Tools",
            ])]
        self.languages = ["Dwarvish", "Common"]
        self.armor_proficiencies = []
        self.powers = [
            {
                "Name": "Dwarven Resilience",
                "Text": "You have advantage on saving throws against poison, "
                        "and you have resistance against poison damage"
            },
            {
                "Name": "Stonecunning",
                "Text": "Whenever you make an Intelligence (History) check "
                        "related to the origin of stonework, you are "
                        "considered proficient in the History skill and add "
                        "double your proficiency bonus to the check, instead "
                        "of your normal proficiency bonus."
            }
            ]
        self.has_subrace = True
        self.subrace_choices = ["Hill", "Mountain"]

    def subrace(self, subrace_choice):
        """Add subrace attributes"""
        if "Hill" in subrace_choice:
            self.abilities["Wisdom"] = 1
        elif "Mountain" in subrace_choice:
            self.abilities["Strength"] = 2
            self.armor_proficiencies = ["Light", "Medium"]
        else:
            return "Invalid subrace choice"


class Elf(object):
    """Elf Class definition"""
    def __init__(self):
        self.abilities = {"Dexterity": 2}
        self.size = "Medium"
        self.speed = 30
        self.darkvision = 60
        self.skills = ["Perception"]
        self.languages = ["Elvish", "Common"]
        self.tool_proficiencies = []
        self.weapon_proficiencies = []
        self.powers = [
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
            ]
        self.has_subrace = True
        self.subrace_choices = ["High Elf", "Wood Elf", "Drow"]

    def subrace(self, subrace_choice):
        """Add subrace attributes"""
        if "High" in subrace_choice:
            self.abilities["Intelligence"] = 1
            self.weapon_proficiencies = ["Longsword", "Shortsword",
                                         "Shortbow", "Longbow"]
            self.powers.append({
                "Name": "Extra cantrip",
                "Text": "You know one extra cantrip of your choice from the "
                        "wizard spell list. Intelligence is your spellcasting "
                        "ability for it"
                })
            self.languages.append("One extra")
        elif "Wood" in subrace_choice:
            self.abilities["Wisdom"] = 1
            self.weapon_proficiencies = ["Longsword", "Shortsword",
                                         "Shortbow", "Longbow"]
            self.powers.append({
                "Name": "Mask of the Wild",
                "Text": "You can attempt to hide even when you are only "
                        "lightly obscured by foliage, heavy rain, falling "
                        "snow, mist, and other natural phenomena."
                })
        elif "Drow" in subrace_choice:
            self.abilities["Charisma"] = 1
            self.darkvision = 120
            self.powers.append({
                "Name": "Sunlight Sensitivity",
                "Text": "You have disadvantage on attack rolls and on Wisdom "
                        "(Perception) checks that rely on sight when you, "
                        "the target of your attack, or whatever you are "
                        "trying to perceive is in direct sunlight."
                })
            self.powers.append({
                "Name": "Drow Magic",
                "Text": "You know the dancing lights cantrip. When you reach "
                        "3rd level, you can cast the faerie fire spell once "
                        "per day. When you reach 5th level, you can also cast "
                        "the darkness spell once per day. Charisma is your "
                        "spellcasting ability for these spells."
                })
            self.weapon_proficiencies = ["Rapier", "Shortsword",
                                         "Crossbow, hand"]
        else:
            return "Invalid subrace choice"


class Halfling(object):
    """Halfling Class definition"""
    def __init__(self):
        self.abilities = {"Dexterity": 2}
        self.size = "Small"
        self.speed = 25
        self.darkvision = 0
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.languages = ["Halfling", "Common"]
        self.powers = [
            {
                "Name": "Lucky",
                "Text": "When you roll a 1 on an attack roll, ability check, "
                        "or saving throw, you can reroll the die and must "
                        "use the new roll."
            },
            {
                "Name": "Brave",
                "Text": "You have advantage on saving throws against being "
                        "frightened."
            },
            {
                "Name": "Halfling Nimbleness",
                "Text": "You can move through the space of any creature that "
                        "is of a size larger than yours."
            },
            ]
        self.has_subrace = True
        self.subrace_choices = ["Lightfoot", "Stout"]

    def subrace(self, subrace_choice):
        """Add subrace attributes"""
        if "Lightfoot" in subrace_choice:
            self.abilities["Charisma"] = 1
            self.powers.append({
                "Name": "Naturally Stealthy",
                "Text": "You can attempt to hide even when you are obscured "
                        "only by a creature that is at least one size larger "
                        "than you."
                })
        elif "Stout" in subrace_choice:
            self.abilities["Constitution"] = 1
            self.powers.append({
                "Name": "Stout Resilience",
                "Text": "You have advantage on saving throws against poison, "
                        "and you have resistance against poison damage"
                })
        else:
            return "Invalid subrace choice"


class Human(object):
    """Human Class definition"""
    def __init__(self):
        self.abilities = {
            "Strength": 1, "Dexterity": 1, "Constitution": 1,
            "Intelligence": 1, "Wisdom": 1, "Charisma": 1
            }
        self.size = "Medium"
        self.speed = 30
        self.darkvision = 0
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.languages = ["One more", "Common"]
        self.powers = []
        self.has_subrace = False


class Dragonborn(object):
    """Dragonborn Class definition"""
    def __init__(self):
        self.abilities = {"Strength": 2, "Charisma": 1}
        self.size = "Medium"
        self.speed = 30
        self.darkvision = 0
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.languages = ["Draconic", "Common"]
        self.powers = [
            {
                "Name": "Draconic Ancestry",
                "Text": "You have draconic ancestry. Choose one type of "
                        "dragon from the Draconic Ancestry table."
            },
            {
                "Name": "Breath Weapon",
                "Text": "You can use your action to exhale destructive energy."
                        " Your draconic ancestry determines the size, shape, "
                        "and damage type of the exhalation. When you use your "
                        "breath weapon, each creature in the area of the "
                        "exhalation must make a saving throw, the type of "
                        "which is determined by your draconic ancestry. The "
                        "DC for this saving throw equals 8 + your Constitution"
                        " modifier + your proficiency bonus. A creature takes "
                        "2d6 damage on a failed save, and half as much damage "
                        "on a successful one. The damage increases to 3d6 at "
                        "6th level, 4d6 at 11th level, and 5d6 at 16th level."

            },
            {
                "Name": "Damage Resistance",
                "Text": "You have resistance to the damage type associated "
                        "with your draconic ancestry."
            },
            ]
        self.has_subrace = False


class Gnome(object):
    """Gnome Class definition"""
    def __init__(self):
        self.abilities = {"Intelligence": 2}
        self.size = "Small"
        self.speed = 25
        self.darkvision = 60
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.languages = ["Gnomish", "Common"]
        self.powers = [
            {
                "Name": "Gnome Cunning",
                "Text": "You have advantage on all Intelligence, Wisdom, and "
                        "Charisma saving throws against magic."
            },
            {
                "Name": "Stonecunning",
                "Text": "Whenever you make an Intelligence (History) check "
                        "related to the origin of stonework, you are "
                        "considered proficient in the History skill and add "
                        "double your proficiency bonus to the check, instead "
                        "of your normal proficiency bonus."
            }
            ]
        self.has_subrace = True
        self.subrace_choices = ["Forest", "Rock"]

    def subrace(self, subrace_choice):
        """Add subrace attributes"""
        if "Forest" in subrace_choice:
            self.abilities["Dexterity"] = 1
            self.powers.append({
                "Name": "Natural Illusionist",
                "Text": "You know the minor illusion cantrip. Intelligence is "
                        "your spellcasting ability for it."
                })
            self.powers.append({
                "Name": "Speak with Small Beasts",
                "Text": "Through sounds and gestures, you can communicate "
                        "simple ideas with Small or smaller beasts. Forest "
                        "gnomes love animals and often keep squirrels, "
                        "badgers, rabbits, moles, woodpeckers, and other "
                        "creatures as beloved pets."
                })
        elif "Rock" in subrace_choice:
            self.abilities["Constitution"] = 1
            self.powers.append({
                "Name": "Artificer's Lore",
                "Text": "Whenever you make an Intelligence (History) check "
                        "related to magic items, alchemical objects, or "
                        "technological devices, you can add twice your "
                        "proficiency bonus, instead of any proficiency bonus "
                        "you normally apply."
                })
            self.powers.append({
                "Name": "Tinker",
                "Text": "You have proficiency with artisan’s tools (tinker’s "
                        "tools). Using those tools, you can spend 1 hour and "
                        "10 gp worth of materials to construct a Tiny "
                        "clockwork device (AC 5, 1 hp)."
                })
        else:
            return "Invalid subrace choice"


class HalfElf(object):
    """Half-Elf Class definition"""
    def __init__(self):
        self.abilities = {"Charisma": 2}
        self.two_random_abilities()
        self.size = "Medium"
        self.speed = 30
        self.darkvision = 60
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.languages = ["Elvish", "Common", "One more"]
        self.powers = [
            {
                "Name": "Fey Ancestry",
                "Text": "You have advantage on saving throws against being "
                        "charmed, and magic can’t put you to sleep."
            },
            {
                "Name": "Skill Versatility",
                "Text": "You gain proficiency in two skills of your choice."
            }
            ]
        self.has_subrace = False
        self.skills = self.get_skills()

    def two_random_abilities(self):
        """Pick two ability bonuses for the Half-Elf"""
        options = ["Strength", "Dexterity", "Intelligence", "Constitution",
                   "Wisdom"]
        stat_one = random.choice(options)
        options.remove(stat_one)
        stat_two = random.choice(options)
        self.abilities[stat_one] = 1
        self.abilities[stat_two] = 1

    def get_skills(self):
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


class HalfOrc(object):
    """Half-Orc Class definition"""
    def __init__(self):
        self.abilities = {"Strength": 2, "Constitution": 1}
        self.size = "Medium"
        self.speed = 30
        self.darkvision = 60
        self.skills = ["Intimidation"]
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.languages = ["Orc", "Common"]
        self.powers = [
            {
                "Name": "Relentless Endurance",
                "Text": "When you are reduced to 0 hit points but not killed "
                        "outright, you can drop to 1 hit point instead. You "
                        "can’t use this feature again until you finish a "
                        "long rest."
            },
            {
                "Name": "Savage Attacks",
                "Text": "When you score a critical hit with a melee weapon "
                        "attack, you can roll one of the weapon’s damage dice "
                        "one additional time and add it to the extra damage "
                        "of the critical hit."
            }
            ]
        self.has_subrace = False


class Tiefling(object):
    """Tiefling Class definition"""
    def __init__(self):
        self.abilities = {"Charisma": 2, "Intelligence": 1}
        self.size = "Medium"
        self.speed = 30
        self.darkvision = 60
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.languages = ["Infernal", "Common"]
        self.powers = [
            {
                "Name": "Hellish Resistance",
                "Text": "You have resistance to fire damage."
            },
            {
                "Name": "Infernal Legacy",
                "Text": "You know the thaumaturgy cantrip. Once you reach 3rd "
                        "level, you can cast the hellish rebuke spell once "
                        "per day as a 2nd-level spell. Once you reach 5th "
                        "level, you can also cast the darkness spell once per "
                        "day. Charisma is your spellcasting ability for these "
                        "spells."
            }
            ]
        self.has_subrace = False
