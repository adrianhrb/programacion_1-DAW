string_prototype = input("Dime algo: ")
alternative_case = ""

for char in string_prototype:
    new_char = char.swapcase()
    alternative_case += new_char

print(alternative_case)