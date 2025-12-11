# release 1.0.0
from calculator import calculate

print("Калькулятор покраски")
part = input("Деталь: ")
color = input("Цвет: ")

price = calculate(part, color)
print(f"Стоимость: {price} руб.")