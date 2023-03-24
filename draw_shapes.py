import tkinter as tk
import math

# Create a Tkinter window
window = tk.Tk()
window.title("Beautiful Drawing")

# Define the draw function
def draw(canvas):
    # Clear the canvas
    canvas.delete("all")

    # Set the background color
    canvas.config(bg="#ffffff")

    # Set the dimensions of the canvas
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # Draw a circle
    x = width / 2
    y = height / 2
    r = min(width, height) / 2 - 10
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="#ffcccc")

    # Draw a spiral
    x = width / 2
    y = height / 2
    r = 10
    angle = 0
    while r < min(width, height) / 2:
        dx = r * math.cos(angle)
        dy = r * math.sin(angle)
        canvas.create_line(x, y, x + dx, y + dy, fill="#00bfff")
        x += dx
        y += dy
        r += 0.1
        angle += 0.1

    # Draw a star
    x = width / 2
    y = height / 2
    r = min(width, height) / 3
    points = []
    for i in range(5):
        angle = 2 * math.pi * i / 5
        dx = r * math.cos(angle)
        dy = r * math.sin(angle)
        points.append(x + dx)
        points.append(y + dy)
    canvas.create_polygon(points, fill="#ffffcc")

# Create a Tkinter canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Bind the draw function to the canvas
canvas.bind("<Configure>", lambda event: draw(canvas))

# Run the Tkinter event loop
window.mainloop()
