import turtle
import time
import random


delay = 0.1

# Score
score = 0
high_score = 0

# Set up our screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#cbcba9")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.shapesize(stretch_wid=1, stretch_len=1, outline=None)
food.penup()
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()

pen.clear()
pen.goto(-270,260)
pen.write(f"Score : {score}",align="left", font=("courier", 14,"normal"))
pen.goto(0,260)
pen.write(f"High Score : {high_score}",align="left", font=("courier", 14,"normal"))

segments = []

# Update Score Board
def write_screen():
    pen.clear()
    pen.goto(-270,260)
    pen.write(f"Score : {score}",align="left", font=("courier", 14,"normal"))
    pen.goto(0,260)
    pen.write(f"High Score : {high_score}",align="left", font=("courier", 14,"normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def write_score(statement):
    global score
    global high_score

    if  statement == "win":
        # Increase score
        score += 10
        print("Horaayy! +10 points! ...")

        if score > high_score:
            high_score = score
            print("New Record Champ! Continue ...")

    if statement == "lose":
        # Reset the score
        score = 0
        print("Oooo. You dead ...")

 
    write_screen()    

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

print("The game starts. Let us play ...")


# Main Game Loop
while True:
    wn.update()
    # # Check for collison on border
    # if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    #     time.sleep(1)
    #     head.goto(0, 0)
    #     head.direction = "stop"

    #     # Hide the segments
    #     for segment in segments:
    #         segment.goto(1000, 1000)

    #     # Clear the segments list
    #     segments.clear()

    #     # Reset the delay

    #     delay = 0.1

    #     # Reset the score
    #     score = 0

    #     write_score()

    # Passing the borders
    if head.xcor() > 290:
        head.goto(head.xcor()-(2*290),head.ycor())

    if head.xcor() < -290:
        head.goto(head.xcor()+(2*290),head.ycor())

    if head.ycor() > 290:
        head.goto(head.xcor(),head.ycor()-(2*290))

    if head.ycor() < -290:
        head.goto(head.xcor(),head.ycor()+(2*290))

    # Check for collision with food
    if head.distance(food) < 20 :
        x = random.randrange(-290, 290, 1)
        y = random.randrange(-290, 290, 1)
        food.goto(x, y)

        # Add a segments to list
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        write_score("win")

    # Get ready to add segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Add to snake's head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()

    # Check for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()
            
            # Reset the delay

            delay = 0.1
            write_score("lose")


    time.sleep(delay)   