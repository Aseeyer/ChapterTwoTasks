# (Counting Duplicate Words)

sentence = "This is a rough sentence with some words and This rough sentence has duplicates that are not really rough"

sentence = sentence.lower()

word_counts = {}

for word in sentence.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("The Duplicate words in my sentence and how many count:")
for word, count in word_counts.items():
    if count > 1:
        print(f"{word}: {count}")
