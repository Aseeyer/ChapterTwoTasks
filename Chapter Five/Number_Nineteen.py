# Finding the People with a Specified Last Name


people = [
    ("Emma", "Somtoo"),
    ("See", "Eze"),
    ("Augie", "Eze"),
    ("Emily", "Brown"),
    ("Mimi", "Eze"),
    ("Aseeyer", "Asee")
]

people_bearing_Eze= list(filter(lambda person: person[1] == "Eze", people))

print("People with last name Eze:", people_bearing_Eze)


#Just another alternative using list comprehension
people_bearing_Eze2 = [person for person in people if person[1] == "Eze"]

print("People with last name Eze (list comprehension):", people_bearing_Eze2)
