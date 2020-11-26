import unittest
from chapter10_name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for chapter10_name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Piotr Jab' work?"""
        formatted_name=get_formatted_name('piotr','jab')
        self.assertEqual(formatted_name,'Piotr Jab')

    def test_first_last_middle_name(self):
        """"Do names like Piotr Andrzej Jablo work?"""
        formatted_name=get_formatted_name("Piotr","jabl","andrzej")
        self.assertEqual(formatted_name, "Piotr Andrzej Jabl")
        
if __name__=='__main__':
    unittest.main()