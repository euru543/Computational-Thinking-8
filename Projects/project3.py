import turtle, time, random
from utils import *
# -----------------------------
# Section 1 - Variables
# These are the starting positions for each sprite
# All sprites start in a straight line and do not overlap
x1 = -300
y1 = 100

x2 = -300
y2 = 30

x3 = -300
y3 = -40

x4 = -300
y4 = -110


# -----------------------------
# Section 2 - Setup
# Set the background and create the sprites
set_background("castle")

t1 = create_sprite("basketball", x1, y1)
t2 = create_sprite("basketball", x2, y2)
t3 = create_sprite("basketball", x3, y3)
t4 = create_sprite("basketball", x4, y4)


# -----------------------------
# Section 3 - Racing
# The for loop repeats 30 times to move the sprites forward
# Sprite 1 is fast
# Sprite 2 is slow
# Sprite 3 is the fastest
# Sprite 4 is medium speed

for i in range(30):
    x1 += 8    # player 1 is fast
    x2 += 4    # player 2 is slow
    x3 += 10   # player 3 is the fastest
    x4 += 6    # player 4 is medium speed

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# -----------------------------
# Section 4 - Winner
# These if statements check who went the farthest

if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("Player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("Player 3 wins!")
else:
    print("Player 4 wins!")
turtle.exitonclick()