import random
import json


from app.deobfuscation.maps import merged_characters, leet
# List of common first and last names to obfuscate
names = [
    "James Smith", "Michael Johnson", "Robert Brown", "Maria Garcia", "David Miller",
    "Sarah Davis", "Charles Wilson", "Emily Moore", "Daniel Taylor", "Jessica White"
]

# Function to obfuscate a single name
def obfuscate_name(name, character_map, leet_map):
    # Splitting the name into first and last names
    parts = name.split(" ")
    
    obfuscated_parts = []
    for part in parts:
        obfuscated_part = ""
        for char in part:
            # Randomly decide whether to obfuscate the character
            if random.random() < 0.5:
                if char.lower() in character_map and random.random() < 0.5:
                    # Replace with a random equivalent character from character_map
                    possible_replacements = character_map[char.lower()]
                    obfuscated_part += random.choice(possible_replacements)
                elif char.lower() in leet_map:
                    # Replace with a leet equivalent
                    obfuscated_part += leet_map[char.lower()]
                else:
                    obfuscated_part += char
            else:
                obfuscated_part += char
        obfuscated_parts.append(obfuscated_part)
    return " ".join(obfuscated_parts)

# Generate 100 obfuscated names
obfuscated_names = []
for _ in range(100):
    name = random.choice(names)
    obfuscated_name = obfuscate_name(name, merged_characters, leet)
    obfuscated_names.append({"name": name, "obfuscated_name": obfuscated_name})

with open('test-names.json', 'w', encoding='utf-16', ) as fh:
    json.dump(obfuscated_names, fh)