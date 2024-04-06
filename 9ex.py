heights = input("Введите высоты трех башен через пробел: ").split()

max_height = max(heights)
min_height = min(heights)

for height in heights:
    if height != max_height and height != min_height:
        middle_height = height

print(max_height, middle_height, min_height)