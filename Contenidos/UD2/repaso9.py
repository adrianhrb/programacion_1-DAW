a = 12
b = 44

for num in range (44, 0, -1):
    if a % num == 0 and b % num == 0:
        break
    else:
        continue
        
print(num)