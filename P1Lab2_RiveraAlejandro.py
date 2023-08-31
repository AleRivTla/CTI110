"""
CTI110
P1LAB2 - Sales
Rivera Alejandro
8/31
Simple point of sakes program.

"""
# Set Up Our Store
store_name = "CTI 110 Hut"
product = "shoes"
stock = 20
price = 49.99

# Greet Customer
print("Welcome to", store_name, ".")
print("What's your name?")
customer_name = input()
print("Nice to meet you,", customer_name,)

# Explain Product

print("Our special today is:", product)
print() #blank line
print("On sale for: $", price)
print("Only", stock, "left!")

# Take Order
print("How many", product, "would you like?")
# Input Gives Us A String
#order = input()
# Convert It To A Number
#order = int(order)

# or....
order = int(input())

# Finish Up
# optional
if (order > stock):
  order = stock
  print("Sorry, we can only sell you", order)


total_price = order * price
print("So you would like")
print(order, product, "for a total of $", total_price)
print("<y,n>", sep = "")
confirm = input()
if (confirm == "y"):
  print("Shipped!")
else:
  print("Order cancelled")
  
print("Thanks for shopping with", store_name, ".")


