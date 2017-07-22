import unittest
import character


class test_generation(unittest.TestCase):
    def test_create_characters(self):
        for char_class in character.classes.CLASS_LIST:
            for race in character.races.RACE_LIST:
                for level in range(1, 21):
                    npc = character.NPC(
                        "Arik", char_class, race, level, "Forest"
                        )
                    character.print_character(npc)
