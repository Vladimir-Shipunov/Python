from data_manager import DataManager
from currency import Currency
from basket import Basket
from user import User

class Exchange:
    def __init__(self):
        self.data_manager = DataManager()
        self.basket = Basket(self.data_manager)

    def display_currencies(self):
        for currency in self.data_manager.currencies:
            print(f"{currency.name}: {currency.price}")

    def add_currency(self, name, price):
        self.data_manager.currencies.append(Currency(name, price))
        self.data_manager.save_currencies()

    def update_currency(self, index, name, price):
        if 0 <= index < len(self.data_manager.currencies):
            self.data_manager.currencies[index] = Currency(name, price)
            self.data_manager.save_currencies()

    def delete_currency(self, index):
        if 0 <= index < len(self.data_manager.currencies):
            self.data_manager.currencies.pop(index)
            self.data_manager.save_currencies()

    def register_user(self):
        print("Регистрация нового пользователя")
        login = input("Введите логин: ")
        if self.data_manager.find_user(login):
            print("Пользователь с таким логином уже существует.")
            return
        password = input("Введите пароль: ")
        new_user = User(login, password)
        self.data_manager.add_user(new_user)
        print("Пользователь успешно зарегистрирован.")

    def login_user(self):
        print("Авторизация пользователя")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        user = self.data_manager.find_user(login)
        if user and user.password == password:
            print(f"Добро пожаловать, {user.login}!")
            return user
        else:
            print("Неверный логин или пароль.")
            return None

    def run(self):
        main = 1
        while main == 1:
            try:
                print('Добро пожаловать на биржу BYBIT')
                print('Выберите от какого имени вы будете использовать биржу: 1.админ. 2.пользователь.')
                a = int(input())

                if a < 1 or a > 2:
                    print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
                else:
                    if a == 1:
                        print(f"Ваш выбор: admin")
                        self.admin_menu()
                    elif a == 2:
                        print(f"Ваш выбор: пользователь")
                        while True:
                            print("1. Регистрация")
                            print("2. Авторизация")
                            print("3. Вернуться назад")
                            choice = input("Выберите действие: ")
                            if choice == '1':
                                self.register_user()
                            elif choice == '2':
                                user = self.login_user()
                                if user:
                                    self.user_menu(user)
                            elif choice == '3':
                                break
                            else:
                                print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
            except ValueError:
                print("Вы должны ввести число")

    def admin_menu(self):
        print('Введите логин администратора биржи')
        login = input()
        print('Введите пароль администратора биржи')
        password = input()

        if login == "admin" and password == "123":
            print('Добро пожаловать на биржу, администратор')
            while True:
                print('Что вы хотите сделать?')
                print('1.Показать валюты')
                print('2.Добавить валюту')
                print('3.Изменить валюту')
                print('4.Удалить валюту')
                print('5.Фильтровать валюты по цене')
                print('6.Выйти')
                choice = input()
                if choice == '1':
                    self.display_currencies()
                elif choice == '2':
                    name = input("Введите название валюты: ")
                    price = float(input("Введите цену валюты: "))
                    self.add_currency(name, price)
                elif choice == '3':
                    index = int(input("Введите номер валюты для изменения: ")) - 1
                    name = input("Введите новое название валюты: ")
                    price = float(input("Введите новую цену валюты: "))
                    self.update_currency(index, name, price)
                elif choice == '4':
                    index = int(input("Введите номер валюты для удаления: ")) - 1
                    self.delete_currency(index)
                elif choice == '5':
                    price_limit = float(input("Введите минимальную цену для фильтрации валют: "))
                    filtered = self.data_manager.filter_currencies(price_limit)
                    if filtered:
                        for currency in filtered:
                            print(f"{currency.name}: {currency.price}")
                    else:
                        print("Нет валют, соответствующих критериям.")
                elif choice == '6':
                    break
                else:
                    print("Неверный выбор.")
        else:
            print('Неверный логин или пароль')

    def user_menu(self, user):
        print(f'Добро пожаловать на биржу, {user.login}')
        while True:
            print('Что вы хотите сделать?')
            print('1.Купить валюту')
            print('2.Продать валюту')
            print('3.Перевести')
            print('4.Выйти')
            print('5.Просмотр валюты')
            print('6.Показать корзину')
            choice = input()
            if choice == '1':
                self.display_currencies()
                name = input("Введите название валюты для покупки: ")
                currency = next((c for c in self.data_manager.currencies if c.name == name), None)
                if currency:
                    self.basket.add_item(currency.name, currency.price)
                    print(f"Валюта {currency.name} добавлена в корзину по цене {currency.price}.")
                else:
                    print("Валюта не найдена.")
            elif choice == '2':
                index = int(input("Введите номер валюты для продажи: ")) - 1
                self.basket.remove_item(index)
                print("Валюта удалена.")
            elif choice == '3':
                print('Перевод валюты')
            elif choice == '4':
                break
            elif choice == '5':
                self.display_currencies()
            elif choice == '6':
                for item in self.basket.to_dict():
                    print(f"{item['item']}: {item['price']}")
            else:
                print("Неверный выбор.")