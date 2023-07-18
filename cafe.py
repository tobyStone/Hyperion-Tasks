'''
based on learning from Hyperion.dev
first compulsory task set in T12
A program to loop through the stock items and prices
of those stock items (both of which are stored in separate
dictionaries) and calculate the overall cost
of the stock in a cafe.
'''

#a list setting up the items to be iterated through
menu = ["biscuits", "parsnips", "Jaffa-cakes", "Red Pepper"]

#a dictionary of the number of each item in stock
stock = {"biscuits": 5, 
         "parsnips": 3, 
         "Jaffa-cakes": 4, 
         "Red Pepper": 2}

#a dictionary of the price of each item in stock
price = {"biscuits": 3.00, 
         "parsnips": 1.20, 
         "Jaffa-cakes": 2.50, 
         "Red Pepper": 1.50}

#a variable to be used to total the cost of stock
total_stock = 0.0

#a loop which multiples the number of items in stock
#by the cost of each item, producing a total cost
for items in menu:
    total_stock += (stock[items] * price[items])

print("The total_stock value is: ", total_stock)