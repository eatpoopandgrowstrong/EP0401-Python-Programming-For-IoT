'''
from tkinter import *

ws = Tk()
ws.title('PythonGuides')


img = PhotoImage(file='Dumpsterfireproject.png')
Label(ws,image=img).pack()

ws.mainloop() 
'''

'''

def main():
    pass




if __name__ == "__main__":
    
    main()
'''

import tkinter as tk
from PIL import Image, ImageTk

def change_pic():
    vlabel.configure(image=root.photo1)
    print ("updated")

root = tk.Tk()

photo = 'dumpsterfire.jpg'
photo1 = "Dumpsterfireproject.png"
root.photo = ImageTk.PhotoImage(Image.open(photo))
root.photo1 = ImageTk.PhotoImage(Image.open(photo1))

vlabel=tk.Label(root,image=root.photo)
vlabel.pack()

b2=tk.Button(root,text="Capture",command=change_pic)
b2.pack()

root.mainloop()