import hashlib

class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.__password = None

    def set_password(self, new_password):
        self.__password = hashlib.sha256(new_password.encode()).hexdigest()

    def check_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

user = UserAccount("user1", "kotcobaka@gmail.com")

user.set_password("my_secure_password")

print(user.check_password("my_secure_password"))
print(user.check_password("wrong_password"))


