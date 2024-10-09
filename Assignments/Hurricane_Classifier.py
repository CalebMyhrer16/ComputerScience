Hurricane = input("what is MPH for the hurricane?\n>")
Hurricane = int(Hurricane)

if Hurricane < 74:
    print("Tropical Storm")

elif Hurricane < 111:
    print("Category 2")

elif Hurricane < 130:
    print("Category 3")

elif Hurricane < 157:
    print("Category 4")

elif Hurricane >= 157:
    print("Category 5") 