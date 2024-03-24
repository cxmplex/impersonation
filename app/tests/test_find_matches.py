import unittest

from app.evaluate import find_matches

class TestFindMatches(unittest.TestCase):
    def test_find_matches(self):
        test_cases = [
            ("johnny smith", "john", "smith"),
            ("johnnysmith", "john", "smith"),
            ("benjammin smith", "benjamin", "smith"),
            ("smith johnny", "john", "smith"),
            ("smith john", "john", "smith"),
            ("smithjohn", "john", "smith"),
            ("smithjohnny", "john", "smith"),
            ("smith johnny", "john", "smith"),
            ("johnnysmithy", "john", "smith"),
            ("johnsmithy", "johnny", "smith"),
            ("smith johnnyson", "john", "smith"),
            ("smithers johannson", "john", "smith"),
            ("johannson smithers", "john", "smith"),
            ("johnannson smithers", "john", "smith"),
            ("smith the one johnny", "john", "smith")
        ]

        expected_results = [
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': 'leven', 'first': 'benjamin', 'last': 'smith'},
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': False, 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': False, 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'},
            {'match': True, 'partial_match': 'reverse_hypocorism', 'first': 'johnny', 'last': 'smith'},
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'},
            {'match': False, 'partial_match': False, 'first': None, 'last': None},
            {'match': False, 'partial_match': False, 'first': None, 'last': None},
            {'match': False, 'partial_match': False, 'first': None, 'last': None},
            {'match': True, 'partial_match': 'hypocorism', 'first': 'john', 'last': 'smith'}
        ]

        for i, (input_data, expected_result) in enumerate(zip(test_cases, expected_results)):
            with self.subTest(f"Test case {i}"):
                normalized_name, first_name, last_name = input_data
                result = find_matches(normalized_name, first_name, last_name)
                self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()