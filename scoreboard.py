from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level= 1
        self.penup()
        self.goto(-290, 270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Level: {self.level} ", font=FONT)

    def increase_level(self):
        self.level+=1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", font=FONT)
