# Exception Handeling
# Write z program taht asks for 2 numbers and divides them

# if  = try
# elif = except with error type
# else  =  except
def divide_two_number():
    try: # we always enetr the try block, there is no condition
        x = int(input(" What is the first number?\n>"))
        y = int(input(" What is the secound number?\n>"))
        print(x / y)
    
    except ZeroDivisionError:
        print("Cannot divide by zero, try again")
    
    except ValueError:
        print("Please enter a valid numberical symbol, try again")
        divide_two_number()

    except: # If anything in the try block causes an error, the try block stops
    #then the ecceept is an the rest of the try block nvever finishes running it skipped
    # if the try block executes without an error the except is skipped
    # the only way to get into the except is to throw an error
        print("invalid input, try again")
        divide_two_number() # tell the function to run

divide_two_number()