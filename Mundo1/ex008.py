# Read a value in meters and convert it to centimeters and millimeters.
# Display the converted values.


metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000


print(f"{metros} metros correspondem a {centimetros:.0f} centímetros e {milimetros:.0f} milímetros.")
