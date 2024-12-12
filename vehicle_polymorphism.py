from abc import ABC,abstractmethod

class BMW:
    def engine(self):
        print("The BMW works with a V6 engine")
    
    def max_speed(self):
        print("The BMW has a maximum speed of 300 Km/h")

class Ferrari:
    def engine(self):
        print("The Ferrari works with a V12 turbo engine")
    
    def max_speed(self):
        print("The Ferrari has a maximum speed of 375 Km/h")

obj_BMW = BMW()
obj_Ferrari = Ferrari()

for vehicle in (obj_BMW, obj_Ferrari):
    vehicle.engine()
    vehicle.max_speed()