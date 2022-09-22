import random

while True:
	number=input(random.randint(1,6))
	rollagain=input("Do you want to roll the dice again?(y/n): ")
	if rollagain=="y":
		continue
	else:
		break