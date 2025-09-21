# (Duplicate Word Removal)

def unique_words(word_list):
    lower_words = [word.lower() for word in word_list]

    unique = set(lower_words)

    sorted_unique = sorted(unique)

    print("The unique words in alphabetical order:")
    for word in sorted_unique:
        print(word)


sentence1 = "i am a mistic an atheist a skeptic and a woke being lol"
sentence2 = "learning Python java PYTHON C++ java JavaScript python"
sentence3 = "At the End of aLL Seriousness, the end is death amd maybe a new beginning"

unique_words(sentence1.split())
print()
unique_words(sentence2.split())
print()
unique_words(sentence3.split())
