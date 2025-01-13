# Conversion factors for temperature conversion
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


    try:
        temp = float(input("Enter the temperature: "))
        scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if scale == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {converted_temp:.2f}°F.")
        elif scale == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C.")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
