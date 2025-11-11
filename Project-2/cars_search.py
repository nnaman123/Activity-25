# Car Search Program
# This program imports car data and allows users to search for cars by name
# It displays the mileage of the requested car

from cars_data import cars_database, search_car, list_all_cars

def display_welcome():
    """Display welcome message and instructions"""
    print("=" * 50)
    print("Welcome to the Car Mileage Search System!")
    print("=" * 50)
    print("Search for any car in our database to find its mileage.")
    print()

def display_all_cars():
    """Display all available cars in the database"""
    print("\nAvailable Cars in Database:")
    print("-" * 50)
    cars = list_all_cars()
    for i, car in enumerate(cars, 1):
        mileage = cars_database[car]
        print(f"{i}. {car}: {mileage} miles")
    print()

def search_and_display():
    """Main search function - allows user to search for cars"""
    while True:
        car_name = input("\nEnter car name to search (or 'list' to see all, 'quit' to exit): ").strip()
        
        if car_name.lower() == 'quit':
            print("Thank you for using the Car Mileage Search System!")
            break
        
        if car_name.lower() == 'list':
            display_all_cars()
            continue
        
        if not car_name:
            print("Please enter a valid car name.")
            continue
        
        mileage = search_car(car_name)
        
        if mileage is not None:
            print(f"\n✓ Found! {car_name.title()} has {mileage} miles")
        else:
            print(f"\n✗ Car '{car_name}' not found in database.")
            print("Type 'list' to see all available cars.")

if __name__ == "__main__":
    display_welcome()
    display_all_cars()
    search_and_display()
