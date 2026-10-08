from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def payment_summary(self):
        print(f"Payment Amount: ₹{self.amount}")


class UPIPayment(Payment):
    def pay(self):
        print(f"Paid ₹{self.amount} using UPI")


class CardPayment(Payment):
    def pay(self):
        print(f"Paid ₹{self.amount} using Credit/Debit Card")


class NetBankingPayment(Payment):
    def pay(self):
        print(f"Paid ₹{self.amount} using Net Banking")