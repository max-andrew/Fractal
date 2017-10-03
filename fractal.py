# Maxwell Andrew
# Feb 5, 2015
# Recursively draw a fractal bubble pattern

from Tkinter import *

def draw_bubbles(canvas,x1,y1,x2,y2,nlevels):
    if nlevels>0:
        draw_bubbles(canvas,x1,y1,(x1+x2)/2,(y2+y1)/2,nlevels-1)
        draw_bubbles(canvas,(x1+x2)/2,y1,x2,(y1+y2)/2,nlevels-1)
        draw_bubbles(canvas,x1,(y1+y2)/2,(x1+x2)/2,y2,nlevels-1)
        draw_bubbles(canvas,(x1+x2)/2,(y1+y2)/2,x2,y2,nlevels-1)
        canvas.create_oval((3*x1+x2)/4,(3*y1+y2)/4,x2-(x2-x1)/4,(y1+3*y2)/4,fill='red')

HEIGHT = 512
WIDTH = 512

window=Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT,highlightthickness=0,bg='blue')
canvas.grid(row=0,column=0)

fracDegs = raw_input('Enter level of fractals: ')
fracDegs = int(fracDegs)

draw_bubbles(canvas,0,0,WIDTH,HEIGHT,fracDegs)

window.mainloop()
