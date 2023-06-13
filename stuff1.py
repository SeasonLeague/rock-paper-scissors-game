
def startAgain():
	import os 
	import sys
	from time import sleep 

	qestn = input("Do you wish to play again?  (yes/no)\n").capitalize()

	if qestn == 'Yes':
		sleep(1)	
		if sys.platform.startswith("win32"):
			os.system('cls')
		elif sys.platform.startswith("linux"):
			os.system('clear')
		else:
			print("Can't get this machine's platform...")
	elif qestn == 'No':
		print("\nThanks for playing this game")

	else:
		print("Its either a yes or a no..!")

startAgain()