# cinema.py

def calculate_ticket_price(base_price: float, age: int, is_student: bool, is_weekend: bool) -> float:
    """
    Расчёт стоимости билета в кино.

    Бизнес-правила:
    1. Если base_price < 0 или age < 0 — ValueError.
    2. Если age < 6 — бесплатно.
    3. Если age < 18 — детский тариф: 50% от base_price.
    4. Если age >= 65 — пенсионный тариф: 30% от base_price.
    5. Иначе — полная цена.
    6. Если is_student=True и age >= 18 — скидка 20%.
    7. Если is_weekend=True — наценка 15%.
    8. Минимальная цена — 100 руб (кроме бесплатных).
    9. Максимальная цена — 1500 руб.
    """
    if base_price < 0:
        raise ValueError("base_price must be >= 0")
    if age < 0:
        raise ValueError("age must be >= 0")

    if age < 6:
        return 0.0

    if age < 18:
        price = base_price * 0.5
    elif age >= 65:
        price = base_price * 0.3
    else:
        price = base_price

    if is_student and age >= 18:
        price *= 0.8

    if is_weekend:
        price *= 1.15

    if price < 100:
        price = 100.0

    if price > 1500:
        price = 1500.0

    return round(price, 2)
