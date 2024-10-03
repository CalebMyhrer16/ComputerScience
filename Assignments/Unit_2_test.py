Noun_1 = input("Name a place \n>") #Task 1
Noun_2 = input("A animal \n>")
verb_1 = input("an action \n>")
print("In a small " + Noun_1 + " there lived a " + Noun_2 + " who loved to " + verb_1)

def add_three(x, y, z): #Task 2
    print(x + y + z)
x = input(" one number \n>")
x = int(x)
y = input(" another number \n>")
y = int(y)
z = input(" final number\n>")
z = int(z)
add_three(x, y, z)

def data_three(): #Task 3
    word_1 = input("Give a Word \n>")
    integer_1 = input("Give a integer \n>")
    integer_1 = int(integer_1)
    float_1 = input("Give a float \n>")
    float_1 = float(float_1)
    print(integer_1 + float_1)
    print(word_1)
data_three()