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
print(f"{blu.name} is {blu.age} years old and is a {blu.species}.")
print(f"{woo.name} is {woo.age} years old and is a {woo.species}.")
