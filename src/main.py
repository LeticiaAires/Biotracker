import time
from src.hardware.sen0159 import SEN0159  # CO2 sensor handler
from src.hardware.adc_handler import DFR0553  # ADC handler
# Add imports for other sensors when implemented

def show_title():
    """Displays the title of the application."""
    print("\n" + "=" * 30)
    print("Welcome to BioTracker")
    print("=" * 30)
    time.sleep(1)

def show_menu():
    """Displays the main menu options."""
    print("\nMain Menu:")
    print("1. Measure CO2")
    print("2. Measure Methane")
    print("3. Measure Moisture")
    print("4. Measure pH")
    print("5. Measure O2")
    print("6. Exit")

def measure_co2(adc):
    """Handles the CO2 measurement process."""
    sensor = SEN0159(adc, channel=0)  # Assuming CO2 sensor is on channel 0
    co2_level = sensor.read_co2_level()
    print(f"\nCO2 Level: {co2_level:.2f} ppm")

def main():
    """Main function for handling user input."""
    # Initialize the ADC
    adc = DFR0553()

    try:
        show_title()

        while True:
            show_menu()
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == "1":
                measure_co2(adc)
            elif choice == "2":
                print("\nMethane measurement function is not implemented yet.")
            elif choice == "3":
                print("\nMoisture measurement function is not implemented yet.")
            elif choice == "4":
                print("\npH measurement function is not implemented yet.")
            elif choice == "5":
                print("\nO2 measurement function is not implemented yet.")
            elif choice == "6":
                print("\nExiting BioTracker. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
            time.sleep(1)  # Pause before showing the menu again
    finally:
        adc.close()

if __name__ == "__main__":
    main()
