import unittest
import armor

PROFS = ["Light", "Shield", "Heavy"]

class test_generation(unittest.TestCase):
    def test_armor_choices(self):
        armor_choice = armor.choose_armor(PROFS, 20, 13)
        for piece in armor_choice:
            print(piece)