#Tuples Representing Invoices
from operator import itemgetter

invoices = [
    (83, "Electric sander", 7, 57.98),
    (24, "Power saw", 18, 99.99),
    (7, "Sledge hammer", 11, 21.50),
    (77, "Hammer", 76, 11.99),
    (39, "Jig saw", 3, 79.50)
]

print("a) Sort by part description:")
for item in sorted(invoices, key=itemgetter(1)):
    print(item)

print("\nb) Sort by price:")
for item in sorted(invoices, key=itemgetter(3)):
    print(item)

print("\nc) (Description, Quantity) sorted by quantity:")
desc_qty = [(desc, qty) for _, desc, qty, _ in invoices]
for item in sorted(desc_qty, key=itemgetter(1)):
    print(item)

print("\nd) (Description, Value) sorted by value:")
desc_value = [(desc, qty * price) for _, desc, qty, price in invoices]
for item in sorted(desc_value, key=itemgetter(1)):
    print(item)

print("\ne) Filter invoice values between 200 and 500:")
for item in filter(lambda x: 200 <= x[1] <= 500, desc_value):
    print(item)

print("\nf) Total of all invoices:")
total = sum(value for _, value in desc_value)
print(total)
