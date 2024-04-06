pin = input("Введите четырехзначный PIN-код: ")

if len(pin) != 4 or not pin.isdigit():
    print("ERROR")
else:
    if len(set(pin)) == 4 and int(pin) not in range(1900, 2051):
        print("OK")
    else:
        print("ERROR")