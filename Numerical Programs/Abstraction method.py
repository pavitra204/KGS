from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def transaction(self):
        pass
class credit(Payment):
    def transaction(self):
        print("credit is done")
class debit(Payment):
    def transaction(self):
        print("debit is done")
class upi(Payment):
    def transaction(self):
        print("upi is done")
        
p=Payment()
c=credit()
d=debit()
u=upi()
p.transaction()
c.transaction()
d.transaction()
u.transaction()
