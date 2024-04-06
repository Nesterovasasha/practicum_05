def convert_knuts_to_galleons(knuts):
    galleons = knuts // (17*29)
    remaining_knuts = knuts % (17*29)
    sickles = remaining_knuts // 29
    remaining_knuts %= 29

    result = ""
    if galleons > 0:
        result += f"{galleons} галлеонов "
    if sickles > 0:
        result += f"{sickles} сиклей "
    if remaining_knuts > 0:
        result += f"{remaining_knuts} кнатов"

    return result

knuts = int(input("Введите количество кнатов: "))
result = convert_knuts_to_galleons(knuts)
print(result)