from turtle import Turtle, Screen
import random


class Turtle_Racer:

    def __init__(self, color, pos_x, pos_y):
        self.turtle = Turtle(shape="turtle")
        self.color = color
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(pos_x, pos_y)

    def movement(self):
        self.turtle.forward(random.randint(1, 15))
        if self.turtle.xcor() >= 230:
            return self.color
        else:
            return ""


screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race Game")
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
for t in range(6):
    y = 75 - (30 * t)
    turtles.append(Turtle_Racer(color=colors[t], pos_x=-240, pos_y=y))

no_winner = True
result = ""
while no_winner:
    for t in range(6):
        if result == "":
            result = turtles[t].movement()
        else:
            no_winner = False
            break

if result == user_bet:
    print(f"You win. The {result} turtle is the winner. ")
else:
    print(f"You lose. The {result} turtle is the winner. ")

screen.exitonclick()
