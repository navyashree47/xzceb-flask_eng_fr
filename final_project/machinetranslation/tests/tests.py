import unittest

from translator import englishToFrench, frenchToEnglish

class TestMyModule(unittest.TestCase):

    def test_english_to_french(self):

        self.assertNotEqual(englishToFrench("None"), "")

        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_french_to_english(self):

        self.assertNotEqual(frenchToEnglish("None"), "")

        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()