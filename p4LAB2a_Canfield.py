import turtle
wn = turtle.Screen()
tom = turtle.Turtle()
tom.shape("turtle")

for i in [0,1,2,3]:
    tom.forward(50)
    tom.left(90)

kay  = turtle.Turtle()
kay.shape("turtle")

kay.penup()
kay.right(180)
kay.forward(80)
kay.pendown()
            
for i in [0,1,2]:
    kay.forward(80)
    kay.left(120)

turtle.exitonclick()

wn.mainloop()
