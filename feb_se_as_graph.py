import tkinter as tk


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def draw(canvas, sequence):
    x = 10
    y = 10
    for number in sequence:
        canvas.create_text(x, y, text=str(number), fill="#00bfff")
        x += 20
        y += 20


window = tk.Tk()
window.title("Fibonacci Sequence")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()


def draw_sequence():
    canvas.delete("all")
    sequence = list(fibonacci(10))
    draw(canvas, sequence)


button = tk.Button(window, text="Draw Fibonacci Sequence", command=draw_sequence)
button.pack()

window.mainloop()
