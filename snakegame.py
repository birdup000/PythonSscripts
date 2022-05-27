import turtle
import time
import random
 
delay = 0.1
score = 0
high_score = 0



wn = turtle.Screen()
wn.title("Snake Game WITH THE TWISTS")
wn.bgcolor("purple")
 
#WINDOW SIZE OF BIRDS
wn.setup(width=600, height=600)
wn.tracer(0)
 
 
#SNAKE HEADS LOL
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
 
#FOOOD
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
 
 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))