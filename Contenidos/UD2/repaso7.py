x_value = 0
y_value = 0
target_x = 7
target_y = 8

for number in range (0, target_x + 1):
    print(f'({x_value}, {y_value})')
    x_value += 1
    y_value += 2
    for num in range (0, target_y + 1):
        x_value += 2
        y_value += 1
        print(f'({x_value}, {y_value})')
        
        
        
