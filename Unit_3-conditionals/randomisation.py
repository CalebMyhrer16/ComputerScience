import random

r = random.randrange(0,10)
# First number is inclusive, secound is exclusive
# 0 <= result < 10


print(r)

print("you have a -8 perecnt chance to win!")
p = random.random()

print(p)
if p <= 0.50:
    print("win")
else:
    print("L")

list(ModuleNotFoundError)