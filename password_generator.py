import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "123456789"
symbols = "!@#$%^&*()"

all = ""
upper,lower,nums,syms=True,True,True,True

if upper:
	all += uppercase_letters
if lower:
	all += lowercase_letters
if nums:
	all += digits
if syms:
	all += symbols

length=10 #length of the password to be generated
amount=10 #no. of times the password should be generated
for x in range(amount):
	password = "".join(random.sample(all,length))
	print(password)
