from turtle import *

color("yellow")
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(40)

color("green")
begin_fill()
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
end_fill()


penup()
goto(100, 100)
pendown()

color("red")
begin_fill()
right(150)
forward(100)
left(120)
forward(100)
end_fill()


penup()
goto(20, 80)
pendown()

color("blue")
begin_fill()
left(30)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()

penup()
goto(80, 80)
pendown()

color("blue")
begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()
exitonclick()
