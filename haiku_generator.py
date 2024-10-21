import random
import re

def count_syllables(word):
    """Counts the number of syllables in a word using regex."""
    word = word.lower()
    # Define vowel groups
    vowels = "aeiouy"
    # Remove silent 'e' at the end
    word = re.sub(r'e$', '', word)
    # Count vowel groups as syllables
    syllable_count = len(re.findall(r'[aeiouy]+', word))
    # Ensure at least one syllable is counted
    return max(1, syllable_count)
    
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
