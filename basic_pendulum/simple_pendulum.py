from tkinter import *
import math

# Environment
PENDULUM_COUNT = 0
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700

ORIGIN_X = WINDOW_WIDTH / 2
ORIGIN_Y = WINDOW_HEIGHT / 2

GRAVITY_ACCELERATION = 0.1

TIME = 15

# Pendulum Specs
LENGTH_DEFAULT = 200
BOB_RADIUS = 10
STARTING_ANGLE_DEFAULT = math.pi / 4
DAMPING_DEFAULT = 1 # No Damping

class Pendulum:
    def __init__(self, win = None, canvas = None, length = LENGTH_DEFAULT, starting_angle = STARTING_ANGLE_DEFAULT, damping = DAMPING_DEFAULT, color="black" ):
        global PENDULUM_COUNT
        PENDULUM_COUNT += 1
        self.win = win
        self.canvas = canvas
        self.id = PENDULUM_COUNT
        self.length = length
        self.angle = starting_angle
        self.angular_velocity = 0
        self.angular_acceleration = 0
        self.damping = damping
        self.color = color
    
    def start(self):
        global GRAVITY_ACCELERATION
        global BOB_RADIUS
        # Calculation Mechanics
        self.angular_acceleration = - (GRAVITY_ACCELERATION / self.length) * math.sin(self.angle)
        self.angular_velocity += self.angular_acceleration
        self.angular_velocity *= self.damping
        self.angle += self.angular_velocity
        
        # Bob position calculation
        bob_position_x = self.length * math.sin(self.angle)
        bob_position_y = self.length * math.cos(self.angle)
        
        # Display Mechanics
        self.canvas.delete(f"rope{self.id}")
        self.canvas.delete(f"bob{self.id}")
        self.canvas.create_line(
            (ORIGIN_X, ORIGIN_Y),
            (ORIGIN_X + bob_position_x, ORIGIN_Y + bob_position_y),
            tags=f"rope{self.id}",
            fill=self.color
        )
        self.canvas.create_oval(
            (ORIGIN_X + bob_position_x - BOB_RADIUS, ORIGIN_Y + bob_position_y - BOB_RADIUS),
            (ORIGIN_X + bob_position_x + BOB_RADIUS, ORIGIN_Y + bob_position_y + BOB_RADIUS),
            tags=f"bob{self.id}",
            fill=self.color
        )
        
        self.win.after(TIME , self.start)
        
win = Tk()
win.title("Simple Pendulum")
win.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+50+50")
win.resizable(False, False)

canvas = Canvas(win, height=700, width=700)
canvas.pack()

p1 = Pendulum(win, canvas,200, color="red")
p1.start()

p2 = Pendulum(win, canvas, 200, damping=0.999)
p2.start()


win.mainloop()