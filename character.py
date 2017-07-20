"""Main module to generate D&D5e NPCs rapidly with minimal input"""

import math
import random

import classes
import races
import weapons
import spells
import armor

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

def load_race(racename, subrace=""):
    if subrace != "":
        races.get_subrace(racename, subrace)
    race = races.RACE_DEFINITIONS[racename]
    return race

class NPC(object):
    """Object to define the stat block of the NPC itself"""
    def __init__(self, npcname, classname, race, level, subrace=""):
        self.name = npcname
        self.level = level
        self.bonus = self.get_proficiency_bonus()
        self.char_class(classname)
        self.race = load_race(race, subrace)
        self.subrace = subrace
        self.ability_scores = self.assign_ability_scores(level)
        self.calculate_proficiencies()
        self.calc_skills()
        self.melee = weapons.choose_melee(self.weapon_proficiencies)
        self.ranged = weapons.choose_ranged(self.weapon_proficiencies)
        self.powers = (
            self.race["Powers"] + self.class_stats.find_powers(self.level)
            )
        self.hitpoints = self.get_hp(
            self.level, self.ability_bonuses['Constitution']
            )
        if self.class_stats.caster:
            self.spell_list = spells.spells_known(self.level, classname)
        self.armor = armor.choose_armor(
            self.armor_proficiencies, self.level,
            self.ability_scores['Strength']
            )
        self.armor_class = self.calc_ac()

    def get_proficiency_bonus(self):
        """Get proficiency bonus based on level"""
        bonus = 2
        extra_bonus = math.floor((self.level-1)/4)
        bonus += extra_bonus
        return bonus

    def get_hp(self, level, con_bonus):
        """Figure out character's HP"""
        hitpoints = self.class_stats.hit_dice
        hitpoints += con_bonus * level
        if self.subrace == "Hill":
            hitpoints += level
        level = level-1
        hitpoints += level * 7
        return hitpoints

    def char_class(self, classname):
        """Load stats for the class"""
        self.charclass = getattr(classes, classname)
        self.class_stats = self.charclass()
        self.class_name = classname

    def assign_ability_scores(self, level):
        """Assign ability scores according to standard matrix"""
        ability_scores = {}
        scores_left = [15, 14, 13, 12, 10, 8]
        abilities_left = ABILITIES
        ability_scores[self.class_stats.primary] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.class_stats.primary)
        ability_scores[self.class_stats.secondary] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.class_stats.secondary)
        while len(abilities_left) > 0:
            next_ability = random.choice(abilities_left)
            ability_scores[next_ability] = scores_left[0]
            del scores_left[0]
            abilities_left.remove(next_ability)
        for ability in self.race["Abilities"]:
            ability_scores[ability] += self.race["Abilities"][ability]
        ability_ups = math.floor(level/4)
        ability_ups = ability_ups*2
        while ability_ups > 0:
            if ability_scores[self.class_stats.primary] < 20:
                ability_scores[self.class_stats.primary] += 1
                ability_ups -= 1
            elif ability_scores[self.class_stats.secondary] < 20:
                ability_scores[self.class_stats.secondary] += 1
                ability_ups -= 1
            else:
                abilities = [ability for ability in self.ability_scores]
                stat_up = random.choice(abilities)
                if ability_scores[stat_up] < 20:
                    ability_scores[stat_up] += 1
                    ability_ups -= 1
        self.ability_bonuses = {}
        for score in ability_scores:
            self.ability_bonuses[score] = math.floor(
                (ability_scores[score] - 10)/2
                )
        return ability_scores

    def calculate_proficiencies(self):
        """Combine racial and class proficiencies"""
        try:
            self.race["Weapon Proficiencies"]
        except:
            self.race["Weapon Proficiencies"] = []
        self.weapon_proficiencies = (
            self.race["Weapon Proficiencies"] +
            self.class_stats.weapon_proficiencies
            )

        try:
            self.race["Armor Proficiencies"]
        except:
            self.race["Armor Proficiencies"] = []
        self.armor_proficiencies = (
            self.race["Armor Proficiencies"] +
            self.class_stats.armor_proficiencies)

        try:
            self.class_stats.tool_proficiencies
        except:
            self.class_stats.tool_proficiencies = []
        self.tool_proficiencies = (
            self.race["Tool Proficiencies"] +
            self.class_stats.tool_proficiencies)

        try:
            self.race["Skills"]
        except:
            self.race["Skills"] = []
        self.skill_proficiencies = (
            self.race["Skills"] + self.class_stats.get_skills()
            )

    def calc_skills(self):
        """Assign values to skill bonuses"""
        skills = {}

        joat_bonus = 0
        if self.charclass.__name__ == "Bard" and self.level >= 2:
            joat_bonus = math.floor(self.bonus/2)

        for skill in STR_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Strength'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Strength'] + joat_bonus

        for skill in DEX_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Dexterity'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Dexterity'] + joat_bonus

        for skill in INT_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = (
                    self.ability_bonuses['Intelligence'] + self.bonus
                    )
            else:
                skills[skill] = (
                    self.ability_bonuses['Intelligence'] + joat_bonus
                    )

        for skill in WIS_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Wisdom'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Wisdom'] + joat_bonus

        for skill in CHA_SKILLS:
            if skill in self.skill_proficiencies:
                skills[skill] = self.ability_bonuses['Charisma'] + self.bonus
            else:
                skills[skill] = self.ability_bonuses['Charisma'] + joat_bonus
        self.skills = skills

        saves = {}
        for save in self.class_stats.saves:
            saves[save] = self.ability_bonuses[save] + self.bonus
        self.saves = saves

    def calc_ac(self):
        """Figure out a character's AC"""
        if self.charclass.__name__ == "Barbarian":
            armor_class = (
                10 + self.ability_bonuses['Dexterity'] +
                self.ability_bonuses['Constitution']
                )
            del self.armor[0]
        elif self.charclass.__name__ == "Monk":
            armor_class = (
                10 + self.ability_bonuses['Dexterity'] +
                self.ability_bonuses['Wisdom']
                )
            del self.armor[0]
        else:
            armor_class = self.armor[0]["AC"]
            if self.ability_bonuses['Dexterity'] > self.armor[0]["Dex_max"]:
                ac_bonus = self.armor[0]["Dex_max"]
            else:
                ac_bonus = self.ability_bonuses['Dexterity']
            armor_class += ac_bonus
        if len(self.armor) > 1:
            armor_class += 2
        return armor_class

    def calc_initiative(self):
        """Figure out a character's intiative"""
        initiative = self.ability_bonuses['Dexterity']
        if self.charclass.__name__ == "Bard" and self.level >= 2:
            initiative += math.floor(self.bonus/2)
        return initiative


def print_character(npc):
    """Print the npc"""
    print(npc.name)
    print(npc.race["Name"])
    print(npc.charclass.__name__)
    print("Level: " + str(npc.level))
    print("HP: " + str(npc.hitpoints))
    print("AC: " + str(npc.armor_class))
    print("Initiative: " + str(npc.calc_initiative()))
    for ability in [
            "Strength", "Dexterity", "Constitution",
            "Intelligence", "Wisdom", "Charisma"
        ]:
        print(
            ability + ": " + str(npc.ability_scores[ability]) + " (" +
            str(npc.ability_bonuses[ability]) + ")"
            )
    print("Saves: " + str(npc.saves))
    print("Size: " + npc.race["Size"])
    print("Speed: " + str(npc.race["Speed"]))
    print("Darkvision: " + str(npc.race["Darkvision"]))
    print("Proficiencies")
    print(npc.weapon_proficiencies)
    print(npc.armor_proficiencies)
    print(npc.tool_proficiencies)
    print(npc.skill_proficiencies)
    print(npc.race["Languages"])
    for skill in ALL_SKILLS:
        print(skill + ": " + str(npc.skills[skill]))
    print(npc.melee)
    print(npc.ranged)
    print(npc.armor)
    for power in npc.powers:
        print(power["Name"] + ": " + power["Text"])
    if npc.class_stats.caster:
        print(npc.spell_list)


def create_character():
    """Interactively request all the necessary fields to create an NPC"""
    name = input("Name? ")
    good_class = False
    class_choices = list(range(1, len(classes.CLASSES)+1))
    class_choices = [str(x) for x in class_choices]
    while good_class is False:
        print("Choose a class: ")
        for item in classes.CLASSES:
            print(str(classes.CLASSES.index(item) + 1) + ": " + item)
        class_choice = int(input("Enter the number for your choice: "))
        if class_choice in list(range(1, len(classes.CLASSES) + 1)):
            class_choice = classes.CLASSES[class_choice - 1]
            good_class = True
        else:
            print("Not a valid class choice")
    good_level = False
    while good_level is False:
        level = int(input("Level? "))
        if (0 < round(level) <= 20):
            level_choice = level
            good_level = True
        else:
            print("Please choose a level from 1 to 20")
    good_race = False
    race_choices = list(range(1, len(races.RACES)+1))
    race_choices = [str(x) for x in race_choices]
    while good_race is False:
        print("Choose a race: ")
        for item in races.RACES:
            print(str(races.RACES.index(item) + 1) + ": " + item)
        race_choice = int(input("Enter the number for your choice: "))
        if race_choice in list(range(1, len(races.RACES) + 1)):
            race_choice = races.RACES[race_choice - 1]
            good_race = True
        else:
            print("Not a valid race choice")
    race = races.RACE_DEFINITIONS[race_choice]
    if "Subraces" in race:
        good_subrace = False
        subrace_choices = list(range(0, len(race["Subraces"])))
        while good_subrace is False:
            print("Choose a subrace: ")
            for item in race["Subraces"]:
                print(
                    str(race["Subraces"].index(item)+1) +
                    ": " + item
                    )
            subrace_choice = int(
                input("Enter the number for your choice: ")
                ) - 1
            if subrace_choice in subrace_choices:
                subrace_choice = race["Subraces"][subrace_choice]
                npc = NPC(
                    name, class_choice, race_choice,
                    level_choice, subrace_choice
                    )
                good_subrace = True
            else:
                print("Not a valid subrace choice")
    else:
        npc = NPC(name, class_choice, race_choice, level_choice)
    print_character(npc)

if __name__ == "__main__":
    create_character()
