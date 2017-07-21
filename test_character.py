import unittest
import character


class test_generation(unittest.TestCase):
    def test_create_dwarven_barbarian(self):
        npc = character.NPC("Arik", "Monk", "Half-Elf", 20, "Forest")
        character.print_character(npc)
