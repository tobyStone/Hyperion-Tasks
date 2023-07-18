'''
based on learning from Hyperion.dev
first compulsory task set in T07
A program to take numerical inputs until
'-1' is inputted, at which point all non '-1'
inputs are totalled.
To deal with fractional parts in binary I have used decimal as suggested here:
https://stackoverflow.com/questions/55517241/how-to-correctly-deal-with-floating-point-arithmetic-in-python
'''

from decimal import Decimal

loop_counter = 0
sum = Decimal(0.0)
number_input = Decimal(0.0)
while number_input != -1.0:
    number_input = Decimal(input("""Please enter a number and I'll add every number you enter.
    I will then give you their mean.
    If you wish to stop inputs and output the sum of these, input \'-1\': """))
    if number_input == -1.0:
        continue
    loop_counter += 1
    sum = sum + number_input
    mean = sum/loop_counter
print(f"Your sum is: {sum} and your mean is: {mean}")
