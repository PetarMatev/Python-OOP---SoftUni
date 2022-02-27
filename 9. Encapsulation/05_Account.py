# 05. Account:

class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    # self validating code.
    def __is_pin_valid(self, pin):
        return self.__pin == pin

    def get_id(self, pin):
        if self.__is_pin_valid(pin):
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if self.__is_pin_valid(old_pin):
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(1234, 44, 4444)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 1234))
print(account.change_pin(3421, 1234))
