#no parameter and without return value
class Calculator:
    def __init__(self):
        self.brand = "casio"
        self.cost = 200
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
        
c1=Calculator()
print(c1.brand)
print(c1.cost)
c1.add()


#no parameter and with return value
class Calculator:
    def __init__(self):
        self.brand = "casio"
        self.cost = 200
    def add(self):
        a=10
        b=20
        c=a+b
        return c
c1=Calculator()
print(c1.brand)
print(c1.cost)
result = c1.add()
print(result)