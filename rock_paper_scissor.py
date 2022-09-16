import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
	user_input=input("Enter rock/paper/scissors or q to quit the game ").lower()
	if user_input=="q":
		break
	if user_input not in options:
		continue
	random_number=random.randint(0,2)
	#rock:0,paper:1,scissors:2
	computer_input=options[random_number]
	print("computer picked",computer_input)

	if user_input=="rock" and computer_input=="scissors":
		user_wins += 1
		print("You won!")
	elif user_input=="paper" and computer_input=="rock":
		user_wins += 1
		print("You won!")
	elif user_input=="scissors" and computer_input=="paper":
		user_wins += 1
		print("You won!")
	else:
		print("You lost!")
		computer_wins += 1
print("You won",user_wins,"times!")
print("Computer won",computer_wins,"times!")        