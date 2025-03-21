class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def to_dict(self):
        return {"login": self.login, "password": self.password}