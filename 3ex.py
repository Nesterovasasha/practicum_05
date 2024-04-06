number = input("Введите четырехзначное число: ")

reversed_number = ''.join(reversed(number))
if reversed_number == number:
    print("Настоящее число")
else:
    print("Кривое число")