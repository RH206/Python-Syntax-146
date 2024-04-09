#Making your code interactive by allowing users to add their input

#input() function prompt user witha string, and allows them to respond WITH A STRING

#input() ALWAYS RETURNS A STRING


food = input("What is your favorite food?") 
print(food)

if food == 'tacos':
    print("We're gonna get along just fine!")
else:
    print("WRONG ANSWER")
last_words =input('Any last words? ')
print("I'll put", last_words, 'on your tomb stone')

#If you're goint to use arithmatic or boolean operators (>,<,>=,<=) I need to convert to int
#since input returns

age = input('How old are you')

if age >= 65:
    print("you're a senior")
else:
    print("you're a youngster")