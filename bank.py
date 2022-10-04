import uuid


class Account:
    def __init__(self,initial_balance=0):
        self.balance=initial_balance
        self.identifier=self._create_identifier()

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance-amount<0:
            raise ValueError(f"No money enough in {self.identifier}")
        self.balance-=amount

    @staticmethod
    def _create_identifier():
        return str(uuid.uuid4())


a=Account(50)
print(a.identifier)
a.deposit(60)

