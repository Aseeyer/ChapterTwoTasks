# (Character Counts)

sentence = input("Enter a sentence: ")

sentence = sentence.lower().replace(" ", "")

letter_counts = {}

for char in sentence:
    if char in letter_counts:
        letter_counts[char] += 1
    else:
        letter_counts[char] = 1

print(f'{"LETTER":<10}COUNT')

for letter, count in sorted(letter_counts.items()):
    print(f'{letter:<10}{count}')




#for the challenge
alphabet = set("abcdefghijklmnopqrstuvwxyz")
letters_used = set(sentence)
missing_letters = alphabet - letters_used

print("\nLetters not in the sentence:", sorted(missing_letters))
