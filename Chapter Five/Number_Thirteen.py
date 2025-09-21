# Word or Phrase to Phone-Number Generator
def word_to_phone_number(word):
    letter_to_digit = {
        **dict.fromkeys(list("ABC"), '2'),
        **dict.fromkeys(list("DEF"), '3'),
        **dict.fromkeys(list("GHI"), '4'),
        **dict.fromkeys(list("JKL"), '5'),
        **dict.fromkeys(list("MNO"), '6'),
        **dict.fromkeys(list("PRS"), '7'),
        **dict.fromkeys(list("TUV"), '8'),
        **dict.fromkeys(list("WXY"), '9')
    }

    normalized_word = ''.join(character.upper() for character in word if character.isalpha())
    phone_number = ''.join(letter_to_digit.get(character, '') for character in normalized_word)

    return phone_number


word = "BIGDATA"
phone_number = word_to_phone_number(word)
print(f"The phone number for '{word}' is {phone_number}")
