import tkinter as tk
import math
def flag():
    window=tk.Tk()#creating the window
    window.geometry("600x400")#setting window size
    window.title("Türk Bayrağı")#setting window title
    window.resizable(False,False)#makes window non-resizable

    #codes of the star
    r=50#radius
    x=294.3#starting point in x axis 
    y=200#starting point in y axis
    #5 dots of the star
    dot1x=x+(r*math.cos(math.radians(36)))
    dot1y=y-(r*math.sin(math.radians(36)))
    dot2x=x-(r*math.cos(math.radians(72)))
    dot2y=y-(r*math.sin(math.radians(72)))
    dot3x=x-(r*math.cos(math.radians(0)))
    dot3y=y-(r*math.sin(math.radians(0)))
    dot4x=x-(r*math.cos(math.radians(72)))
    dot4y=y+(r*math.sin(math.radians(72)))
    dot5x=x+(r*math.cos(math.radians(36)))
    dot5y=y+(r*math.sin(math.radians(36)))




    w=tk.Canvas(window,width=1000,height=1000,background="#E30A17")
    w.pack()
    w.create_oval(266,100,66,300,outline="white",fill="white")#outer(white) circle
    w.create_oval(111,120,271,280,outline="#E30A17",fill="#E30A17")#inner(red) circle
    w.create_polygon(dot1x,dot1y,dot4x,dot4y,dot2x,dot2y,dot5x,dot5y,dot3x,dot3y,outline="white",fill="white")#star

    window.mainloop()#maintain the window
flag()