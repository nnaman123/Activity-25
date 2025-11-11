#Create Class
class Parrot:

    #Class Attribute
    species = "Bird"

    #instance attributes
    def __init__(self ,name, age):
        self.name = name
        self.age = age

#Instantiate The Parrot Class
blu = Parrot("Blu" ,10)
woo = Parrot("Woo" ,15)

#Access The Class Attributes
print("Blu is a {}".format(blu.name ,blu.age))
print("Woo is also a {}".format(woo.name ,blu.age))
