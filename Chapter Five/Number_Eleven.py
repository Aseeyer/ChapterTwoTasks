# Summarizing letters in a string
def summarize_letters(input_string):
    normalized_string = ''.join(character.lower() for character in input_string if character.isalpha())

    letter_frequencies = {}
    for character in normalized_string:
        letter_frequencies[character] = letter_frequencies.get(character, 0) + 1

    summary_list = list(letter_frequencies.items())
    return summary_list


test_string = "The quick brown fox jumps over the lazy dog!"

summary = summarize_letters(test_string)

print("Letter Frequencies:")
for letter, frequency in summary:
    print(f"{letter}: {frequency}")



alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
contains_all_letters = alphabet_set.issubset(set(character.lower() for character in test_string if character.isalpha()))

if contains_all_letters:
    print("\nThe string contains all the letters of the alphabet.")
else:
    print("\nThe string does NOT contain all the letters of the alphabet.")
