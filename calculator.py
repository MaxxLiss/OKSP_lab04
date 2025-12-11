from config import BASE_PRICE, COLORS, PARTS

def calculate(part, color):
    if part not in PARTS:
        return "Ошибка детали"
    if color not in COLORS:
        return "Ошибка цвета"
    return BASE_PRICE * PARTS[part] * COLORS[color]