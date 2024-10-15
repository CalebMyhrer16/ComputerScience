# logical operators
# Arithmatic Operators = - * / // ** %
# Comparison Operators > < >= <= ==
# Logical Operators and or !
# And means that BOTH conditions must be true
# OR means that atleast one condition must be true
# ! (not) means the inverse,

def check_eligibility(age, exp):
    if age  >= 18 and exp >=1:
        print("You are eligable!")

    else:
        print("You are not eligable :(")

check_eligibility()