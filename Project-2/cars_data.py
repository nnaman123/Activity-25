# Cars Database - Comprehensive List of Cars with Mileage
# This file contains car data that can be imported into other modules

cars_database = {
    "Toyota Camry": 45000,
    "Honda Civic": 38000,
    "Ford Mustang": 52000,
    "BMW 3 Series": 48000,
    "Mercedes-Benz C-Class": 55000,
    "Audi A4": 50000,
    "Volkswagen Jetta": 42000,
    "Hyundai Elantra": 35000,
    "Mazda3": 41000,
    "Nissan Altima": 44000,
    "Chevrolet Malibu": 39000,
    "Subaru Legacy": 47000,
    "Kia Optima": 36000,
    "Lexus ES 350": 60000,
    "Infiniti Q50": 58000,
    "Volvo S60": 56000,
    "Tesla Model 3": 75000,
    "Prius": 35000,
    "Civic Hybrid": 40000,
    "RAV4": 46000,
}

def get_car_mileage(car_name):
    """Returns the mileage of a car given its name"""
    if car_name in cars_database:
        return cars_database[car_name]
    return None

def list_all_cars():
    """Returns a list of all available cars"""
    return list(cars_database.keys())

def search_car(car_name):
    """Search for a car and return its mileage, case-insensitive"""
    for car, mileage in cars_database.items():
        if car.lower() == car_name.lower():
            return mileage
    return None
