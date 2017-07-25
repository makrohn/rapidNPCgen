import unittest
from rpcg_web import character


class test_generation(unittest.TestCase):
    def test_create_characters(self):
        for char_class in character.classes.CLASS_LIST:
            for race in character.races.RACE_LIST:
                for level in range(1, 21):
                    npc = character.NPC(
                        "Arik", char_class, race, level, "Forest"
                        )
                    npc.print_character()


class test_spellcaster(unittest.TestCase):
    def test_spellcaster(self):
        npc = character.NPC("Arik", "Bard", "Dwarf", 4, "Hill")
        npc.print_character()
