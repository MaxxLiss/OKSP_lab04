# release 0.0.1
from calculator import calculate

print("Калькулятор покраски")
part = input("Деталь: ")
color = input("Цвет: ")

price = calculate(part, color)
print(f"Стоимость: {price} руб.")