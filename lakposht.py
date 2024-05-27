
import turtle
import random


wn = turtle.Screen()
wn.title("بازی لاکپشت و توپ")
wn.bgcolor("white")  
wn.setup(width=600, height=600)


square = turtle.Turtle()
square.speed(0)
square.shape("square")
square.color("blue")
square.shapesize(stretch_wid=30, stretch_len=30)
square.penup()
square.goto(0, 0)



turtle.speed(0)
turtle.shape("turtle")
turtle.color("black")  # تغییر رنگ لاکپشت به سیاه
turtle.shapesize(stretch_wid=1, stretch_len=2)
turtle.penup()
turtle.goto(0, 0)



ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(random.randint(-290, 290), random.randint(-290, 290))

score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(300, 300)
score_display.write("امتیاز: 0", align="right", font=("Courier", 16, "normal"))

def move_left():
    x = turtle.xcor()
    x -= 20
    if -290 < x:
        turtle.setx(x)
        check_collision()

def move_right():
    x = turtle.xcor()
    x += 20
    if x < 290:
        turtle.setx(x)
        check_collision()


def move_forward():
    y = turtle.ycor()
    y += 20
    if y < 290:
        turtle.sety(y)
        check_collision()

def move_backward():
    y = turtle.ycor()
    y -= 20
    if -290 < y:
        turtle.sety(y)
        check_collision()


def check_collision():
    global score
    if turtle.distance(ball) < 20:
        ball.goto(random.randint(-290, 290), random.randint(-290, 290))
        score += 1
        score_display.clear()
        score_display.write(f"امتیاز: {score}", align="right", font=("Courier", 16, "normal"))
        
      
        turtle.color(random.choice(["red", "green", "purple", "orange"]))
   

    
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_forward, "Up")
wn.onkey(move_backward, "Down")


while True:
    wn.update()
    check_collision()
