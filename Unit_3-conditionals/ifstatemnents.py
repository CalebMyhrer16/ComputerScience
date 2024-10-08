#if statements evaluate boolean expresions 
#they make desicions about which code to run next 

#take a temperature 
#print :<tempature> is hot" if its its >= to 80
#Otherwise, print "<tempature is not hot"
temp = input("what the tempature in f?\n>")
temp = int(temp)

# if <boolean expression> :
# This should remind of writting a functiob
# def <name> ():
if temp >= 80:
    print(str(temp) + " is hot!")

else:   #Otherwise....
    print(str(temp) + " is not hot...")

# Not all if statements need an else, in fact NONE of them NEED and else
# Else statements are an option, they ar eoptional
# ALL else statements must have a corresponding if statement
# Else statements cannot exist alone
# An if statement can only have one else

# Create a program that asks for a password
# if the password is correct print ACESS denied
# The password is skibidi68.9

real_password = "skibidi68"
input_pass = input("what the password?\n>")

if real_password == input_pass:
    print(" ACCESS GRANTED")

else:
    print(" ACCESS DENIED")

question_1 = 