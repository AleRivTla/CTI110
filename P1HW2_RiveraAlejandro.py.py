"""
Calculating the total travel budget and expenses for a customer
09/08/2023
CTI 110 P1HW2 - Travel Expenses
Rivera Alejandro

"""


# ask the user for their name
print("Hello, what is your name?")
name = input()

# ask the user for their budget
budget = float(input("What is your current budget? "))

# ask the user where they plan to travel to
print("Where do you plan to travel to,", name, "?")
location = input()

# ask the user how much will be spent on expenses: gas, accommodation, food.
gas = float(input("How much would you spend on gas?"))
accommodation = float(input("How much will you need on accommodations?"))
food = float(input("Finally, how much will you spend on food?"))

# calculate the user's total expenses
total_expenses = gas + accommodation + food

# if the total expenses is over the planned budget, alert the user
if total_expenses > budget:
  print("I'm sorry,", name, "but you are spending more than your budget allows.")

# Dispay results
else:
  print("------Travel Expenses------")
  print("Location:", location)
  print(f"Initial budget: {budget:.2f}")
  print(f"Fuel: {gas:.2f}")
  print(f"Accommodation: {accommodation:.2f}")
  print(f"Food: {food:.2f}")
  print("")
  # subtract total expenses from budget
  print(f"Remaining balance: {budget - total_expenses:.2f}")

