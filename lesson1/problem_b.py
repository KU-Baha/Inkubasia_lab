# In Excel, columns are named using letters, and then more letters are added as necessary:

# Column 1: “A”
# Column 2: “B”
# …
# Column 26: “Z”
# Column 27: “AA”
# Column 28: “AB”
# …
# Column 52: “AZ”
# Column 53: “BA”
# Column 54: “BB”
# …
# Column ?: “ZZ”
# Column ?: “AAA”
# Column ?: “AAB”

# Write a function that takes a column number and returns a string representing the column name.
import string

ascii_uppercase = string.ascii_uppercase


def excel_colum(colum_number: int) -> string:
    result = ''

    while colum_number > 0:
        colum_number, remainder = (colum_number - 1) // 26, (colum_number - 1) % 26
        result = ascii_uppercase[remainder] + result

    return result


print(excel_colum(52))
