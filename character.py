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
        self.melee = weapons.choose_melee(self.weapon_proficiencies)

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


def create_character():
    """Interactively request all the necessary fields to create an NPC"""
    name = input("Name? ")
    good_class = False
    class_choices = list(range(1, len(classes.CLASSES)+1))
    class_choices = [str(x) for x in class_choices]
    while good_class is False:
        print("Choose a class: ")
        for item in classes.CLASSES:
            print(item + ": " + classes.CLASSES[item])
        class_choice = input("Enter the number for your choice: ")
        if class_choice in class_choices:
            class_choice = classes.CLASSES[class_choice]
            good_class = True
        else:
            print("Not a valid class choice")
    good_race = False
    race_choices = list(range(1, len(races.RACES)+1))
    race_choices = [str(x) for x in race_choices]
    while good_race is False:
        print("Choose a race: ")
        for item in races.RACES:
            print(item + ": " + races.RACES[item])
        race_choice = input("Enter the number for your choice: ")
        if race_choice in race_choices:
            race_choice = races.RACES[race_choice]
            good_race = True
        else:
            print("Not a valid race choice")
    race = getattr(races, race_choice)
    race_subrace = race()
    if race_subrace.has_subrace is True:
        good_subrace = False
        subrace_choices = list(range(0, len(race_subrace.subrace_choices)))
        while good_subrace is False:
            print("Choose a subrace: ")
            for item in race_subrace.subrace_choices:
                print(
                    str(race_subrace.subrace_choices.index(item)+1) +
                    ": " + item
                    )
            subrace_choice = int(
                input("Enter the number for your choice: ")
                ) - 1
            if subrace_choice in subrace_choices:
                subrace_choice = race_subrace.subrace_choices[subrace_choice]
                npc = NPC(name, class_choice, race_choice, subrace_choice)
                good_subrace = True
            else:
                print("Not a valid subrace choice")
    else:
        npc = NPC(name, class_choice, race_choice)
    print_character(npc)

if __name__ == "__main__":
    create_character()
