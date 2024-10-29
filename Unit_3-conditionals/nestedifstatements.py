# Nested if statements


prime = True
cost = 25
age = 17
consent = False

# if (prime == True or cost > 20) and (age >= 18 or consent == True):

if prime:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("NO FREE SHIPPING!!!!!")

elif cost >= 25:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("NO FREE SHIPPING!!!!!")

else:
    print("NO FREE SHIPPING FOR YOUOOOO!!!!!!")


# Decide if we need an umbrella
# You need an umbrella if its raining ANd your going outside that day

raining = input("Is it raining outside?\n>")


if raining.lower() == "yes":
    outside = input("do you plan on going outside?\n>")

    if outside.lower("yes"):
        raining = input("Is it raining outside?\n>")
        print("BRING AN UMBRELLA")
    else:
        print("NO UMBRELLA")
else:
    print("NO UMBRELLA")