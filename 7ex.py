def min_stations_to_travel(N, K, M):
    clockwise_distance = abs(K - M) - 1
    anticlockwise_distance = N - clockwise_distance - 2
    return min(clockwise_distance, anticlockwise_distance)

N, K, M = map(int, input("Введите через пробел число станций N, номер станции К, номер станции М: ").split())
min_stations = min_stations_to_travel(N, K, M)
print(f"Артему нужно проехать минимум {min_stations} станций.")