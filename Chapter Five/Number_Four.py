#Creating a 2-by-3 list
number_of_rows = 2
number_of_columns = 3
table_data = [[0 for column_index in range(number_of_columns)] for row_index in range(number_of_rows)]
#The list comprehension creates a 2-row, 3-column list filled with zeros.
#Each inner list represents a row in the table.


#Part (a): Fill the list with order numbers
order_number = 1
for current_row in range(number_of_rows):
    for current_column in range(number_of_columns):
        table_data[current_row][current_column] = order_number
        order_number += 1
#The nested loops go through each row and column in order.
#Each element gets a value showing the order in which it was processed.


#Part (b): Display in tabular format
print("        ", end="")
for column_index in range(number_of_columns):
    print(f"Column{column_index}", end="\t")
print()

for row_index in range(number_of_rows):
    print(f"Row{row_index}", end="\t")
    for column_index in range(number_of_columns):
        print(table_data[row_index][column_index], end="\t")
    print()
#The first loop prints column headings (Column0, Column1, Column2).
#The nested loops print each row label (Row0, Row1) and the data values in table format.
