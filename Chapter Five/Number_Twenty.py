# Display a Two-Dimensional List in Tabular Format)


def display_table(table):
    print("    ", end="")
    for col in range(len(table[0])):
        print(f"{col:>5}", end="")
    print()



    for row_idx, row in enumerate(table):
        print(f"{row_idx:>3} ", end="")
        for value in row:
            print(f"{value:>5}", end="")
        print()


data = [
    [1, 2, 12],
    [4, 5, 6],
    [7, 8, 9],
]

display_table(data)
