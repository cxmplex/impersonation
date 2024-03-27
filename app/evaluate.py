from app.deobfuscation.maps import hypocorisms, reverse_hypocorisms
from app.deobfuscation.utils import levenshtein_distance

def create_word_pairs(input_string):
    # Split the string into words based on spaces
    words = input_string.split()
    # List to hold the pairs
    pairs = []

    # Loop through the words to create pairs
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # Add the pair to the list
            pairs.append((words[i], words[j]))

    return pairs


def find_matches(normalized_name, first_name, last_name):
    """
    Identifies if a given normalized name matches or partially matches with the provided first and last name by checking
    various combinations and applying specific match criteria, including direct matches, Levenshtein distance, and
    potential hypocorism matches.

    Args:
    - normalized_name (str): The name to be matched, which may be a combination of first and/or last name,
                             potentially with variations or additional words.
    - first_name (str): The first name of the individual to match against.
    - last_name (str): The last name of the individual to match against.

    Returns:
    - dict: A dictionary with the match status, indicating if a direct match or partial match was found, and
            the first and last name if a match is identified. The dictionary includes the following keys:
            - 'match' (bool): True if a direct match is found, False otherwise.
            - 'partial_match' (bool/str): False if no partial match is found, otherwise a string describing
                                          the type of partial match (e.g., "leven" for Levenshtein distance match,
                                          "hypocorism" for nickname match, "reverse_hypocorism" for reversed name match).
            - 'first' (str/None): The first name if a match is found, None otherwise.
            - 'last' (str/None): The last name if a match is found, None otherwise.
    """
    result = {
        'match': False,
        'partial_match': False,
        'first': None,
        'last': None,
    }

    word_pairs = create_word_pairs(normalized_name) or [(f"{normalized_name}", '')]

    for pair in word_pairs:
        normalized_name_lower = f"{pair[0]}{pair[1]}".lower()
        first_name_lower = first_name.lower()
        last_name_lower = last_name.lower()

        # Check for direct match
        if normalized_name_lower == f"{first_name_lower}{last_name_lower}" or normalized_name_lower == f"{last_name_lower}{first_name_lower}" \
            or normalized_name_lower.replace(" ", "") == f"{first_name_lower}{last_name_lower}" or normalized_name_lower.replace(" ", "") == f"{last_name_lower}{first_name_lower}":
            result.update(match=True, first=first_name, last=last_name)
            return result

        # Check for leven distance
        full_name_direct = f"{first_name_lower}{last_name_lower}"
        full_name_reversed = f"{last_name_lower}{first_name_lower}"
        direct_ratio = levenshtein_distance(full_name_direct, normalized_name_lower) / max(len(normalized_name_lower), len(full_name_direct))
        reversed_ratio = levenshtein_distance(full_name_reversed, normalized_name_lower) / max(len(normalized_name_lower), len(full_name_reversed))
        if direct_ratio <= 0.15 or reversed_ratio <= 0.15:
            result.update(match=True, partial_match="leven", first=first_name, last=last_name)


        # If not a direct match, and not leven, check for partial matches including reversed names and potential hypocorisms
        if not result['match']:
            # Check for potential hypocorism match
            if first_name_lower in hypocorisms:
                for nickname in hypocorisms[first_name_lower]:
                    if (nickname in normalized_name_lower and last_name_lower in normalized_name_lower) or \
                    (last_name_lower in normalized_name_lower and nickname in normalized_name_lower):
                        result.update(match=True, partial_match="hypocorism", first=first_name, last=last_name)
                        break  # A match found, no need to check further
            # Check for reversed name format for partial match
            if last_name_lower in normalized_name_lower:
                if any(name in normalized_name_lower for name in reverse_hypocorisms.get(first_name_lower, [])):
                    result.update(match=True, partial_match="reverse_hypocorism", first=first_name, last=last_name)
        if result['match'] or result['partial_match']:
            return result
    return result
