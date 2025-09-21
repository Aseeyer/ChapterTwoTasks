# (Synonyms Dictionary)

synonyms = {
    "good": ["nice", "great", "fine"],
    "bad": ["awful", "terrible", "poor"],
    "hot": ["warm", "boiling", "heated"],
    "cold": ["chilly", "freezing", "cool"],
    "fun": ["enjoyable", "amusing", "entertaining"]
}

for word, synonym_list in synonyms.items():
    print(f"{word}:")
    for synonym in synonym_list:
        print(f"  {synonym}")
