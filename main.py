from turtle import Turtle, Screen
import random

# Set up the screen dimensions and basic configuration
screen = Screen()
screen.setup(width=1000, height=800)

# Flag to check if the race has started
race_on = False

# Ask the user for their bet
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race?(\nRed, Orange, Yellow, Green, Blue, Purple)\nenter the color:"
)

# Define turtle colors and names
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_name = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial x and y coordinates for turtle placement & Create a list to store all turtle objects
x_coor = -485
y_coor = -100
ind = 0
all_turtle = []

# Create turtles, set their properties, and position them
for turtle in turtle_name:
    turtle = Turtle(shape="turtle")
    turtle.color(colors[ind])
    turtle.speed(12)
    ind += 1
    turtle.penup()
    turtle.goto(x=x_coor, y=y_coor)
    y_coor += 50
    all_turtle.append(turtle)

# Start the race if the user has placed a bet
if user_bet:
    race_on = True

# Run the race
while race_on:
    for turtle in all_turtle:
        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 480:
            # Stop the race & Get the color of the winning turtle
            race_on = False
            winner_turtle = turtle.pencolor()
            # Check if the user's bet matches the winning turtle
            if winner_turtle == user_bet:
                print(f"You've won. The winner turtle is {winner_turtle}.")
            else:
                print(f"You've lost. The winner turtle is {winner_turtle}.")

        # Move the turtle forward by a random distance
        race_pace = random.randint(0, 10)
        turtle.forward(race_pace)

# Exit the screen when clicked
screen.exitonclick()
