import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Tree Drawing")

# Create the turtle
tree_turtle = turtle.Turtle()
tree_turtle.speed(1)
tree_turtle.width(3)

# Draw the trunk
tree_turtle.color("saddlebrown")
tree_turtle.begin_fill()
tree_turtle.penup()
tree_turtle.goto(0, -100)
tree_turtle.pendown()
tree_turtle.goto(0, 0)
tree_turtle.goto(-100, 0)
tree_turtle.goto(-100, -100)
tree_turtle.goto(0, -100)
tree_turtle.end_fill()

# Draw the leaves
tree_turtle.color("green")
tree_turtle.begin_fill()
tree_turtle.penup()
tree_turtle.goto(-50, 0)
tree_turtle.pendown()
tree_turtle.circle(50) # Bottom circle of leaves
tree_turtle.end_fill()

tree_turtle.begin_fill()
tree_turtle.penup()
tree_turtle.goto(-40, 50)
tree_turtle.pendown()
tree_turtle.circle(40) # Middle circle of leaves
tree_turtle.end_fill()

tree_turtle.begin_fill()
tree_turtle.penup()
tree_turtle.goto(-30, 90)
tree_turtle.pendown()
tree_turtle.circle(30) # Top circle of leaves
tree_turtle.end_fill()

# Hide the turtle and complete
tree_turtle.hideturtle()
turtle.done()
