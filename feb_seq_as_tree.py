import tkinter as tk


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def draw_tree(canvas, x, y, width, height, level):
    if level == 0:
        return
    x1 = x - width / 2
    y1 = y + height
    x2 = x + width / 2
    y2 = y + height
    x3 = x
    y3 = y
    canvas.create_line(x1, y1, x3, y3, fill="#00bfff")
    canvas.create_line(x3, y3, x2, y2, fill="#00bfff")
    draw_tree(canvas, x1, y1, width / 2, height, level - 1)
    draw_tree(canvas, x2, y2, width / 2, height, level - 1)


window = tk.Tk()
window.title("Fibonacci Sequence")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()


def draw():
    canvas.delete("all")
    sequence = list(fibonacci(10))
    draw_tree(canvas, 200, 10, 100, 80, len(sequence))


button = tk.Button(window, text="Draw Fibonacci Tree", command=draw)
button.pack()

window.mainloop()
