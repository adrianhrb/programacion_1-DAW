obj_num = 87
attempts = 0

while True:
    guess_number = int(input("Dime un número: "))
    if guess_number == obj_num:
        attempts += 1
        print(f'✅ ¡Enhorabuena! Has encontrado el número en {attempts} intentos')
        break
    elif guess_number > obj_num:
        attempts += 1
        print('Menor')
    else:
        attempts += 1
        print("Mayor")