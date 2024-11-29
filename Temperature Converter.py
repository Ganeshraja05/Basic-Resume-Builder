def convert_temperature(temperature, unit):
    if unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        converted = (temperature - 32) * 5 / 9
        return round(converted, 2)
    elif unit.upper() == 'C':
        # Convert Celsius to Fahrenheit
        converted = (temperature * 9 / 5) + 32
        return round(converted, 2)
    else:
        raise ValueError("Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius.")

# Get input from the user
try:
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Enter the unit of the input temperature ('F' for Fahrenheit, 'C' for Celsius): ")
    
    converted_temp = convert_temperature(temp, unit)
    print(f"The converted temperature is: {converted_temp}°{'C' if unit.upper() == 'F' else 'F'}")
except ValueError as e:
    print(e)