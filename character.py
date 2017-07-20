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
    """Load an NPC's race definition"""
    if subrace != "":
        races.get_subrace(racename, subrace)
    race = races.RACES[racename]
    return race


class NPC(object):
    """Object to define the stat block of the NPC itself"""
    def __init__(self, npcname, classname, race, level, subrace=""):
        self.name = npcname
        self.level = level
        self.bonus = self.get_proficiency_bonus()
        self.char_class = classes.CLASSES[classname]
        self.race = load_race(race, subrace)
        self.subrace = subrace
        self.ability_scores = self.assign_ability_scores(level)
        self.calculate_proficiencies()
        self.skill_proficiencies = self.find_skills()
        self.calc_skills()
        self.melee = weapons.choose_melee(self.weapon_proficiencies)
        self.ranged = weapons.choose_ranged(self.weapon_proficiencies)
        self.powers = (
            self.race["Powers"] + self.get_powers()
            )
        self.hitpoints = self.get_hp(
            self.level, self.ability_bonuses['Constitution']
            )
        if "Caster" in self.char_class:
            self.spell_list = spells.spells_known(self.level, classname)
        self.armor = armor.choose_armor(
            self.armor_proficiencies, self.level,
            self.ability_scores['Strength']
            )
        self.armor_class = self.calc_ac()

    def get_powers(self):
        """Calculate powers for the NPC"""
        powers = []
        for power in self.char_class["Powers"]:
            if power["Level"] <= self.level:
                powers.append(power)
        for power in powers:
            for compare in powers:
                if power["Name"] == compare["Name"]:
                    if power["Level"] < compare["Level"]:
                        powers.remove(power)
                    elif compare["Level"] > power["Level"]:
                        powers.remove(compare)
        return powers

    def get_proficiency_bonus(self):
        """Get proficiency bonus based on level"""
        bonus = 2
        extra_bonus = math.floor((self.level-1)/4)
        bonus += extra_bonus
        return bonus

    def get_hp(self, level, con_bonus):
        """Figure out character's HP"""
        hitpoints = self.char_class["Hit Dice"]
        hitpoints += con_bonus * level
        if self.subrace == "Hill":
            hitpoints += level
        level = level-1
        hitpoints += level * 7
        return hitpoints

    def assign_ability_scores(self, level):
        """Assign ability scores according to standard matrix"""
        ability_scores = {}
        scores_left = [15, 14, 13, 12, 10, 8]
        abilities_left = ABILITIES
        ability_scores[self.char_class["Primary"]] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.char_class["Primary"])
        ability_scores[self.char_class["Secondary"]] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.char_class["Secondary"])
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
            if ability_scores[self.char_class["Primary"]] < 20:
                ability_scores[self.char_class["Primary"]] += 1
                ability_ups -= 1
            elif ability_scores[self.char_class["Secondary"]] < 20:
                ability_scores[self.char_class["Secondary"]] += 1
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
        self.weapon_proficiencies = (
            self.race["Weapon Proficiencies"] +
            self.char_class["Weapon Proficiencies"]
            )

        try:
            self.race["Armor Proficiencies"]
        except:
            self.race["Armor Proficiencies"] = []
        self.armor_proficiencies = (
            self.race["Armor Proficiencies"] +
            self.char_class["Armor Proficiencies"]
            )

        try:
            self.char_class["Tool Proficiencies"]
        except:
            self.char_class["Tool Proficiencies"] = []
        self.tool_proficiencies = (
            self.race["Tool Proficiencies"] +
            self.char_class["Tool Proficiencies"]
            )

    def find_skills(self):
        """Get Race skills, then find remaining Class skills"""
        if "Skills" in self.race:
            skills = self.race["Skills"]
        else:
            skills = []
        for skill in self.char_class["Skill List"]:
            if skill in skills:
                self.char_class["Skill List"].remove(skill)
        counter = self.char_class["Skill Picks"]
        while counter > 0:
            skill = random.choice(self.char_class["Skill List"])
            skills.append(skill)
            self.char_class["Skill List"].remove(skill)
            counter -= 1
        return skills

    def calc_skills(self):
        """Assign values to skill bonuses"""
        skills = {}

        joat_bonus = 0
        if self.char_class == "Bard" and self.level >= 2:
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
        for save in self.char_class["Saves"]:
            saves[save] = self.ability_bonuses[save] + self.bonus
        self.saves = saves

    def calc_ac(self):
        """Figure out a character's AC"""
        if self.char_class["Name"] == "Barbarian":
            armor_class = (
                10 + self.ability_bonuses['Dexterity'] +
                self.ability_bonuses['Constitution']
                )
            del self.armor[0]
        elif self.char_class["Name"] == "Monk":
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
        for item in self.armor:
            if item["Name"] == "Shield":
                armor_class += 2
        return armor_class

    def calc_initiative(self):
        """Figure out a character's intiative"""
        initiative = self.ability_bonuses['Dexterity']
        if self.char_class["Name"] == "Bard" and self.level >= 2:
            initiative += math.floor(self.bonus/2)
        return initiative


def print_character(npc):
    """Print the npc"""
    print(npc.name)
    print(npc.race["Name"])
    print(npc.char_class["Name"])
    print("Level: " + str(npc.level))
    print("HP: " + str(npc.hitpoints))
    print("AC: " + str(npc.armor_class))
    print("Initiative: " + str(npc.calc_initiative()))
    for ability in ["Strength", "Dexterity", "Constitution",
                    "Intelligence", "Wisdom", "Charisma"]:
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
    if "Caster" in npc.char_class:
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
        if 0 < round(level) <= 20:
            level_choice = level
            good_level = True
        else:
            print("Please choose a level from 1 to 20")
    good_race = False
    race_choices = list(range(1, len(races.RACE_LIST)+1))
    race_choices = [str(x) for x in race_choices]
    while good_race is False:
        print("Choose a race: ")
        for item in races.RACE_LIST:
            print(str(races.RACE_LIST.index(item) + 1) + ": " + item)
        race_choice = int(input("Enter the number for your choice: "))
        if race_choice in list(range(1, len(races.RACE_LIST) + 1)):
            race_choice = races.RACE_LIST[race_choice - 1]
            good_race = True
        else:
            print("Not a valid race choice")
    race = races.RACES[race_choice]
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
