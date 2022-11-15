import sys

# En values tendremos una lista con los valores (como strings)
"""values = sys.argv[1:]
total_numbers = 0
addition = 0
for num in values:
    number = int(num)
    total_numbers += 1
    addition += number

avg = addition / total_numbers
print(avg)"""

values = sys.argv[1:]
total_numbers = int(len(values.split(" ")))
avg = [int(number / total_numbers) for number in values]