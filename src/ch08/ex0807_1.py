import tkinter

cnt = 0
def main_proc():
    global cnt
    canvas.delete("PHOTO")
    canvas.create_image(400, 300, image=img_list[cnt], tag="PHOTO")
    cnt = cnt + 1
    if cnt >= 4:
       cnt = 0
    root.after(5000, main_proc)

root = tkinter.Tk()
root.title("디지털 액자")

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

img_list = [
    tkinter.PhotoImage(file="d:\github\gyp2021\python_game\src\ch08\cat00.png"),
    tkinter.PhotoImage(file="d:\github\gyp2021\python_game\src\ch08\cat01.png"),
    tkinter.PhotoImage(file="d:\github\gyp2021\python_game\src\ch08\cat02.png"),
    tkinter.PhotoImage(file="d:\github\gyp2021\python_game\src\ch08\cat03.png"),
]

main_proc()

root.mainloop()
