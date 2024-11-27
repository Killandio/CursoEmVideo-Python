# Read the temperature in Celsius
celsius = float(input("Digite a temperatura em °C: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the results
print(f"{celsius:.1f}°C equivalem a {fahrenheit:.1f}°F.")

# Read the temperature in Fahrenheit
fahrenheit = float(input("Digite a temperatura em °F: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Display the results
print(f"{fahrenheit:.1f}°F equivalem a {celsius:.1f}°C.")
