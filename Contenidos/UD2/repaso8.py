str1 = "0001010011101"
str2 = "0000110010001"
diff_char = 0
comando = 1

while True:
    if comando == 1:
        for char1 in str1:
            for char2 in str2:
                if char1 != char2:
                    diff_char +=1
                    comando -=1
                    print(diff_char)
    else:
        comando +=1





    
            