num_char = 0
for code in range(33, 127 + 1):
    ascii_num = chr(code)
    num_char += 1
    print(f"{code:03}:{ascii_num}", end="  ")
    #Desplazamiento modular
    if num_char % 5 == 0:
        print()

