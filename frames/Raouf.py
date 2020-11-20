class ATM:
    def __init__(self , balance , bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def Bank_name(self):
        print(self.bank_name)

    def Money_bills(self,request):
        self.withdrawals_list.append(request)
        self.balance -= request
        notes = [100, 50, 10, 5, 2, 1]
        for note in notes:
            if request >= note:
                request -= note
                print("give ", note)

    def withdraw(self, request):
        self.Bank_name()
        result = self.balance
        if request > self.balance:
            print("There is no enough money in ATM ")
        elif request <= 0:
            print("your request shouldn't be a negative number ")
        else:
            result = self.balance - request
            self.Money_bills(request)
        return result

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)


atm1 = ATM(600, "BANK_1")
atm2 = ATM(400, "BANK_2")

atm1.balance = atm1.withdraw(300)
atm2.balance = atm2.withdraw(200)

print("New ATM Balance is :", atm1.balance)
print("New ATM Balance is :", atm2.balance)