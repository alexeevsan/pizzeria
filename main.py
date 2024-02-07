from abc import ABC, abstractmethod


class Pizza:
    def __init__(self, name, size, ingredients):
        self.name = name
        self.size = size
        self.ingredients = ingredients

    def __str__(self):
        ing = '' if len(self.ingredients) == 0 else ', '.join(self.ingredients)
        return f'Название: {self.name}\nРазмер: {self.size} см\nИнгридиенты: {ing}'


class Order:
    def __init__(self, pizza, ingredients):
        self.pizza = pizza
        self.ingredients = ingredients

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def show_prise(self):
        price = self.pizza.size * 10 + len(self.pizza.ingredients) * 50 + len(self.ingredients) * 50
        return price

    def __str__(self):
        ing = '' if len(self.ingredients) == 0 else ', '.join(self.ingredients)
        return f'\n#-----------------------------\nВаш заказ:\n{self.pizza}\nДоп. ингридиент: {ing}\nСтоимость: {self.show_prise()}\n#-----------------------------'


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class PayCash(Payment):
    def pay(self, price):
        return f'\nОплата наличными: {price}'

    def __str__(self):
        return f'Оплата наличными'

class PayCard(Payment):
    def pay(self, price):
        return f'\nОплата картой: {price}'

    def __str__(self):
        return f'Оплата картой'


pizza1 = Pizza('Пепперони', 30, ['пепперони', 'моцарелла'])
pizza2 = Pizza('Цыпленок Барбекю', 35, ['лук', 'бекон', 'соус Барбекю'])
pizza3 = Pizza('Четыре Сыра', 30, ['сыр', 'томатный соус', 'орегано'])
pizza4 = Pizza('Мексиканская', 40, ['моцарелла', 'шампиньоны', 'перец', 'томат'])
pizza5 = Pizza('Маргарита', 23, ['моцарелла', 'томат', 'орегано'])

pizzas = {1: pizza1, 2: pizza2, 3: pizza3, 4: pizza4, 5: pizza5}
toppings = {1: 'сладкий лук', 2: 'халапеньо', 3: 'чили', 4: 'соленный огурец', 5: 'оливки'}
payments = {1: PayCard(), 2: PayCash()}


def show_pizzas(pizzas_dct: dict):
    for el in pizzas_dct.keys():
        print(f'\nНомер: {el}\n{pizzas_dct[el]}')


def show_toppings(toppings_dct: dict):
    for el in toppings_dct.keys():
        print(f'{el}: {toppings_dct[el]}')


def show_payment(payments_dct: dict):
    for el in payments_dct.keys():
        print(f'{el}: {payments_dct[el]}')


def select_pizza() -> Order:
    while True:
        try:
            number_pizza = int(input('\nДля заказа введите номер пиццы: '))
            if 0 < number_pizza < len(toppings) + 1:
                selected_pizza = Order(pizzas[number_pizza], [])
                print(selected_pizza)
                return selected_pizza
            else:
                print('Неверный ввод')
        except ValueError:
            print('Неверный ввод')


def add_toppings(selected_pizza: Order):
    while True:
        try:
            number_topping = int(input('Введите номер топпинга: (0 - выход) '))
            if number_topping == 0:
                break
            if 0 < number_topping < len(toppings) + 1:
                selected_pizza.ingredients.append(toppings[number_topping])
                print(f'Ингредиент "{toppings[number_topping]}" добавлен')
            else:
                print('Неверный ввод')
        except ValueError:
            print('Неверный ввод')


def select_pay():
    print('\nВыберите способ оплаты: ')
    show_payment(payments)
    while True:
        try:
            number_payment = int(input('\nСпособ оплаты: '))
            if 0 < number_payment < len(payments) + 1:
                return payments[number_payment]
            else:
                print('Неверный ввод')
        except ValueError:
            print('Неверный ввод')


# ----------------------------------------

print('Выберите вашу пиццу: ')
show_pizzas(pizzas)
order = select_pizza()

try:
    t = int(input('\nДобавить топпинги: (1 - да, anykey - нет) '))
    if t == 1:
        show_toppings(toppings)
        add_toppings(order)
except ValueError:
    pass

print(order)
pay = select_pay()
print(pay.pay(order.show_prise()))