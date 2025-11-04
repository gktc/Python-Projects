from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("black")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}",align=ALIGNMENT ,font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",align=ALIGNMENT ,font= ("Courier", 16, "normal"))

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()