import unittest
import weapons

PROFS = ["Club", "Simple"]

class test_generation(unittest.TestCase):
    def test_weapon_choices(self):
        melee = weapons.choose_melee(PROFS)
        print(melee)
        ranged = weapons.choose_ranged(PROFS)
        print(ranged)
