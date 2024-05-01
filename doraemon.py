import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#fcf9f2")  # Doraemon's face color
screen.title("Doraemon Drawing")

# Function to draw a filled circle
def draw_filled_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a rectangle
def draw_rectangle(color, width, height, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Function to draw Doraemon's face
def draw_doraemon_face():
    # Draw Doraemon's face
    draw_filled_circle("#fcf9f2", 100, 0, -50)

    # Draw Doraemon's eyes
    draw_filled_circle("white", 15, -35, 30)
    draw_filled_circle("white", 15, 35, 30)
    draw_filled_circle("black", 7, -35, 40)
    draw_filled_circle("black", 7, 35, 40)

    # Draw Doraemon's nose
    draw_filled_circle("red", 7, 0, 10)

    # Draw Doraemon's mouth
    t.penup()
    t.goto(-30, -10)
    t.pendown()
    t.setheading(-60)
    t.circle(25, 120)

    # Draw Doraemon's whiskers
    t.penup()
    t.goto(-35, 15)
    t.pendown()
    t.setheading(120)
    t.forward(45)

    t.penup()
    t.goto(-35, 0)
    t.pendown()
    t.setheading(90)
    t.forward(45)

    t.penup()
    t.goto(-35, -15)
    t.pendown()
    t.setheading(60)
    t.forward(45)

# Function to draw Doraemon's body
def draw_doraemon_body():
    # Draw Doraemon's body
    draw_filled_circle("#fcf9f2", 130, 0, -190)

    # Draw Doraemon's pocket
    draw_rectangle("#004cb2", 60, 30, -30, -210)

# Function to draw Doraemon's hands
def draw_doraemon_hands():
    # Draw Doraemon's hands
    draw_filled_circle("#fcf9f2", 50, -140, -100)
    draw_filled_circle("#fcf9f2", 50, 140, -100)

# Function to draw Doraemon's feet
def draw_doraemon_feet():
    # Draw Doraemon's feet
    draw_filled_circle("#004cb2", 35, -60, -280)
    draw_filled_circle("#004cb2", 35, 60, -280)

# Function to draw Doraemon
def draw_doraemon():
    draw_doraemon_face()
    draw_doraemon_body()
    draw_doraemon_hands()
    draw_doraemon_feet()

# Initialize the turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Draw Doraemon
draw_doraemon()

# Hide turtle
t.hideturtle()

# Keep the window open until closed manually
screen.mainloop()
