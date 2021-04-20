import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

cx = 1
cy = 1
def main_proc():
    global cx, cy
    if key == "Up" and maze[cy - 1][cx] == 0:
        cy = cy - 1
    if key == "Down" and maze[cy + 1][cx] == 0:
        cy = cy + 1
    if key == "Left" and maze[cy][cx - 1] == 0:
        cx = cx - 1
    if key == "Right" and maze[cy][cx + 1] == 0:
        cx = cx + 1

    canvas.coords("CAT", cx * 80 + 40, cy * 80 + 40)
    root.after(200, main_proc)

root = tkinter.Tk()
root.title("미로 고양이")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tkinter.Canvas(root, width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill="skyblue", width=0)

img = tkinter.PhotoImage(file="d:\github\gyp2021\python_game\src\ch08\mimi_s.png")
canvas.create_image(cx * 80 + 40, cy * 80 + 40, image=img, tag="CAT")

main_proc()

root.mainloop()
