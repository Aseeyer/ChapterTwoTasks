# Function to generate all possible anagrams
def generate_anagrams(input_string):
    if len(input_string) <= 1:
        return [input_string]

    anagram_list = []
    for index in range(len(input_string)):
        current_character = input_string[index]
        remaining_characters = input_string[:index] + input_string[index + 1:]

        for sub_anagram in generate_anagrams(remaining_characters):
            anagram_list.append(current_character + sub_anagram)

    return anagram_list


word = "abc"
all_anagrams = generate_anagrams(word)

print(f"All anagrams of '{word}':")
for anagram in all_anagrams:
    print(anagram)
