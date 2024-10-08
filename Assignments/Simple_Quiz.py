#string functions are a group of functions that modify strings
#String functiobs are a group of functions that modify strings
#.Lower()
#. Lower() changes the string to be all lowercase
#.upper() changes the string to uppercase
#.capitalize()  changes entire string to lowercas, then capilizes the first letter
#Hello  World becomes > Hello world

#.title() changes the entire string to titlecase(capital first letter on each word)
# "hello world" > "Hello World"

#.swpacase() inverts the capitalization of each character
#"Hello World!" > "hELLO wORLD"

question1 = input(str("What is the best video game \n>"))
question_entered1 = "Gta 6"
question2 = input(str("What is the best movie \n>"))
question_entered2 = "Spiderman 2"
question3 = input(str("what is the best song \n>"))
question_entered3 = "new ksi drop"
question4 = input(str("where is my house \n>"))
question_entered4 = "Albertville"
question5 = input(str("What is the best food \n>"))
question_entered5 = ("lunchly")

score = 0
if question1 == question_entered1:
        score = score + 1
if question2 == question_entered2:
        score = score + 1
if question3 == question_entered3:
        score = score + 1
if question4 == question_entered4:
        score = score  + 1
if question5 == question_entered5:
        score = score + 1
print(score)