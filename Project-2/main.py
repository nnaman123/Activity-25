#create Class
class Vehicle:
    #create init method
    def __init__(self ,max_speed, mileage):
        #Bind The Arguments
        self.max_speed = max_speed
        self.mileage = mileage

#Create Object
ModelX = Vehicle(240, 18)
#Accessing Object Properties
print("ModelX Speed:", ModelX.max_speed)
print("ModelX Mileage:", ModelX.mileage)