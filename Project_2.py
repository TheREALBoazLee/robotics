def command():
  webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ') 

from tkinter import *
import webbrowser

root = Tk()
root.title("anything random")

btn = Button(root, text="press me", command=command)
btn.pack()

root.mainloop()
