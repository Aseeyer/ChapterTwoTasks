#Create a list of five numbers and sum up all the number
list_of_numbers = [1,2,3,4,5]
total = 0
for number in list_of_numbers:
    total += number
print(total)



#Create a list of words and print a new list with the length of each words in the corresponding index of the word
word_list = ["apple", "banana", "cherry", "aforapplebforball"]
lengths = []
for word in word_list:
    lengths.append(len(word))
print(lengths)


#Create a list of 10 integers and print the numbers at the odd index
number_list = [2,22,4,5,6,7,8,9,10,1]
new_number_list = 0
for number in range(0, 10):
    if number % 2 == 1:
        new_number_list = number_list[number]
        print(new_number_list)



