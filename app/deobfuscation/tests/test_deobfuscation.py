import unittest
import json
import os

from app.deobfuscation.clean import normalize
from app.deobfuscation.maps import inverted_merged_characters
from app.deobfuscation.utils import levenshtein_distance_partwise

class TestDeobfuscation(unittest.TestCase):
    def setUp(self):
        # Load test cases from the file
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        with open('test-names.json', 'r', encoding='utf-16') as file:
            self.test_cases = json.load(file)

    def test_deobfuscate(self):
        for test_case in self.test_cases:
            original_name = test_case['name'].lower()
            obfuscated_name = test_case['obfuscated_name']
            # normalize & deobfuscate name
            deobfuscated_name = normalize(obfuscated_name, inverted_merged_characters)
            # split name into first/last and check that each is < 1 character away from it's actual
            distance = levenshtein_distance_partwise(original_name, deobfuscated_name)
            self.assertTrue(distance <= 2, f"Failed on {original_name} != {deobfuscated_name} with distance {distance}")


if __name__ == '__main__':
    unittest.main()
