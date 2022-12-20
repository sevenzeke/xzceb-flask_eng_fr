import unittest

from translator import englishtofrench, frenchtoenglish

class TestTranslator(unittest.TestCase):

    def test_english_to_french_null_input(self):
        self.assertNotEqual(englishtofrench(None),'Bonjour')

    def test_french_to_english_null_input(self):
        self.assertNotEqual(frenchtoenglish(None),'Hello')

    def test_english_to_french(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()