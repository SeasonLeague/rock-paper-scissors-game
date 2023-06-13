
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
	
