from turtle import Turtle

class Scoreboard(Turtle): #the title of game, on the top of screen
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.score = 0
        self.high_score = self.read_best_score()
        self.hideturtle()
        self.update_the_scoreboard()

    def update_the_scoreboard(self): #will made the first title
        self.write(f"score: {self.score}  High score {self.high_score}", False, 'center', ('curiel', 24, 'normal'))

    def reset(self): #used in main  to reset default title  when snake collide with tail or wall
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("best_scores.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_the_scoreboard()

    def end_title (self): #print game over
        self.goto(0,0)
        self.write('GAME OVER',False,'center',('curiel',24,'normal'))

    def increase_score(self): #it used in main under, detect collision whit food, to increase score by one when food is eat
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}  High score {self.high_score}", False, 'center', ('curiel', 24, 'normal'))

    def read_best_score(self): #get last best score
        with open("best_scores.txt", mode='r') as data:
            the_best_score = int(data.read())
            return the_best_score

