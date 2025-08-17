class savings:
    money=0
    interest=0
    r=0.03
    def deposit(self,saving):
        savings.money+=saving
        savings.interest=savings.money*savings.r
        savings.money+=savings.interest
    def withdraw(self,amount):
        savings.money=savings.money-amount
    def check(self):
        print(f"Amount = {savings.money}")
a=savings()
a.deposit(1000)
a.check()
a.withdraw(500)
a.check()