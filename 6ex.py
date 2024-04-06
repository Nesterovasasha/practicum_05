def count_repeats(smiles):
    count = 0
    for i in range(len(smiles)-2):
        if smiles[i] == smiles[i+1] == smiles[i+2]:
            count += 1
    return count

smiles = []
for i in range(3):
    num = int(input(f"Введите количество подданных, видевших улыбку волшебницы в {i+1} день: "))
    smiles.append(num)

repeats = count_repeats(smiles)
print(f"Количество повторений: {repeats}")