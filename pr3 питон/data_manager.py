import json
import os
from user import User
from currency import Currency

class DataManager:
    def __init__(self):
        self.users = []
        self.currencies = []
        self.basket = []

        self.users_file = os.path.join(os.path.expanduser("~"), "Desktop", "users.json")
        self.currencies_file = os.path.join(os.path.expanduser("~"), "Desktop", "currencies.json")
        self.basket_file = os.path.join(os.path.expanduser("~"), "Desktop", "basket.json")

        self.load_users()
        self.load_currencies()
        self.load_basket()

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                users_data = json.load(file)
                self.users = [User(user['login'], user['password']) for user in users_data]
        except FileNotFoundError:
            self.users = []

    def save_currencies(self):
        with open(self.currencies_file, 'w') as file:
            json.dump([currency.to_dict() for currency in self.currencies], file, indent=4)

    def load_currencies(self):
        try:
            with open(self.currencies_file, 'r') as file:
                currencies_data = json.load(file)
                self.currencies = [Currency(currency['название'], currency['цена']) for currency in currencies_data]
        except FileNotFoundError:
            self.currencies = []

    def save_basket(self):
        with open(self.basket_file, 'w') as file:
            json.dump(self.basket, file, indent=4)

    def load_basket(self):
        try:
            with open(self.basket_file, 'r') as file:
                self.basket = json.load(file)
        except FileNotFoundError:
            self.basket = []

    def add_user(self, user):
        self.users.append(user)
        self.save_users()

    def find_user(self, login):
        return next((user for user in self.users if user.login == login), None)

    def filter_currencies(self, price_limit):
        return [currency for currency in self.currencies if currency.price > price_limit]