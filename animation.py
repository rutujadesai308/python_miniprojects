import turtle
turtle.bgcolor("lightpink")
turtle.pensize(1.5)
turtle.speed(0.5) #speed of drawing the circle
color = ["red","blue", "green", "orange"]
for a in range(9): #this will repeat 4 colored circles 9 times
	for i in color:
		turtle.color(i)
		turtle.circle(100)
		turtle.left(10) #this will leave space of 10 pixels from left after each circle

		

turtle.mainloop()