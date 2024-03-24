import unittest
import json
import os

from app.deobfuscation.clean import normalize
from app.deobfuscation.maps import inverted_merged_characters
from app.evaluate import find_matches

class TestImpersonation(unittest.TestCase):
    def test_impersonation_logic(self):
        expected_results = [
            {'match': True, 'partial_match': False, 'first': 'James', 'last': 'Smith'},
            {'match': True, 'partial_match': False, 'first': 'James', 'last': 'Smith'},
            {'match': True, 'partial_match': False, 'first': 'James', 'last': 'Smith'},
            {'match': True, 'partial_match': False, 'first': 'James', 'last': 'Smith'},
            {'match': True, 'partial_match': False, 'first': 'James', 'last': 'Smith'},
            {'match': True, 'partial_match': False, 'first': 'James', 'last': 'Smith'},
            {'match': True, 'partial_match': False, 'first': 'David', 'last': 'Miller'},
            {'match': True, 'partial_match': False, 'first': 'Emily', 'last': 'Moore'},
            {'match': True, 'partial_match': False, 'first': 'Jessica', 'last': 'White'}
        ]

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # load company users
        with open('company_users.json') as f:
            company_users = json.load(f)

        # load header froms
        with open('header_froms.json') as f:
            header_froms = json.load(f)

        normalized_header_froms = [normalize(x, inverted_merged_characters) for x in header_froms]
        results = []
        for user in company_users:
            for header_from in normalized_header_froms:
                result = find_matches(header_from, user['first_name'], user['last_name'])
                if result['match'] or result['partial_match']:
                    results.append(result)

        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()