class Plane:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
class Cargo(Plane):
    def takeoff(self):
        print("cargo is take off")
    def land(self):
        print("cargo is land")
    def fly(self):
        print("cargo is fly")
class Passenger(Plane):
    def takeoff(self):
        print("Passenger is take off")
    def land(self):
        print("Passenger is land")
    def fly(self):
        print("Passenger is fly")
c=Cargo()
p=Passenger()
def allowPlane(ref):
    ref.takeoff()
    ref.land()
    ref.fly()
allowPlane(c)
allowPlane(p)
print("=======================")
class Cargo:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
    def carry(self):
        print("plane carry cargo")
class Passenger:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
    def carry(self):
        print("plane carry passenger")
class Fighter:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
    def carry(self):
        print("plane carry weapons ")
c=Cargo()
p=Passenger()
f=Fighter()
def allowPlane(ref):
    ref.takeoff()
    ref.land()
    ref.fly()
    ref.carry
allowPlane(c)
allowPlane(p)
allowPlane(f)
print("=======================")
class Plane:
    def takeoff(self):
        print("plane is take off")
    def land(self):
        print("plane is land")
    def fly(self):
        print("plane is fly")
class Cargo(Plane):
    def takeoff(self):
        print("cargo is take off")
    def land(self):
        print("cargo is land")
    def fly(self):
        print("cargo is fly")
class Passenger(Plane):
    def takeoff(self):
        print("Passenger is take off")
    def land(self):
        print("Passenger is land")
    def fly(self):
        print("Passenger is fly")
c=Cargo()
p=Passenger()
c.takeoff()
c.land()
c.fly()
p.takeoff()
p.land()
p.fly()