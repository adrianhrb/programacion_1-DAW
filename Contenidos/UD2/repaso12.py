num_count = 0
for num in range(33, 127 + 1):
    ascii_num = chr(num)
    num_count += 1
    print(f"{num:03}:{ascii_num}", end="  ")
    if num_count % 5 == 0:
        print()
