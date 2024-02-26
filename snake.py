# import modules necessary for the game
import random
import curses

# initialize the curses library to create our screen
screen = curses.initscr()

# hide the mouse cursor
curses.curs_set(0)

# getmax screen height and width
screen_height , screen_width = screen.getmaxyx()

# create a new window
window = curses.newwin(screen_height,screen_width,0,0)

# allow window to recieve input from keyboard
window.keypad(1)

# set the delay for updating the screen 
window.timeout(100)

# set the x,y coordinates of the initial position of snake's head
snk_y = screen_height//2
snk_x = screen_width//4

# define the initial postition of snake body
snake = [
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2],
]

# create the food in the middle of window
food = [screen_height//2, screen_width//2]
# add the food by using PI character from curses module
window.addch(food[0],food[1], curses.ACS_PI)

# set initial movement direction to right

# create game loop that loops forever untill player loses or quits

# get the next key that will be pressed by user

# if user doesn't input anything, key remains same, else key will be set 
# to the new pressed key