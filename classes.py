"""Module to hold 5e Class definitions"""

import random
import math

CLASSES = ["Barbarian", "Bard"]


class Barbarian(object):
    """Barbarian Class definition"""
    def __init__(self):
        self.primary = "Strength"
        self.secondary = "Constitution"
        self.armor_proficiencies = ["Light", "Medium", "Shields"]
        self.weapon_proficiencies = ["Simple", "Martial"]
        self.tool_proficiencies = []
        self.saves = ["Strength", "Constitution"]
        self.hit_dice = 12
        self.caster = False

    def get_skills(self):
        """Figure out what skills a Barbarian has"""
        skills_list = [
            "Animal Handling",
            "Athletics",
            "Intimidation",
            "Nature",
            "Perception",
            "Survival"
            ]
        first_skill = random.choice(skills_list)
        skills_list.remove(first_skill)
        second_skill = random.choice(skills_list)
        skills = [first_skill, second_skill]
        return skills

    def find_powers(self, level):
        """Figure out what powers they have for their level"""
        powers = [
            {
                "Name": "Rage",
                "Text": "On your turn, you can enter a rage as a bonus "
                        "action.",
                "Level": 1,
            },
            {
                "Name": "Unarmored Defense",
                "Text": "While you are not wearing any armor, your Armor "
                        "Class equals 10 + your Dexterity modifier + your "
                        "Constitution modifier.",
                "Level": 1,
            },
            {
                "Name": "Reckless Attack",
                "Text": "You can throw aside all concern for defense to attack"
                        " with fierce desperation. When you make your first "
                        "attack on your turn, you can decide to attack "
                        "recklessly. Doing so gives you advantage on melee "
                        "weapon attack rolls using Strength during this turn, "
                        "but attack rolls against you have advantage until "
                        "your next turn.",
                "Level": 2,
            },
            {
                "Name": "Danger Sense",
                "Text": "You gain an uncanny sense of when things nearby "
                        "aren’t as they should be, giving you an edge when you"
                        " dodge away from danger. You have advantage on "
                        "Dexterity saving throws against effects that you can "
                        "see, such as traps and spells. To gain this benefit, "
                        "you can’t be blinded, deafened, or incapacitated.",
                "Level": 2
            },
            ]
        acquired = []
        for power in powers:
            if power["Level"] <= level:
                acquired.append(power)
        return acquired


class Bard(object):
    """Bard Class definition"""
    def __init__(self):
        self.primary = "Charisma"
        self.secondary = "Dexterity"
        self.armor_proficiencies = ["Light"]
        self.weapon_proficiencies = [
            "Simple", "Crossbow, hand", "Longsword", "Rapier", "Shortsword"
            ]
        self.tool_proficiencies = self.get_instruments()
        self.saves = ["Dexterity", "Charisma"]
        self.hit_dice = 8
        self.caster = True

    def get_instruments(self):
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

    def get_skills(self):
        """Figure out what skills a Bard has"""
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
        skills_list.remove(second_skill)
        third_skill = random.choice(skills_list)
        skills = [first_skill, second_skill, third_skill]
        return skills

    def find_powers(self, level):
        """Figure out what powers they have for their level"""
        inspiration_die = 6
        extra_size = math.floor(level/5)*2
        inspiration_die += extra_size
        inspiration_die = str(inspiration_die)
        rest_die = 6
        if level > 5:
            extra_rest = math.floor((level-5)/4)*2
            rest_die += extra_rest
        rest_die = str(rest_die)
        powers = [
            {
                "Name": "Bardic Inspiration",
                "Text": "Use a bonus action on your turn to choose one "
                        "creature other than yourself within 60 feet of you "
                        "who can hear you. That creature gains one Bardic "
                        "Inspiration die, a d%s." % inspiration_die,
                "Level": 1,
            },
            {
                "Name": "Song of Rest",
                "Text": "you can use soothing music or oration to help "
                        "revitalize your wounded allies during a short rest. "
                        "If you or any friendly creatures who can hear your "
                        "performance regain hit points at the end of the "
                        "short rest, each of those creatures regains an extra "
                        "1d%s hit points." % rest_die,
                "Level": 2,
            },
            ]
        acquired = []
        for power in powers:
            if power["Level"] <= level:
                acquired.append(power)
        return acquired
