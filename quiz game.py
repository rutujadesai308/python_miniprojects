print("Welcome to the quiz!")
print("Do you want to play? ")
x=str(input()).lower()
if(x!="yes"):
    quit()
else:
    print("Let's Play")
score=0
print("(1)What does CPU stands for? ")
x=str(input()).lower()
if(x=="central processing unit"):
    print("correct")
    score+=1
else:
    print("incorrect")

print("(2)What does GPU stands for? ")
x=str(input()).lower()
if(x=="graphics processing unit"):
    print("correct")
    score+=1
else:
    print("incorrect")

print("(3)What does RAM stands for? ")
x=str(input()).lower()
if(x=="random access memory"):
    print("correct")
    score+=1
else:
    print("incorrect")


print("(4)What does HTML stands for? ")
x=str(input()).lower()
if(x=="hyper text markup language"):
    print("correct")
    score+=1
else:
    print("incorrect")
    
print("Your score = ",score)
print("You scored",(score/4)*100,"%")
