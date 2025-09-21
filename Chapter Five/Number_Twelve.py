# Telephone Number Word Generator
def generate_phone_words(phone_number):
    digit_to_letters = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI',
        '5': 'JKL', '6': 'MNO', '7': 'PRS',
        '8': 'TUV', '9': 'WXY'
    }

    words = ['']
    for digit in phone_number:
        if digit in digit_to_letters:
            letters = digit_to_letters[digit]
            words = [prefix + letter for prefix in words for letter in letters]

    return words





phone_number = "6862377"
all_words = generate_phone_words(phone_number)

print(f"Total combinations: {len(all_words)}")
print("Sample words:", all_words[:10])
