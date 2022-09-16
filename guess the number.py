n=25 #no. to be guessed
print("Guess the number between 1 to 50")
i=9
while(10>i>0):
    print("chances left to guess",i)
    i=i-1
    x=int(input())
        
    if x>n:
        print("Your guess is high,please try a smaller number")
        continue;
    elif x<n:
        print("Your guess is low,please try a greater number")
        continue;
    else:
        print("You guessed the correct number")
        print("You took",9-i,"chances to guess the number")
        break;    
        
    
print("game over")
