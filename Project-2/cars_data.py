# Cars Database - Fetches car data from external JSON file
# This module imports and manages car data from cars_list.json

import json
import os

def load_cars_database():
    """
    Load car data from external JSON file (cars_list.json)
    Returns a dictionary of cars with their mileage
    """
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(current_dir, 'cars_list.json')
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data.get('cars', {})
    except FileNotFoundError:
        print(f"Error: {json_file} not found!")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {json_file} is not valid JSON!")
        return {}

# Load the cars database from external JSON file
cars_database = load_cars_database()

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
