# Sales Prediction
# 8/31/2018
# CTI-110 P2T1- Sales Prediction
# Matthew Estes
#

# A company has determined that its annual profit is typically 23 percent of 
# total sales. Write a program that asks the user to enter the projected amount
# of total sales, and then displays the profit that will be made from that
# amount.

# Pseudocode
# 1. Ask user to enter total amount of sales
# 2. Create a formula for dividing total sales by 0.23
# 3. Display the result

# User enters total amount of projected sales.
projectedTotalSales = float(input("Please enter projected amount" + \
                                    "of total sales: " ))
# Create variable and formula for figuring out total profit.
profit = 0.23 * projectedTotalSales

print(profit)








