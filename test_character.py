import unittest
import character


class test_generation(unittest.TestCase):
    def test_create_dwarven_barbarian(self):
        npc = character.NPC("Arik", "Barbarian", "Dwarf", 4, "Mountain")
        character.print_character(npc)
