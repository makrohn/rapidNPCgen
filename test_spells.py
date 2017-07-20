import unittest
import spells


class test_spell_picker(unittest.TestCase):
    def test_spell_picker(self):
        spell_list = spells.spells_known(19, "Bard")
        print(spell_list)
