can_fly = True
is_human = True
has_mask = True

if can_fly:
    if is_human:
        if has_mask:
            print('Ironman')
        else:
            print('Captain Marvel')
    else:
        if has_mask:
            print("Ronan accuser")
        else:
            print("Vision")
else:
    if is_human:
        if has_mask:
            print("Spiderman")
        else:
            print("Hulk")
    else: 
        if has_mask:
            print("Black Bolt")
        else:
            print("Thanos")