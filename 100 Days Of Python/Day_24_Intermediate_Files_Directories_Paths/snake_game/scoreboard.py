from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

with open("data.txt","r") as file:
    DEFAULT_SCORE = file.read()

# Score Board Setup
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(DEFAULT_SCORE)
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    # Score Updates
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align=ALIGNMENT, font=FONT)

    # # Game Over when collision with the wall happens
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.!",align=ALIGNMENT,font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score  
        new_high_Score = str(self.high_score)  
        with open("data.txt","w") as file:
            file.write(new_high_Score)      
        self.score = 0
        self.update_scoreboard()

            

    # Score will increase when snake eats food
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
