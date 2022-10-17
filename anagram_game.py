import random
list1 = ['ironman','hulk','batman','hawkeye','wanda','thor']
word = random.choice(list1)
jumble = "".join(random.sample(word,len(word)))




chances = 5

print("*"*35)
print("***** Avengers Jumble Bumble *****")
print("*"*35)



while(chances!=0):
	
	print(jumble)
	Guess = input("Guess The word: ").lower()
	if Guess == word:
		print("You guessed correct!")
		break
	else:
		chances -= 1
		print("You guessed wrong,")
		print("Chances left = ",chances)


			
