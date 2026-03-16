from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

# Score Board Setup
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    # Score Updates
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Game Over when collision with the wall happens
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.!",align=ALIGNMENT,font=FONT)

    # Score will increase when snake eats food
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
