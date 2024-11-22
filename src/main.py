import time
import os

def clear_screen():
    """
    Clears the terminal screen for a cleaner display.
    Works on Windows, macOS, and Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    """
    Displays the title of the application
    """
    clear_screen()
    print("######################################")
    print("#            BIOTRACKER             #")
    print("######################################")
    time.sleep(1)

def display_menu():
    """
    Displays the main menu options.
    """
    clear_screen()
    print("######################################")
    print("#            BIOTRACKER             #")
    print("######################################")
    print("\nChoose an option to measure:")
    print("1. CO2 Level")
    print("2. Methane Level")
    print("3. Moisture Level")
    print("4. pH Level")
    print("5. O2 Level")
    print("0. Exit")
    print("\n")

def handle_selection(selection):
    """
    Handles the user's menu selection.
    """
    if selection == "1":
        print("\nMeasuring CO2 Level...")
        # Call the CO2 sensor function
        measure_co2()
    elif selection == "2":
        print("\nMeasuring Methane Level...")
        # Call the Methane sensor function
        measure_methane()
    elif selection == "3":
        print("\nMeasuring Moisture Level...")
        # Call the Moisture sensor function
        measure_moisture()
    elif selection == "4":
        print("\nMeasuring pH Level...")
        # Call the pH sensor function
        measure_ph()
    elif selection == "5":
        print("\nMeasuring O2 Level...")
        # Call the O2 sensor function
        measure_o2()
    elif selection == "0":
        print("\nExiting Biotracker. Goodbye!")
        time.sleep(1)
        exit(0)
    else:
        print("\nInvalid option! Please choose a valid option.")

# Placeholder functions for sensors (to be replaced with actual imports later)
def measure_co2():
    print("Simulating CO2 measurement...")
    time.sleep(1)

def measure_methane():
    print("Simulating Methane measurement...")
    time.sleep(1)

def measure_moisture():
    print("Simulating Moisture measurement...")
    time.sleep(1)

def measure_ph():
    print("Simulating pH measurement...")
    time.sleep(1)

def measure_o2():
    print("Simulating O2 measurement...")
    time.sleep(1)

# Main program flow
if __name__ == "__main__":
    display_title()
    while True:
        display_menu()
        user_input = input("Enter your choice: ")
        handle_selection(user_input)
        input("\nPress Enter to return to the menu...")
