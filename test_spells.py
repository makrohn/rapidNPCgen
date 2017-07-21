import unittest
import spells


class test_spell_picker(unittest.TestCase):
    def test_spell_picker(self):
        spell_list = spells.spells_known(1, "Cleric", 3)
        print(spell_list)
