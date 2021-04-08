price = 0
discount = 10
number_of_tickets = int(input("Введите количество билетов: "))
for u in range(1, number_of_tickets+1):
    try:
        age = int(input("Введите возраст посетителя: "))
        if 0 <= age <= 17:
            price = price + 0
        elif 18 <= age <= 24:
            price = price + 990
        elif 25 <= age <= 120:
            price = price + 1390
        else:
            print("введен некорректный возраст, расчет стоимости покупки будет произведен без учета билета с некорректным возрастом")
    except ValueError as e:
        print("ошибка: возраст указывается цифрами, расчет стоимости покупки будет произведен без учета билета с некорректным возрастом")
print(price)
if number_of_tickets > 3:
    price = price-(price*discount/100)
print("общая стоимость покупки: ", int(pricrice)
