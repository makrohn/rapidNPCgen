import unittest
import character


class test_generation(unittest.TestCase):
    def test_create_dwarven_barbarian(self):
        npc = character.NPC("Arik", "Bard", "Half-Elf", 10, "Mountain")
        character.print_character(npc)
