# https://gist.github.com/thr0wn/f80eb02b3e25742aece046f075bb0370

import turtle
import math


def mandelbrot(z , c , n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c


# screen size (in pixels)
screenx, screeny = 800, 600

# complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)

# discretization step
step = 2

# turtle config
turtle.tracer(0, 0)
turtle.bgcolor("#010f7c")
screen = turtle.Screen()
screen.title("Mandelbrot Fractal (discretization step = %d)" % (int(step)))
mTurtle = turtle.Turtle()
mTurtle.penup()
mTurtle.shape("turtle")

# px * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny

# plot
min_x = int(-screenx / 2)
max_x = int(screenx / 2)

min_y = int(-screeny / 2)
max_y = int(screeny / 2)


for px in range(min_x, max_x, int(step)):
    for py in range(min_y, max_y, int(step)):
        x, y = px * pixelToX, py * pixelToY
        m =  mandelbrot(0, x + 1j * y)
        if not math.isnan(m.real):
            color = [abs(math.sin(m.imag)) for i in range(3)]
            mTurtle.color(color)
            mTurtle.dot(2.4, color)
            mTurtle.goto(px, py)
    turtle.update()

turtle.mainloop()