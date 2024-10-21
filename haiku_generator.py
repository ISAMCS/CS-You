import random
import re

def count_syllables(word):
    """Counts the number of syllables in a word using regex and additional rules."""
    word = word.lower()  # Convert the word to lowercase for consistency
    
    # Exception list for words with irregular syllable counts
    exceptions = {
        "area": 3, "idea": 3, "real": 2, "being": 2, "create": 2,
        "really": 2, "business": 2, "beautiful": 3, "science": 2
    }
    
    # Check if the word is in the exceptions list and return its syllable count if it is
    if word in exceptions:
        return exceptions[word]
    
    # Remove non-alphabetic characters (e.g., hyphens, apostrophes)
    word = re.sub(r'[^a-z]', '', word)
    
    # Define vowels
    vowels = "aeiouy"
    
    # Count initial vowel as a syllable if present
    if word[0] in vowels:
        count = 1
    else:
        count = 0
    
    # Count vowel groups as syllables
    # re.findall returns all non-overlapping matches of the pattern in the string
    # [aeiouy]{1,2} matches 1 or 2 consecutive vowels
    count += len(re.findall(r'[aeiouy]{1,2}', word[1:]))
    
    # Adjust for specific patterns
    
    # Subtract silent 'e' at the end of words
    # (?<=[aeiouy])e$ matches 'e' at the end of a word preceded by a vowel
    count -= len(re.findall(r'(?<=[aeiouy])e$', word))
    
    # Add syllable for 'le' at the end, which typically forms its own syllable
    count += len(re.findall(r'le$', word))
    
    # Subtract syllables for 'es' and 'ed' endings, which often don't add a syllable
    count -= len(re.findall(r'es$|ed$', word))
    
    # Add syllable for 'ion' suffix, which usually adds a syllable
    count += len(re.findall(r'ion', word))
    
    # Handle words ending in 'y' preceded by a consonant
    # (?<=[^aeiou])y$ matches 'y' at the end of a word preceded by a non-vowel
    if re.search(r'(?<=[^aeiou])y$', word):
        count += 1
    
    # Ensure at least one syllable is counted
    return max(1, count)
    
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
