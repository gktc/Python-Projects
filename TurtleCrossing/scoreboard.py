FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-250, y=250)
        self.write(f"Level {self.level}", align="left", font= FONT)

    def next_level(self):
        self.level += 1
        # print(self.level)
        self.update_scoreboard()

    def game_over(self):
         self.goto(0,0)
         self.write("Game Over" ,align="center", font=FONT)
         # self.update_scoreboard()
