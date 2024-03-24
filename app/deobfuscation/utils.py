# https://en.wikipedia.org/wiki/Levenshtein_distance?useskin=vector

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def levenshtein_distance_partwise(s1, s2):
    parts1 = s1.split()
    parts2 = s2.split()
    total_distance = 0
    
    for part1, part2 in zip(parts1, parts2):
        distance = levenshtein_distance(part1, part2)
        total_distance += distance
        
    return total_distance