import random

#random.randint(4, 10)

# Adventure game
# It's a game. Your player has a name (asked at the beginning)
# Your player has health
# You have an inventory of items (see automate the boring stuff chapter 5 project)
	#use JOIN() to print inventory list
# The game is presented as a series of prompts to the player
# There are three bosses of varying difficulty
# On their turn, the player can do several things
# - INVENTORY will print out the player's current inventory
# - ATTACK will attack the current boss
# - EAT will consume a cookie from the player's inventory and restores health.
#   - if there are no cookies, the player loses their turn
# - Add more options if you want
# After beating a boss, the player receives loot from the boss which is added to their inventory
# Each boss should drop one unique item as a trophy
# After each player turn, if the boss is still alive, they attack (or do other stuff, feel free to get creative if you want)
# After each boss, move to the next boss with a story hook

#consider a custum function to automatically capitalize all inputs! also trims with '.strip()'

#request name and welcom player
print("Welcome to Super Adventure VIII!".center(50,"-"))
name = input("What is your name bold adventurer?!\nName: ")
print("Welcome,",name+". You find yourself in a dungeon, of course! There are three bosses to conquerer! Have at it!\n")
print("Enter the command, 'HP', to check your Health at any time. Try it now!")

HP = 50
#HP request function
def HPrequest():
	print("Health:",HP"\n")

	
def attack():
	dmg = random.randint(2,5)
	print(dmg,"Damage")

HPtut = input()
while True:
	if HPtut in ["HP","hp"]:
		HPrequest()
		break
	else:
		print("You can enter 'HP' to see your HP! Try it now!\n")
		HPtut=input()
#story beat, boss 1 narrative
print("You enter a dark cave and before you stands a mighty minotaur! He snorts at you and brandishes a large battle axe. Try entering 'ATTACK' to attack the beast!")
	
