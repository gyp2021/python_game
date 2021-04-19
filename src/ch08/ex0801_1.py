import tkinter

timer = 0

def count_up():
    global timer
    timer = timer + 1
    label["text"] = timer
    root.after(1000, count_up)

root = tkinter.Tk()
label = tkinter.Label(root, font=("Times New Roman", 80))
label.pack()

root.after(1000, count_up)
root.mainloop()
