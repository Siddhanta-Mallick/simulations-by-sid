from tkinter import *
import math
HEIGHT = 700
WIDTH = HEIGHT
ORIGIN_X = WIDTH / 2
ORIGIN_Y = HEIGHT / 2
VELOCITY = 10
GRAVITY_ACCELARATION = 0.1
DAMPING_FACTOR = 1
# DAMPING_FACTOR = 0.9999
BOB_SIZE = 10

LENGTH = 100

ANGLE =  - math.pi/4

ANGULAR_VELOCITY = 0
ANGULAR_ACCELARATION = 0

win = Tk()
win.title("Simple Pendulum")
win.geometry("700x700+50+50")
win.resizable(False, False)

canvas = Canvas(win, height=700, width=700)
canvas.pack()

def environmentLoop(ANGLE, ANGULAR_VELOCITY, ANGULAR_ACCELARATION):
    global GRAVITY_ACCELARATION
    global LENGTH
    global DAMPING_FACTOR
    
    ANGULAR_ACCELARATION = - (GRAVITY_ACCELARATION / LENGTH) * math.sin(ANGLE)
    ANGULAR_VELOCITY +=ANGULAR_ACCELARATION
    ANGULAR_VELOCITY *= DAMPING_FACTOR
    ANGLE += ANGULAR_VELOCITY
    bob_position_x = LENGTH * math.sin(ANGLE)
    bob_position_y = LENGTH * math.cos(ANGLE)
    
    canvas.delete("rope")
    canvas.delete("bob")
    canvas.create_line((ORIGIN_X,ORIGIN_Y),
                       ((ORIGIN_X + bob_position_x),(ORIGIN_Y + bob_position_y)),
                       tags="rope")
    
    canvas.create_oval((ORIGIN_X + bob_position_x - BOB_SIZE),
                       (ORIGIN_Y + bob_position_y - BOB_SIZE),
                       (ORIGIN_X + bob_position_x + BOB_SIZE),
                       (ORIGIN_Y + bob_position_y + BOB_SIZE),
                       fill="black",
                       tags="bob")
    
    win.after(VELOCITY,environmentLoop, ANGLE, ANGULAR_VELOCITY, ANGULAR_ACCELARATION)

environmentLoop(ANGLE, ANGULAR_VELOCITY, ANGULAR_ACCELARATION)

win.mainloop()