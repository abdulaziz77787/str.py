from datetime import datetime


class BankAccount:

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0.0

    def _get_timestamp(self):
        now = datetime.now()
        period = "am" if now.strftime("%p") == "AM" else "pm"
        return now.strftime(f"%Y/%m/%d، الساعة %I:%M{period}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(
                f"تم إيداع {amount} ريال لرصيدك البنكي في {self._get_timestamp()}."
            )

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(
                f"تم خصم {amount} ريال من رصيدك البنكي في {self._get_timestamp()}."
            )
        elif amount > self.balance:
            print("الرصيد غير كافٍ لإتمام العملية.")

    def check_balance(self):
        print(f"رصيدك الحالي: {self.balance} ريال")


# Example Usage:
account = BankAccount("Aziz")
account.deposit(2000)
account.withdraw(150)
account.check_balance()
