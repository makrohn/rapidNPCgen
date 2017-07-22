"""Main module to generate D&D5e NPCs rapidly with minimal input"""

import math
import random

import classes
import races
import weapons
import spells
import armor

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
    def __init__(self, npcname, classname, race, level, subrace=""):
        self.name = npcname
        self.level = level
        self.char_class = classes.load_class_file(classname)
        self.race = races.load_race_file(race, subrace)
        self.sheet = {}
        self.sheet["Subrace"] = subrace
        self.sheet["Name"] = self.name
        self.sheet["Race"] = self.race
        self.sheet["Ability Scores"] = self.assign_ability_scores(level)
        self.calc_proficiencies()
        self.sheet["Skill Proficiencies"] = self.find_skills()
        self.sheet["Expertise Skills"] = self.calc_expertise()
        self.sheet["Skill Bonuses"] = self.calc_skills()
        self.sheet["Melee Weapon"] = \
            weapons.choose_melee(self.sheet["Weapon Proficiencies"])
        self.sheet["Ranged Weapon"] = \
            weapons.choose_ranged(self.sheet["Weapon Proficiencies"])
        self.sheet["Powers"] = (
            self.race["Powers"] + self.get_powers()
            )
        self.sheet["Hit Points"] = self.get_hp(
            self.level, self.sheet["Ability Bonuses"]['Constitution']
            )
        if "Caster" in self.char_class:
            self.sheet["Spells"] = spells.spells_known(
                self.level, classname,
                self.sheet["Ability Bonuses"][self.char_class["Casting Stat"]]
                )
        if self.char_class["Name"] != "Monk":
            self.sheet["Armor"] = armor.choose_armor(
                self.sheet["Armor Proficiencies"], self.level,
                self.sheet["Ability Scores"]['Strength']
                )
        else:
            self.sheet["Armor"] = ["None"]
            self.unarmored_movement()
        self.sheet["AC"] = self.calc_ac()

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
        if self.sheet["Subrace"] == "Hill":
            hitpoints += level
        level = level-1
        hitpoints += level * 7
        return hitpoints

    def assign_ability_scores(self, level):
        """Assign ability scores according to standard matrix"""
        ability_scores = {}
        scores_left = [15, 14, 13, 12, 10, 8]
        abilities_left = [
            "Strength", "Dexterity", "Constitution",
            "Intelligence", "Wisdom", "Charisma"
            ]
        ability_scores[self.char_class["Primary"]] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.char_class["Primary"])
        ability_scores[self.char_class["Secondary"]] = scores_left[0]
        del scores_left[0]
        abilities_left.remove(self.char_class["Secondary"])
        counter = len(abilities_left)
        while counter > 0:
            next_ability = random.choice(abilities_left)
            ability_scores[next_ability] = scores_left[0]
            del scores_left[0]
            abilities_left.remove(next_ability)
            counter -= 1
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
                abilities = [ability for ability in ability_scores]
                stat_up = random.choice(abilities)
                if ability_scores[stat_up] < 20:
                    ability_scores[stat_up] += 1
                    ability_ups -= 1
        self.sheet["Ability Bonuses"] = {}
        for score in ability_scores:
            self.sheet["Ability Bonuses"][score] = math.floor(
                (ability_scores[score] - 10)/2
                )
        return ability_scores

    def calc_proficiencies(self):
        """Combine racial and class proficiencies"""
        self.sheet["Weapon Proficiencies"] = (
            self.race["Weapon Proficiencies"] +
            self.char_class["Weapon Proficiencies"]
            )

        self.sheet["Armor Proficiencies"] = (
            self.race["Armor Proficiencies"] +
            self.char_class["Armor Proficiencies"]
            )

        self.sheet["Tool Proficiencies"] = (
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
        proficiency_bonus = self.get_proficiency_bonus()

        joat_bonus = 0
        if self.char_class["Name"] == "Bard" and self.level >= 2:
            joat_bonus = math.floor(proficiency_bonus/2)

        stat_map = {
            "Strength": STR_SKILLS, "Dexterity": DEX_SKILLS,
            "Intelligence": INT_SKILLS, "Charisma": CHA_SKILLS,
            "Wisdom": WIS_SKILLS
            }

        for stat in stat_map:
            for skill in stat_map[stat]:
                if skill in self.sheet["Skill Proficiencies"]:
                    skills[skill] = (
                        self.sheet["Ability Bonuses"][stat] +
                        proficiency_bonus
                        )
                elif skill in self.sheet["Expertise Skills"]:
                    skills[skill] = (
                        self.sheet["Ability Bonuses"][stat] +
                        (proficiency_bonus * 2)
                        )
                else:
                    skills[skill] = (
                        self.sheet["Ability Bonuses"][stat] + joat_bonus
                        )

        saves = {}
        for save in self.char_class["Saves"]:
            saves[save] = (
                self.sheet["Ability Bonuses"][save] + proficiency_bonus
                )
        self.sheet["Saves"] = saves

        return skills

    def calc_expertise(self):
        """Calculate Bard or Rogue proficiencies"""
        expertise_skills = []
        if self.char_class["Name"] == "Rogue":
            if self.level < 6:
                counter = 2
            elif self.level >= 6:
                counter = 4
        elif self.char_class["Name"] == "Bard":
            if self.level < 3:
                counter = 0
            elif 3 <= self.level < 10:
                counter = 2
            elif len(self.sheet["Skill Proficiencies"]) == 3:
                counter = 3
            elif self.level >= 10:
                counter = 4
        else:
            counter = 0
        while counter > 0:
            new_expert = random.choice(self.sheet["Skill Proficiencies"])
            expertise_skills.append(new_expert)
            self.sheet["Skill Proficiencies"].remove(new_expert)
            counter -= 1
        return expertise_skills

    def calc_ac(self):
        """Figure out a character's AC"""
        if self.char_class["Name"] == "Barbarian":
            armor_class = (
                10 + self.sheet["Ability Bonuses"]['Dexterity'] +
                self.sheet["Ability Bonuses"]['Constitution']
                )
            del self.sheet["Armor"][0]
        elif self.char_class["Name"] == "Monk":
            armor_class = (
                10 + self.sheet["Ability Bonuses"]['Dexterity'] +
                self.sheet["Ability Bonuses"]['Wisdom']
                )
            del self.sheet["Armor"][0]
        else:
            armor_class = self.sheet["Armor"][0]["AC"]
            if (self.sheet["Ability Bonuses"]['Dexterity'] >
                    self.sheet["Armor"][0]["Dex_max"]):
                ac_bonus = self.sheet["Armor"][0]["Dex_max"]
            else:
                ac_bonus = self.sheet["Ability Bonuses"]['Dexterity']
            armor_class += ac_bonus
        for item in self.sheet["Armor"]:
            if item["Name"] == "Shield":
                armor_class += 2
        for power in self.char_class["Powers"]:
            if power["Name"] == "Defense":
                armor_class += 1
        return armor_class

    def calc_initiative(self):
        """Figure out a character's intiative"""
        initiative = self.sheet["Ability Bonuses"]['Dexterity']
        if self.char_class["Name"] == "Bard" and self.level >= 2:
            initiative += math.floor(self.get_proficiency_bonus()/2)
        return initiative

    def unarmored_movement(self):
        """Add a Monk's unarmored movement bonus to their base racial speed"""
        if self.level > 1:
            movement_bonus = (math.ceil((self.level-1)/4) + 1) * 5
        else:
            movement_bonus = 0
        self.race["Speed"] += movement_bonus


def print_character(npc):
    """Print the npc"""
    print(npc.sheet["Name"])
    print(npc.sheet["Race"])
    print(npc.char_class["Name"])
    print("Level: " + str(npc.level))
    print("HP: " + str(npc.sheet["Hit Points"]))
    print("AC: " + str(npc.sheet["AC"]))
    print("Initiative: " + str(npc.calc_initiative()))
    print("Proficiency Bonus: " + str(npc.get_proficiency_bonus()))
    for ability in ["Strength", "Dexterity", "Constitution",
                    "Intelligence", "Wisdom", "Charisma"]:
        print(
            ability + ": " + str(npc.sheet["Ability Scores"][ability]) +
            " (" + str(npc.sheet["Ability Bonuses"][ability]) + ")"
            )
    print("Saves: " + str(npc.sheet["Saves"]))
    print("Size: " + npc.race["Size"])
    print("Speed: " + str(npc.race["Speed"]))
    print("Darkvision: " + str(npc.race["Darkvision"]))
    print("Proficiencies")
    print(npc.sheet["Weapon Proficiencies"])
    print(npc.sheet["Armor Proficiencies"])
    print(npc.sheet["Tool Proficiencies"])
    print(npc.sheet["Skill Proficiencies"])
    print(npc.sheet["Expertise Skills"])
    print(npc.race["Languages"])
    for skill in ALL_SKILLS:
        print(skill + ": " + str(npc.sheet["Skill Bonuses"][skill]))
    print(npc.sheet["Melee Weapon"])
    print(npc.sheet["Ranged Weapon"])
    print(npc.sheet["Armor"])
    for power in npc.sheet["Powers"]:
        print(power["Name"] + ": " + power["Text"])
    if "Caster" in npc.char_class:
        print(npc.sheet["Spells"])
        print(spells.spell_slots(npc.level, npc.char_class["Name"]))


def class_picker():
    """Interactively prompt for a class choice"""
    class_choices = list(range(1, len(classes.CLASS_LIST)+1))
    class_choices = [str(x) for x in class_choices]
    good_class = False
    while good_class is False:
        print("Choose a class: ")
        for item in classes.CLASS_LIST:
            print(str(classes.CLASS_LIST.index(item) + 1) + ": " + item)
        class_choice = int(input("Enter the number for your choice: "))
        if class_choice in list(range(1, len(classes.CLASS_LIST) + 1)):
            class_choice = classes.CLASS_LIST[class_choice - 1]
            good_class = True
        else:
            print("Not a valid class choice")
    return class_choice


def level_query():
    """Interactively prompt for NPC level"""
    good_level = False
    while good_level is False:
        level = int(input("Level? "))
        if 0 < round(level) <= 20:
            level_choice = level
            good_level = True
        else:
            print("Please choose a level from 1 to 20")
    return level_choice


def race_picker():
    """Interactively prompt for a race choice"""
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
    return race_choice


def subrace_picker(race):
    """Interactively prompt for a subrace choice"""
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
            good_subrace = True
        else:
            print("Not a valid subrace choice")
    return subrace_choice


def create_character():
    """Interactively request all the necessary fields to create an NPC"""
    name = input("Name? ")
    class_choice = class_picker()
    level = level_query()
    race = race_picker()
    subrace_check = races.load_race_file(race)
    if "Subraces" in subrace_check:
        subrace = subrace_picker(subrace_check)
        npc = NPC(name, class_choice, race, level, subrace)
    else:
        npc = NPC(name, class_choice, race, level)
    print_character(npc)

if __name__ == "__main__":
    create_character()
