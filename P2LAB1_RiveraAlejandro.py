"""
CTI 110
P2LAB1 - Gas Prices
Rivera Alejandro
09/07/2023

Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f} {your_value2:.2f} {your_value3:.2f}')

"""
# ask for miles per gallin
miles_per_gallon = float(input("What is the car's MPG? "))
# ask for the price per gallon of gas
price_per_gallon = float(input("Pricer per gallon? "))

# show the price per mile to drive
# unit we want is $/miles
price_per_mile = price_per_gallon / miles_per_gallon
#print("This vehicle costs $", price_per_mile, "to drive 1 mile.")
# f strings are like this: {variable:.2f} for 2 decimal points
print(f"This vehicle costs ${price_per_mile:.2f} to drive 1 mile.")

# formatting
print("""


""")

# Last step: Tell the user the cost to drive 20, 75, and 500 miles

# price of 20 miles
print(f"The price to drive 20 miles is ${price_per_mile * 20:.2f}")
# price of 75 miles
print(f"The price to drive 75 miles is ${price_per_mile * 75:.2f}")
# price of 500 miles
print(f"The price to drive 500 miles is ${price_per_mile * 500:.2f}")

