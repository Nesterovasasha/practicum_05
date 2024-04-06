def sklonenie(number):
    if number == 1:
        return "попугай"
    elif 2 <= number <= 4:
        return "попугая"
    else:
        return "попугаев"

number = int(input("Введите число от 1 до 100: "))
if 1 <= number <= 100:
    print(f"У вас {number} {sklonenie(number)}")
else:
    print("Число должно быть от 1 до 100.")
