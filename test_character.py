import unittest
import character


class test_generation(unittest.TestCase):
    def test_create_dwarven_barbarian(self):
        npc = character.NPC("Arik", "Ranger", "Half-Elf", 1, "Forest")
        character.print_character(npc)
