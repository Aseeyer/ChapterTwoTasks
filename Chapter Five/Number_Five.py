#Creating the string
alphabet = 'abcdefghijklmnopqrstuvwxyz'


#A: The first half using starting and ending indices
first_half = alphabet[0:13]



#B: The first half using only the ending index
first_half_short = alphabet[:13]



#C: The second half using starting and ending indices
second_half = alphabet[13:26]



#D: The second half using only the starting index
second_half_short = alphabet[13:]



#E: Every second letter starting with 'a'
every_second_letter = alphabet[0::2]


#F: The entire string in reverse
reverse_alphabet = alphabet[::-1]


#G: Every third letter in reverse starting with 'z'
every_third_reverse = alphabet[::-3]
