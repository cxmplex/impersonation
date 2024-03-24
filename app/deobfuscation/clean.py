# functions to deobfuscate and normalize input
import re

def deobfuscate(content, obfs_map):
    """
    Deobfuscate characters in the content using the provided obfuscation map.
    Add debugging to inspect replacements.
    """
    for unicode_char, ascii_char in obfs_map.items():
        if unicode_char in content:
            content = content.replace(unicode_char, ascii_char)
    return content


def normalize(content, character_map):
    """
    Normalize the content by deobfuscating characters and converting to lowercase.

    Args:
    - content (str): The text content to normalize.
    - character_map (dict): A map for character deobfuscation.

    Returns:
    - tuple: (normalized_content (str), results (dict))
    """
    normalized = deobfuscate(content, character_map)
    
    normalized_lower = normalized.lower()
    
    return re.sub(r'[^a-z\s]', '', normalized_lower)
