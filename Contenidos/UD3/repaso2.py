entry = ["this", "is", "a", "real", "real", "real", "story"]
corrected_list = []

for char in entry:
    if char not in corrected_list:
        corrected_list.append(char)
print(corrected_list)