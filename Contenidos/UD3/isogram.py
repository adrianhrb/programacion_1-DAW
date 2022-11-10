word = input("Dime algo: ")
seen_chars = []

for letter in word:
    if letter in seen_chars:
        print("No es un isograma")
        break
    seen_chars.append(letter)
else:
    print("Es un isograma")
