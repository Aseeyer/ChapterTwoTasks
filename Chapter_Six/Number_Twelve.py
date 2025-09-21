# (Translation Dictionary)

translations = {
    "Good Morning": "Ututu Oma",
    "goodbye": "Ka Odi",
    "thank you": "Daalu",
    "yes": "eyaa",
    "no": "mba",
    "Food": "nri"
}

print(f'{"ENGLISH":<20}{"IGBO TRANSLATION"}')
for english_word, translated_to_igbo in translations.items():
    print(f'{english_word:<20}{translated_to_igbo:<20}')
