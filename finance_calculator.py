"""
based on learning from Hyperion.dev
Capstone Project task set in T05
This program is a finance calculator for returning capital amounts for investment
or for working out monthly repayments on a bond/mortgage.
In the investments there are three choices of interest returns:
simple, compound or, with investment in stocks and shares, random returns.
In programming I used:
https://stackoverflow.com/questions/658763/how-to-suppress-scientific-notation-when-printing-float-values
to display random return types in non-scientific notation.
The whole program has been nested in a loop so if invalid input occurs, it takes
the user back around to the beginning.
"""

import math
import random

"""
recursive function working out random investment returns between -20% and +20%
function called each year with random returns applied to the previous year's
capital and returns printed for each year
"""
def recursive_random_interest (investment_amount, investment_term, year_ticker):
    investment_amount = investment_amount + investment_amount * (random.randint(-20,20)/100)
    investment_term = investment_term -1
    print("""These are the running yearly capital amounts:
   in year {0} your capital was {1:.2f}""".format(year_ticker, investment_amount))
    year_ticker += 1
    if investment_term > 0:
        recursive_random_interest(investment_amount, investment_term, year_ticker)

"""
function to work out interest added each after a term of years to an unchanging capital amount
formula provided by Hyperion
"""
def simple_interest (investment_amount, investment_interest_rate, investment_term):
    investment_amount = \
    investment_amount + investment_amount * investment_interest_rate/100 * investment_term
    return investment_amount

"""
function to work out interest added each year to a capital amount, with the interest of the
next year then calculated on this changed capital amount
formula provided by Hyperion
"""
def compound_interest (investment_amount, investment_interest_rate, investment_term):
    invest_amount = investment_amount * \
        math.pow((1 + investment_interest_rate/100), investment_term)
    return invest_amount

"""
function to work out monthly repayments on a mortgage/bond
formula provided by Hyperion
"""
def bond_repayment (bond_interest_rate, house_price, bond_term):
    repayment = (((bond_interest_rate/100)/12) * house_price)/\
        (1 - (1 + (bond_interest_rate/100)/12)**(0 - (bond_term * 12)))
    return repayment

#program to get user choices on type of finance and type of interest on that finance
loop = True
while loop:
    finance_choice = input("""Welcome. These are your financial choices today:\n\n
    \tinvestment - to calculate the amount of interest you will receive
    on your investment\n
    \tbond - to calculate how much you'll have to pay on your home loan\n\n
    Enter either 'investment' or 'bond' from the menu above to proceed:""")

    if finance_choice.upper() == 'INVESTMENT':
        investment_amount = float(input("Please enter the amount you wish to invest: "))
        investment_interest_rate = float(input \
            ("We will now kindly allow you to choose your own interest rate. Please enter this: "))
        investment_term = int(input("Please enter the term of your investment, in years: "))
        interest_type = input("""Please enter your preferred interest type:
        'simple' or 'compound' or gamble and select 'shares' and the interest rate will become random
        (Please note- in stocks and shares returns can go down as well as up): """)

        if interest_type.upper() == 'SIMPLE':
            investment_amount = simple_interest(investment_amount, investment_interest_rate, investment_term)
        elif interest_type.upper() == 'COMPOUND':
            investment_amount = compound_interest(investment_amount, investment_interest_rate, investment_term)
        elif interest_type.upper() == 'SHARES':
            year_ticker = 1
            recursive_random_interest(investment_amount, investment_term, year_ticker)
            break
        else:
            print("I'm sorry your input was incorrect, please start again.")
            continue
        print("The return on your investment is {0:.2f} pounds".format(investment_amount))
        loop = False

    elif finance_choice.upper() == 'BOND':
        house_price = int(input("Please enter the value of the property: "))
        bond_interest_rate = float(input("""We will now kindly allow you to choose your own interest rate.
        Please enter this: """))
        bond_term = int(input("Please enter the term of your bond, in years: "))
        repayment = bond_repayment(bond_interest_rate, house_price, bond_term)
        print("Your bond's monthly repayment is {0:.2f} pounds".format(repayment))
        loop = False

    else:
        print("I'm sorry your input was incorrect, please start again.")
        continue
