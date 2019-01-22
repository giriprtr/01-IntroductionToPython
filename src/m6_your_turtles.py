"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Kash
"""
########################################################################
#  Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
#  Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(5)
blue = rg.SimpleTurtle('turtle')
blue.pen = rg.Pen('blue', 3)
blue.speed = 20
red = rg.SimpleTurtle('turtle')
red.speed = 100
red.pen = rg.Pen('red', 0.5


blue.forward(5)
for k in range(100):
    n = 100 - k
    blue.left(45)
    blue.forward(n)

red.right(90)
red.forward(75)
for t in range(10000):
    n = 45 + t
    red.forward(100)
    red.right(n + t)
    red.forward(5 + t)
    red.left(t)
    red.forward(t)

window.close_on_mouse_click()