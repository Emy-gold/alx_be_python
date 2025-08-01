FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsuis(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit:.1f}°F is {celsius}")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) +32
    print(f"{celsius:.1f}°C is {fahrenheit}")

def main():
    temperature = int(input("Enter the temperature to convert: "))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if temperature_type == "C":
        return convert_to_celsuis(temperature)
    elif temperature_type == "F":
        return convert_to_fahrenheit(temperature)
    else :
        print("Invalid temperature. Please enter a numeric value.")
    
if __name__ == "__main__":
    main()