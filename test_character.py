import unittest
import character


class test_generation(unittest.TestCase):
    def test_create_dwarven_barbarian(self):
        npc = character.NPC("Arik", "Bard", "Half-Orc", 10, "Hill")
        character.print_character(npc)
