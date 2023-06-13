"""dinner = ["Beans", "Okra", "Egusi"]
drinks = ["coffee", "soda", "tea"]
desser = ['cake', 'ice', 'cream']

food = [drinks, dinner, desser]
print("2D Lists:",food)
print("\n")

food_1 = [[drinks, dinner, desser]]
print("3D Lists:",food_1[0][0])

print("\n")
print("AND SO ON...")

# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments 

def add(*args):
	sum = 0
	for i in args:
		sum += i
	return sum
print(add(1, 2, 3, 4, 5))


#**kwargs = parameter that will pack all arguments into a dictionary
#useful so that a function can accept a varying amount of keyworda arguments

def hello(**kwargs):
	#print("Hello " + kwargs['first'] + " " + kwargs['last'])
	print("Hello", end=' ')
	for key, value in kwargs.items():
		print(value, end=' ')
hello(title = 'Mr.', first = "Godspower", mid = "Pius", last = "Maurice\n")


import random as rd 
x = rd.randint(1, 6)
print(x)

y = rd.random()
print(y)

myList = ['rock', 'paper', 'scissors', "play"]
z = rd.choice(myList)
print(z)

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
rd.shuffle(card)
print(card)

try:
	with open("test.tx") as file:
		print(file.read())
except FileNotFoundError as f:
	print(f)

text = '''\n\nHave a nice day
Bye Christian.'''
with open("test_2.txt", 'a') as file:
	file.write(text)

import shutil 
# copyfile() = Copies contents of a file
# copy() = copyfile + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
shutil.copy2("test_2.txt", 'copy_1.txt')


help("modules")
"""


import random as rd 

while True:
	choices = list(["Rock", "Paper", "Scissors"])
	computer = rd.choice(choices)

	player = input("\nChoose an answer: Rock, Paper or Scissors? ").capitalize()
	if player == computer:
		print("BOT said:",computer)
		print("YOU said:",player)
		print("You win!")
	elif player not in choices:
		print("Not included. Please Use the acceptables")
	else:
		print("BOT said:",computer)
		print("YOU said:",player)
		print("You lose")
		
	import stuff1
	stuff1.startAgain()

#br = input("Press any key to continue...")
#print("Do you wanna play again?")

	
