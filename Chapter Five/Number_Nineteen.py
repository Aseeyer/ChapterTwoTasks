# Finding the People with a Specified Last Name


people = [
    ("Emma", "Somtoo"),
    ("See", "Eze"),
    ("Augie", "Eze"),
    ("Emily", "Brown"),
    ("Mimi", "Eze"),
    ("Aseeyer", "Asee")
]

people_bearing_jones = list(filter(lambda person: person[1] == "Eze", people))

print("People with last name Eze:", people_bearing_jones)


#Just another alternative using list comprehension
jones_people2 = [person for person in people if person[1] == "Jones"]

print("People with last name Jones (list comprehension):", jones_people2)
