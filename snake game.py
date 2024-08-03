import turtle
import random
import time

# CREATING SCREEN
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("black")

# CREATING BORDER
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 215)
border.color("red")
border.pendown()
for _ in range(2):
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
border.hideturtle()

# SHOWING THE SCORE BOARD
score = 0
delay = 0.1

# SNAKE
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# CREATING THE FOOD
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# storing the number of old fruits
old_fruit = []

# HOW THE SCORE GETS UPDATED
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

# DEFINING HOW TO MOVE
def snake_go_up():
    if snake.direction != "Down":
        snake.direction = "Up"

def snake_go_down():
    if snake.direction != "Up":
        snake.direction = "Down"

def snake_go_left():
    if snake.direction != "Right":
        snake.direction = "Left"

def snake_go_right():
    if snake.direction != "Left":
        snake.direction = "Right"

def snake_move():
    if snake.direction == "Up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "Down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "Left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "Right":
        x = snake.xcor()
        snake.setx(x + 20)

# KEYBOARD BINDING-FUNCTIONING OF KEYS OR ARROWS
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# MAIN LOOP-how it works no of times and various possibilities of collisions...
while True:
    screen.update()
    # snake and fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        # After eating the fruit, the score will change, and we are updating the score here
        score += 1
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

        delay -= 0.001
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    # snake and border collision
    if (
        snake.xcor() > 280
        or snake.xcor() < -300
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write(
            "Game over\n Your score is {}".format(score),
            align="center",
            font=("Courier", 24, "bold"),
        )
        break  # Break out of the while loop when the game is over

    # snake bite itself leads to game over case
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(
                "Game over\n Your score is {}".format(score),
                align="center",
                font=("Courier", 24, "bold"),
            )
            break  # Break out of the for loop when the game is over

    time.sleep(delay)

turtle.Terminator()
