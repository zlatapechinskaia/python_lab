seat_number = int(input("Введите номер места: "))

if 1 <= seat_number <= 36:
    side = "Боковое" if seat_number % 2 == 0 else "Купе"
    place = "нижнее"
elif 37 <= seat_number <= 81:
    side = "Боковое" if seat_number % 2 == 0 else "Купе"
    place = "верхнее"
else:
    print("Места с таким номером нет в плацкартном вагоне")
    exit()
print(f"Место {side, place}")