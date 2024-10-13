import random

def count_syllables(word):
    """Counts the number of syllables in a word.
    This is a simple heuristic and may not be perfectly accurate.
    """
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count +=1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if count == 0:
        count +=1
    return count
    
def generate_haiku_line(word_bank, target_syllables):
    """Generates a single line of a haiku with a target number of syllables."""
    line = []
    syllable_count = 0
    
    while syllable_count < target_syllables:
        suitable_words = [word for word in word_bank if
                           # Make sure to use the defined function count_syllables.
                           count_syllables(word) <= target_syllables - syllable_count]
        if suitable_words:
            chosen_word = random.choice(suitable_words)
            line.append(chosen_word)
            syllable_count += count_syllables(chosen_word) # Ensure count_syllables is used
        else:
            # If no suitable words are found, return the line as is (might be incomplete)
            return line
    
    return line

def generate_haiku(word_bank):
    """Generates a complete haiku."""
    
    # Try to generate haiku lines with the expected syllable counts (5, 7, 5)
    line1 = generate_haiku_line(word_bank, 5)
    line2 = generate_haiku_line(word_bank, 7)
    line3 = generate_haiku_line(word_bank, 5)
    
    # Check if all lines were successfully generated (not empty)
    if line1 and line2 and line3:
        # Join the words in each line to form a string
        return " ".join(line1) + "\n" + " ".join(line2) + "\n" + " ".join(line3)
    else:
        return None # or some error message
