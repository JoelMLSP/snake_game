from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open(file="data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.current_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

  #  def game_over(self):
      #  self.goto(0,0)
       # self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)



    def gain_score(self):
        self.current_score += 1
        self.update_scoreboard()



    def reset(self):
        if self.current_score > self.high_score:
            with open(file="data.txt", mode="w") as data:
                self.high_score = self.current_score
                data.write(str(self.high_score))
        self.current_score = 0
        self.update_scoreboard()









