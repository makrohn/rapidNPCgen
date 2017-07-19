"""Main module to generate D&D5e NPCs rapidly with minimal input"""

import math
import random

import classes
import races
import weapons

ABILITIES = [
    "Strength", "Dexterity", "Constitution",
    "Intelligence", "Wisdom", "Charisma"
    ]

STR_SKILLS = ["Athletics"]
DEX_SKILLS = ["Acrobatics", "Sleight of Hand", "Stealth"]
INT_SKILLS = ["Arcana", "History", "Investigation", "Nature", "Religion"]
WIS_SKILLS = [
    "Animal Handling", "Insight", "Medicine", "Perception", "Survival"
    ]
CHA_SKILLS = ["Deception", "Intimidation", "Performance", "Persuasion"]
ALL_SKILLS = STR_SKILLS + DEX_SKILLS + INT_SKILLS + WIS_SKILLS + CHA_SKILLS
ALL_SKILLS = sorted(ALL_SKILLS)


class NPC(object):
    """Object to define the stat block of the NPC itself"""
    def __init__(self, npcname, classname, race, subrace=""):
        self.name = npcname
        self.level = 1
        self.bonus = 2
        self.char_class(classname)
        self.char_race(race)
        if subrace != "":
            self.race_stats.subrace(subrace)
        self.assign_ability_scores()
        self.calculate_proficiencies()
        self.calc_skills()

    def char_class(self, classname):
        """Load stats for the class"""
        self.charclass = getattr(classes, classname)
        self.class_stats = self.charclass()
        self.class_name = classname

    def char_race(self, race):
        """Load stats for the race"""
        self.race = getattr(races, race)
        self.race_stats = self.race()
        self.race_name = race

    def assign_ability_scores(self):
        """Assign ability scores according to standard matrix"""
        self.ability_scores = {}
        scores_left = [15, 14, 13, 12, 10, 8]
        abilities_left = ABILITIES
        self.ability_scores[self.class_stats.primary] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.class_stats.primary)
        self.ability_scores[self.class_stats.secondary] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.class_stats.secondary)
        while len(abilities_left) > 0:
            next_ability = random.choice(abilities_left)
            self.ability_scores[next_ability] = scores_left[0]
            del scores_left[0]
            abilities_left.remove(next_ability)
        for ability in self.race_stats.abilities:
            self.ability_scores[ability] += self.race_stats.abilities[ability]
        self.ability_bonuses = {}
        for score in self.ability_scores:
            self.ability_bonuses[score] = math.floor(
                (self.ability_scores[score] - 10)/2
                )

    def calculate_proficiencies(self):
        """Combine racial and class proficiencies"""
        try:
            self.race_stats.weapon_proficiencies
        except:
            self.race_stats.weapon_proficiencies = []
        self.weapon_proficiencies = (
            self.race_stats.weapon_proficiencies +
            self.class_stats.weapon_proficiencies
            )

        try:
            self.race_stats.armor_proficiencies
        except:
            self.race_stats.armor_proficiencies = []
        self.armor_proficiencies = (
            self.race_stats.armor_proficiencies +
            self.class_stats.armor_proficiencies)

        try:
            self.class_stats.tool_proficiencies
        except:
            self.class_stats.tool_proficiencies = []
        self.tool_proficiencies = (
            self.race_stats.tool_proficiencies +
            self.class_stats.tool_proficiencies)

        try:
            self.race_stats.skills
        except:
            self.race_stats.skills = []
        self.skill_proficiencies = (
            self.race_stats.skills + self.class_stats.skills
            )

    def calc_skills(self):
        """Assign values to skill bonuses"""
        skills = {}
        for skill in STR_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Strength'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Strength']

        for skill in DEX_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Dexterity'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Dexterity']

        for skill in INT_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = (
                    self.ability_bonuses['Intelligence'] + self.bonus
                    )
            else:
                skills[skill] = self.ability_bonuses['Intelligence']

        for skill in WIS_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Wisdom'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Wisdom']

        for skill in CHA_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Charisma'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Charisma']
        self.skills = skills


def create_character():
    """Interactively request all the necessary fields to create an NPC"""
    name = input("Name? ")
    class_choice = input("Class? ")
    race_choice = input("Race? ")
    if npc.race_stats.has_subrace:
        subrace_choice = input("Choose 'Hill' or 'Mountain' subrace: ")
        npc.race_stats.subrace(subrace_choice)
    npc = NPC(name, class_choise, race_choice)
    npc.assign_ability_scores()
    return npc


def print_character(npc):
    """Print the npc"""
    print(npc.name)
    print(npc.race.__name__)
    print(npc.charclass.__name__)
    for ability in [
            "Strength", "Dexterity", "Constitution",
            "Intelligence", "Wisdom", "Charisma"
        ]:
        print(ability + ": " + str(npc.ability_scores[ability]))
    print("Size: " + npc.race_stats.size)
    print("Speed: " + str(npc.race_stats.speed))
    print("Darkvision: " + str(npc.race_stats.darkvision))
    print("Proficiencies")
    print(npc.weapon_proficiencies)
    print(npc.armor_proficiencies)
    print(npc.tool_proficiencies)
    print(npc.skill_proficiencies)
    for skill in ALL_SKILLS:
        print(skill + ": " + str(npc.skills[skill]))
