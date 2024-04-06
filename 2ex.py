import math

def check_point_in_circle(center_x, center_y, radius, point_x, point_y):
    distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)

    if distance < radius:
        return "Точка находится внутри окружности"
    elif distance == radius:
        return "Точка лежит на окружности"
    else:
        return "Точка находится за пределами окружности"


center_x = float(input("Введите координату центра окружности по оси X: "))
center_y = float(input("Введите координату центра окружности по оси Y: "))
radius = float(input("Введите радиус окружности: "))

point_x = float(input("Введите координату точки по оси X: "))
point_y = float(input("Введите координату точки по оси Y: "))

result = check_point_in_circle(center_x, center_y, radius, point_x, point_y)
print(result)