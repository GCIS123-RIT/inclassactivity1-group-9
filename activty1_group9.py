"""
ALI jouni: fixed mistakes
Ali almhuairi: added comments
Farah ottor: added functions
This module's goal is to finish the drawing of the three shapes—hexagon,circle, and square—by using user input.
This will display the result in three distinct rows with the certain colors for the border and fill in that the user selected.

"""
from turtle import Screen, Turtle

def setPos(fish, x, y):
  

    # Lift the pen to avoid drawing while moving to the specified position
    fish.up()

    
    fish.goto(x,y)

def mv_fd_rt(fish, fd, rg):
  

    # Move the turtle forward by the specified distance
    fish.forward(fd)

    # Rotate the turtle to the right by the specified angle
    fish.right(rg)

def next_shape(fish):
   

    # Lift the pen and move the turtle forward to create space between shapes
    fish.up()
    fish.forward(100)
    fish.down()

def hexagon(fish, hexa_color, border_color):

    # Lower the turtle pen to start drawing
    fish.down()

    
    # Begin filling the hexagon with the specified fill and border colors
    fish.begin_fill()
    fish.color(border_color, hexa_color)

    # Define the angles and distance for drawing a hexagon
    hexa_right = 60
    hexa_forward = 50

    # Draw the hexagon by moving the turtle forward and turning right six times
    mv_fd_rt(fish, hexa_forward, hexa_right)
    mv_fd_rt(fish, hexa_forward, hexa_right)
    mv_fd_rt(fish, hexa_forward, hexa_right)
    mv_fd_rt(fish, hexa_forward, hexa_right)
    mv_fd_rt(fish, hexa_forward, hexa_right)
    mv_fd_rt(fish, hexa_forward, hexa_right)

    # End filling the hexagon
    fish.end_fill()

def circle(fish, circle_color, border_color):
 

    # Lower the turtle pen to start drawing
    fish.down()

    # Begin filling the circle with the specified fill and border colors
    fish.begin_fill()
    fish.color(border_color, circle_color)

    # Draw the circle with radius -47 (negative radius for clockwise direction)
    fish.circle(-47)

    # End filling the circle
    fish.end_fill()

def square(fish, square_color, border_color):
    
    
    # Lower the turtle pen to start drawing
    fish.down()

    # Begin filling the square with the specified fill and border colors
    fish.begin_fill()
    fish.color(border_color, square_color)

    # Define the angles and distance for drawing a square
    square_right = 90
    square_forward = 90

    # Draw the square by moving the turtle forward and turning right four times
    mv_fd_rt(fish, square_forward, square_right)
    mv_fd_rt(fish, square_forward, square_right)
    mv_fd_rt(fish, square_forward, square_right)
    mv_fd_rt(fish, square_forward, square_right)

    # End filling the square
    fish.end_fill()


def pattern(fish, hexa_color, circle_color, square_color, border_color):

    hexagon(fish, hexa_color, border_color) 

    # Move the turtle to the next position
    next_shape(fish) 

    # Move the turtle forward to create space between the hexagon and circle 
    fish.up()  
    fish.forward(60)
    fish.down()

    #Draw a circle with the specified fill and border color
    circle(fish, circle_color, border_color)

    # Move the turtle to the next position
    next_shape(fish) 

    #Draw a square with the specified fill and border color
    square(fish, square_color, border_color)

def main():

    # Prompt the user to input the color for the hexagon
    hexa_fill = input("Enter the Hexagon Color: ")

    # Prompt the user to input the color for the circle
    circle_fill = input("Enter The Circle Color: ")

    # Prompt the user to input the color for the square
    square_fill = input("Enter The Square Color: ")

    # Prompt the user to input the color for the border of the shapes
    border_color = input("Enter The Border Color: ")

    # Create a variable 'wind' to represent the screen where the drawing will be displayed
    wind = Screen()

    # Create a variable 'fish' to represent the turtle
    fish = Turtle() 

    # Set the turtle's shape to "turtle"
    fish.shape("turtle")

    # Set the turtle's drawing speed to 9
    fish.speed(9)

    # Specifying the title of the window
    wind.title("GROUP 9 ACTIVITY 1") 

    # Specifying the background color
    wind.bgcolor("black")
    
   

    # Set the initial position for drawing the first pattern
    x = -300 
    y = 250 
    setPos(fish, x, y) 

    pattern(fish, hexa_fill, circle_fill, square_fill, border_color)

    # Set the initial position for drawing the second pattern
    x = -200
    y = 100
    setPos(fish, x, y)

    pattern(fish, hexa_fill, circle_fill, square_fill, border_color) 
 
    # Set the initial position for drawing the third pattern
    x = -100
    y = -50
    setPos(fish, x, y)

    pattern(fish, hexa_fill, circle_fill, square_fill, border_color) 

    #hide the turtle cursor
    fish.hideturtle()

    fish.up()

 #Wait for the user to click on the window to exit
    wind.exitonclick()

    
main()