'''
PSEUDOCODE

Step 1. : Request the celsius value of temperature from user and store in a variable
Step 2. : Multiply the value above with (9/5)
Step 3. : Add the result of the above to 32
Step 4: : Store Value as a variable
Step 5. : Print result

CONVERTER = 9/5
CELSIUS_CONSTANT = 32

temperature_in_celsius = float(input('Enter the temperature in Celsius: '))

temperature_in_fahrenheit = (CONVERTER * temperature_in_celsius) + CELSIUS_CONSTANT

print ("The value of ", temperature_in_celsius, "degree Celsius is ", round(temperature_in_fahrenheit, 2))