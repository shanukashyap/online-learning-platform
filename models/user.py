from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    def login(self):
        print(f"{self.__name} logged in.")

    def logout(self):
        print(f"{self.__name} logged out.")

    @abstractmethod
    def get_role(self):
        pass

    def display_info(self):
        print(
            f"ID: {self.__user_id}, "
            f"Name: {self.__name}, "
            f"Email: {self.__email}, "
            f"Role: {self.get_role()}"
        )