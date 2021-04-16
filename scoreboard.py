from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.color("black")
        self.level_value = 1
        self.penup()
        self.goto(-100, 250)
        self.boardwrite()


    def boardwrite(self):
        self.write(f"Level {self.level_value}", align="center", font=FONT)


    def update(self):
        self.clear()
        self.level_value += 1
        self.boardwrite()


    def finish(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
