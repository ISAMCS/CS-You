import random

def count_syllables(word):
    """Counts the number of syllables in a word.
    This is a simple heuristic and may not be perfectly accurate.
    """
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    # Count first syllable if word starts with a vowel
    if word[0] in vowels:
        count += 1
    # Count syllables in the rest of the word
    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            count += 1
    """This method counts syllables based on the principle that a syllable 
    typically contains a vowel sound. It looks for transitions from consonants 
    to vowels, which often indicate the start of a new syllable.
    """
    # Adjust count for words ending in 'e'
    if word.endswith('e'):
        count -= 1
    # Ensure at least one syllable is counted
    if count == 0:
        count += 1
    return count
    
def generate_haiku_line(word_bank, target_syllables):
    """Generates a single line of a haiku with a target number of syllables."""
    line = []
    syllable_count = 0
    
    while syllable_count < target_syllables:
        # Find suitable words that fit within remaining syllables
        suitable_words = [word for word in word_bank if
                           count_syllables(word) <= target_syllables - syllable_count]
        if suitable_words:
            # Randomly choose a word from suitable words
            chosen_word = random.choice(suitable_words)
            line.append(chosen_word)
            syllable_count += count_syllables(chosen_word)
        else:
            # Return incomplete line if no suitable words found
            return line
    
    return line

def generate_haiku(word_bank):
    """Generates a complete haiku."""
    
    # Generate three lines with 5, 7, and 5 syllables respectively
    line1 = generate_haiku_line(word_bank, 5)
    line2 = generate_haiku_line(word_bank, 7)
    line3 = generate_haiku_line(word_bank, 5)
    
    # Check if all lines were successfully generated
    if line1 and line2 and line3:
        # Join words in each line and combine lines with newline characters
        return " ".join(line1) + "\n" + " ".join(line2) + "\n" + " ".join(line3)
    else:
        return None # Return None if haiku generation failed
