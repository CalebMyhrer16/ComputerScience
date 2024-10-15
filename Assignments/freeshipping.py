#  Create a function called free_shipping
# That tells you if you qualify for free shipping or not
# You only get shipping if 
# you are a Prime memebr OR order is at least 25$
# You are at least 18 years old OR have parent consent
# Your function should take four parameters
# prime (boolean), cost (float), age (int), consent (bool)
#huge hint
# you can use more than one logical operator in a condition
# use parenthesis to group if needed
def free_shipping(age, permission, price, prime):
    if prime == "Yes":
        if age > 18:
            print("you got Free shipping")
        else: 
            print("Did your parent give you permission")
    
            if permission == "yes":
                print("you got free shipping")
            else:
                print("please ask for parent permission")
    else:
        if price > 25:
            print("you got free shipping")
        else:
            print("you dont have free shipping")

free_shipping(18, "yes", 45, "no")

