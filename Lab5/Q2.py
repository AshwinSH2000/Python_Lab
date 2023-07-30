class Vehicle:
    def __init__(self):
        self.owner = ""
        self.regno = ""
        self.mfg_er = ""
        
    
class Passenger(Vehicle):
    def __init__(self):
        self.pasgs = 0
    def input(self):
        self.owner = input("Enter the name of the owner:")
        self.regno = input("Enter th vehicle registration number:")
        self.mfg_er = input("Enter the manufacturer of the vehicle:")
        self.pasgs = input("Enter the max no of passengers allowed:")

    def output(self, i):
        print("\nVehicle {} details are as follows:".format(i))
        print("Owner name: {}".format(self.owner))
        print("Registration number:",self.regno)
        print("Manufacturing company:",self.mfg_er)
        print("Max passengers allowed:", self.pasgs)


n = int(input("How many vehicles:"))
for i in range(n):
    print("Vehicle ",i+1)
    reg = Passenger()
    reg.input()

for i in range(n):
    reg.output(i+1)



    
        
