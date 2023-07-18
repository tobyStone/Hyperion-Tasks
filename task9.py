"""
A program set by Hyperion as Task 9. It gives two options, to input an expression for calculation,
or to read a line from a file which contains expressions for calculation.
The task is orientated around defensive programming. As such,
the coded functions check for non-existent files, non-numeric characters and blank lines
and return messages for these errors.
The program will then calculate any length of expression which contains a plus, minus,
division or multiplication operator, returning the result. This result is written to file in the case
of the input expressions, or returned to the user in the case of the lines read from
the pre-existing file.
The following were used as sources for the code contained:
https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
Mike James's The Python Programmer: Everything is Data, pages 239/240- Context Managers and With pattern
https://stackoverflow.com/questions/4138202/using-isdigit-for-floats
https://www.w3schools.com/python/python_ref_list.asp
Thanks also to feedback from both Darren (helper functions) and Chris (code-factorisation) at Hyperion.
Following on from these discussions, I have also moved on from my original design of using eval()
to work out the calculations. Hence, the calculator program I designed. A future change would be to include
the calculations of powers and involving brackets (probably by recursion, for the last).
"""

def addition(number1, number2):
    '''this and the next three functions are helpers for the find and replace function, below'''
    sum_add = number1 + number2
    return sum_add

def subtraction(number1, number2):
    difference = number1 - number2
    return difference

def multiplication(number1, number2):
    product = number1 * number2
    return product

def division(number1, number2):
    dividend = number1/number2
    return dividend


def list_to_number(array_to_change):
    '''function takes the comma-separated digits of a listed number and combines them
    by working out the maximum power of ten from the list's length, then
    decrementing this, multiplying by the digits and summing the result'''
    sum_list = 0
    power = len(array_to_change) - 1
    for place_value_column in array_to_change:
        sum_list = sum_list + place_value_column * 10 ** power
        power = power - 1
    return sum_list

def find_next_num_func(next_num_for_loop_counter, find_next_num, array, int2_catcher, for_loop_counter):
    '''finds the right hand operand of the operators found in the calculation function'''
    while find_next_num == True:
        if next_num_for_loop_counter > len(array) - 1:
            find_next_num = False
            break
         #check if numeric and ensure floats counted as such
        elif array[next_num_for_loop_counter].replace(".","").replace("-","").isdigit():
            #append operands into list, appending so right order maintained
            int2_catcher.append(float(array[next_num_for_loop_counter]))
            #replaces all used operands and operators with 'a' as placeholders
            array.insert(for_loop_counter, 'a')
            array.pop(for_loop_counter + 1)
            array.insert(next_num_for_loop_counter, 'a')
            array.pop(next_num_for_loop_counter + 1)
            next_num_for_loop_counter = next_num_for_loop_counter + 1
                
        else:
            find_next_num = False
            break
    tuple_return_next = (array, next_num_for_loop_counter, int2_catcher)
    return tuple_return_next


def find_last_num_func(last_num_counter, find_last_num, array, int1_catcher):
    '''finds the left hand operand of the operators found in the calculation function'''
    while find_last_num is True:
        if last_num_counter < 0:
            find_last_num = False
            break
        #check if numeric and ensure floats counted as such
        elif array[last_num_counter].replace(".","").replace("-","").isdigit():
            #insert operands into a list, inserting so right order maintained
            int1_catcher.insert(0, float(array[last_num_counter]))
            #replaces all used operands and operators with 'a' as placeholders
            array.insert(last_num_counter, 'a')
            array.pop(last_num_counter + 1)
            last_num_counter = last_num_counter - 1
            end_slice = last_num_counter
        else:
            find_last_num = False
            break
    tuple_return_last = (array, last_num_counter, int1_catcher, end_slice)
    return tuple_return_last

def sum_and_replace_func(operator, next_num_for_loop_counter,\
   last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice):
    '''combines the right and left hand operator with 
    the operator type located to calculate the result 
    of the expression, using the four helper functions 
    at the top of the program. This function then replaces 
    all of the terms in the expression with its result'''
    int1_sum = list_to_number(int1_catcher)
    int2_sum = list_to_number(int2_catcher)
    if operator == "*":
        reinsert_sum = multiplication(int1_sum, int2_sum)
    elif operator == "/":
        reinsert_sum = division(int1_sum, int2_sum)
    elif operator == "+":
        reinsert_sum = addition(int1_sum, int2_sum)
    elif operator == "-":
        reinsert_sum = subtraction(int1_sum, int2_sum)
    #empty lists used to capture operands
    int1_catcher.clear()
    int2_catcher.clear()
    array.insert(next_num_for_loop_counter, str(reinsert_sum))
    for_loop_counter = for_loop_counter + 1
    del array[end_slice + 1:next_num_for_loop_counter]
    next_num_for_loop_counter = 0
    last_num_counter = 0
    tuple_return_final = (next_num_for_loop_counter, last_num_counter,\
       int1_catcher, int2_catcher, for_loop_counter, array)
    return tuple_return_final




def calc(array):
    '''function looping through the list of numbers and operators, finding operators and then calling
    the helper functions, above, in the order of precedence to find the operands of those operators, 
    calculate the result before returning the resulting list'''
    loop = True

    while loop is True:
        precedence_for_loop_counter = 0
        #two empty lists for operand capture
        int1_catcher = []
        int2_catcher = []
        for_loop_counter = 0
        #variable to determine parts of list to be deleted once calculations made
        end_slice = 0
        last_num_counter = 0
        next_num_for_loop_counter = 0
        #loop checking for operators with higher precdence and running different part of the below function, if present
        for precedence in array:
            if precedence == "/":
                precedence_for_loop_counter = precedence_for_loop_counter + 1
            if precedence == "*":
                precedence_for_loop_counter = precedence_for_loop_counter + 1

        for numeric in array:
            if precedence_for_loop_counter > 0:
                if numeric == "*":
                    operator = "*"
                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter,\
                       find_next_num, array, int2_catcher, for_loop_counter)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last
                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter,\
                       last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    #unpacking the tuple into variables, in the order in which they were returned
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher,\
                       for_loop_counter, array = tuple_returned_final
                    #counting down operators with higher precedence and leaving precedence loop, if zero left
                    precedence_for_loop_counter = precedence_for_loop_counter - 1
                    if precedence_for_loop_counter == 0:
                        numeric = 0

                elif numeric == "/":
                    operator = "/"
                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1
                    if array[next_num_for_loop_counter] == "0":
                        print("You are trying to divide by zero. This is undefined behaviour. The calculation is now exiting.")
                        del array[1:]
                        array[0] = "undefined"
                        loop = False
                        break
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter, find_next_num,\
                       array, int2_catcher, for_loop_counter)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last
                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter,\
                       last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    #unpacking the tuple into variables, in the order in which they were returned
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher,\
                       for_loop_counter, array = tuple_returned_final
                    #counting down operators with higher precedence and leaving precedence loop, if zero left
                    precedence_for_loop_counter = precedence_for_loop_counter - 1
                    precedence_for_loop_counter = precedence_for_loop_counter - 1
                    if precedence_for_loop_counter == 0:
                        break
              

                else:
                    for_loop_counter = for_loop_counter + 1
                    for index in array:
                        del array[end_slice + 1:next_num_for_loop_counter]
                        next_num_for_loop_counter = 0
                        last_num_counter = 0

            else:
                if numeric == "+":
                    operator = "+"
                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter, find_next_num,\
                       array, int2_catcher, for_loop_counter)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last
                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter, last_num_counter,\
                       int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    #unpacking the tuple into variables, in the order in which they were returned
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter,\
                       array = tuple_returned_final
                    break
                  

                elif numeric == "-":
                    operator = "-"
                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter, find_next_num, array,\
                       int2_catcher, for_loop_counter)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    #unpacking the tuple into variables, in the order in which they were returned
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last
                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter,\
                       last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    #unpacking the tuple into variables, in the order in which they were returned
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher,\
                       for_loop_counter, array = tuple_returned_final
                    break
              

                else:
                    for_loop_counter = for_loop_counter + 1
                    for index in array:
                        del array[end_slice + 1:next_num_for_loop_counter]
                        next_num_for_loop_counter = 0
                        last_num_counter = 0
            if len(array) <= 1:
                loop = False

    return array





def writeToFile():
    '''function run if user requests to input the expression for calculation'''
    #with pattern to run RAII and close automatically
    with open("CalculationFile.txt", "a") as myFile:
        loop = True
        while loop is not False:
            sum_input = input("""Please input a sum of as many whole numbers you'd like.\n
           You may include '+', '-', '*', and '/': """)
           #list method to stop floats setting off the non-numeric errors
            split_sum = list(sum_input.replace(" ", "").replace("\n",""))
            for i  in split_sum:
                if i.isdigit() is False:
                    print("These inputs are not all numerical, please try again")
                    continue
                else:
                    sum_answered = calc(split_sum)
                    print(f"This is the answer to your math's question: {sum_answered[0]}")
                    myFile.write(str(sum_input))
                    myFile.write(" = ")
                    myFile.write(str(sum_answered[0]))
                    myFile.write("\n")
                    break
            loop = input("Please input \'False\' if you want to stop calculating...: ")
            if loop.upper() == "FALSE":
                loop = False
                print("Thank you, and goodbye.")
            else:
                continue
    


def readFromFile(file_chosen):
    '''function run if user requests to read expressions from a file'''
    myFile = None
    #try blockto back-stop errors
    try:
        #with pattern to run RAII and close automatically
        with open(file_chosen, "r") as myFile:
            print("File opening...\n\nReading first line...\n\n")
            loop = True
            while loop is not False:
                sum_read = myFile.readline()
                if not sum_read:
                    print("There's nothing in this line.")
                split_sum = list(sum_read.replace(" ", "").replace("\n",""))
                for i in split_sum:
                    if i.isdigit() is False:
                        print("These inputs are not all numerical, please try to read the next line")
                        continue
                    else:
                        sum_answered = calc(split_sum)
                        print(f"""Printed below is the file's calculation along with it's answer:\n{sum_read} = {sum_answered[0]}""")
                        break
                loop = input("""Please input \'False\' if you want to stop reading lines from the opened file...: """)
                if loop.upper() == "FALSE":
                    print("Thank you, and goodbye.")
                    loop = False
                else:
                    continue

    except FileNotFoundError as error:
        #catch-all error message, a lcack of file should have been discovered earlier,\
        # at the point of inputting the file name
        print("""Something has gone badly wrong with the logic in ths program.\n 
        Please turn the computer off and on and try again...""")
        print(error)

    finally:
        if myFile is not None:
            myFile.close()


def stream_choice():
    '''function which offers the user the choice of reading expressions from a file and calculating their
    result or writing input expressions to a file, along with their result'''
    looper = True

    while looper is True:

        choice = input("""Welcome to the calculator.\n 
        You can either choose to input an expression for calculation,\n
       or to open a file which will import expressions to be calculated.\n
       For the first please type 'input'.\n
       For the second please type 'import': """)
        if choice.upper() == 'INPUT':
            looper = False
            writeToFile()
        elif choice.upper() == 'IMPORT':
            file_choice = input("""Please input the file you want to open.\n
           The following file: 'calculations.txt' is available: """)
            if file_choice == 'calculations.txt':
                file_chosen = 'calculations.txt'
                looper = False
                readFromFile(file_chosen)
            else:
                print("The file that you are trying to open does not exist. Please try again: ")
        else:
            print("You have not made one of the choices. Please try again: ")


        
stream_choice()
