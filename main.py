#Librerías
from tkinter import *
from PIL import ImageTk, Image

def switch(num):
    Bot1.config(image=img1)
    Bot2.config(image=img2)
    Bot3.config(image=img3)
    Bot4.config(image=img4)
    Bot5.config(image=img5)
    if num==1:
        Bot1.config(image=img1_)
    elif num==2:
        Bot2.config(image=img2_)
    elif num==3:
        Bot3.config(image=img3_)
    elif num==4:
        Bot4.config(image=img4_)
    else:
        Bot5.config(image=img5_)
    return

#Objetos de ventana
ventana = Tk()
frame = Frame(ventana)

FrameOpciones = Frame(frame)
FrameJuego = Frame(frame)

#Cambios a ventana
ventana.title('Futoshiki')

#Imágenes

imgTitulo    = ImageTk.PhotoImage(Image.open('images/title.png').resize((448, 152), Image.NONE))

imgJugar     = ImageTk.PhotoImage(Image.open('images/jugar.png').resize((147, 57), Image.NONE))
imgDeshacer  = ImageTk.PhotoImage(Image.open('images/volver.png').resize((147, 57), Image.NONE))
imgTerminar  = ImageTk.PhotoImage(Image.open('images/juzgar.png').resize((147, 57), Image.NONE))
imgReiniciar = ImageTk.PhotoImage(Image.open('images/borrar.png').resize((147, 57), Image.NONE))
imgTop       = ImageTk.PhotoImage(Image.open('images/top.png').resize((147, 57), Image.NONE))

img1         = ImageTk.PhotoImage(Image.open('images/Numeros/1.png').resize((75, 75), Image.NONE))
img2         = ImageTk.PhotoImage(Image.open('images/Numeros/2.png').resize((75, 75), Image.NONE))
img3         = ImageTk.PhotoImage(Image.open('images/Numeros/3.png').resize((75, 75), Image.NONE))
img4         = ImageTk.PhotoImage(Image.open('images/Numeros/4.png').resize((75, 75), Image.NONE))
img5         = ImageTk.PhotoImage(Image.open('images/Numeros/5.png').resize((75, 75), Image.NONE))

img1_         = ImageTk.PhotoImage(Image.open('images/Numeros/1_.png').resize((75, 75), Image.NONE))
img2_         = ImageTk.PhotoImage(Image.open('images/Numeros/2_.png').resize((75, 75), Image.NONE))
img3_         = ImageTk.PhotoImage(Image.open('images/Numeros/3_.png').resize((75, 75), Image.NONE))
img4_         = ImageTk.PhotoImage(Image.open('images/Numeros/4_.png').resize((75, 75), Image.NONE))
img5_         = ImageTk.PhotoImage(Image.open('images/Numeros/5_.png').resize((75, 75), Image.NONE))

imgB0         = ImageTk.PhotoImage(Image.open('images/Bloques/0.png').resize((75, 75), Image.NONE))
imgB1         = ImageTk.PhotoImage(Image.open('images/Bloques/1.png').resize((75, 75), Image.NONE))
imgB2         = ImageTk.PhotoImage(Image.open('images/Bloques/2.png').resize((75, 75), Image.NONE))
imgB3         = ImageTk.PhotoImage(Image.open('images/Bloques/3.png').resize((75, 75), Image.NONE))
imgB4         = ImageTk.PhotoImage(Image.open('images/Bloques/4.png').resize((75, 75), Image.NONE))
imgB5         = ImageTk.PhotoImage(Image.open('images/Bloques/5.png').resize((75, 75), Image.NONE))


imgB1_        = ImageTk.PhotoImage(Image.open('images/Bloques/1_.png').resize((75, 75), Image.NONE))
imgB2_        = ImageTk.PhotoImage(Image.open('images/Bloques/2_.png').resize((75, 75), Image.NONE))
imgB3_        = ImageTk.PhotoImage(Image.open('images/Bloques/3_.png').resize((75, 75), Image.NONE))
imgB4_        = ImageTk.PhotoImage(Image.open('images/Bloques/4_.png').resize((75, 75), Image.NONE))
imgB5_        = ImageTk.PhotoImage(Image.open('images/Bloques/5_.png').resize((75, 75), Image.NONE))

#Labels
LblTitulo =  Label(frame, image=imgTitulo, background='light gray')

#Botones
BotJugar = Button(FrameOpciones, image=imgJugar,  highlightthickness = 0, bd = 0)
BotDeshacer = Button(FrameOpciones, image=imgDeshacer,  highlightthickness = 0, bd = 0)
BotTerminar = Button(FrameOpciones, image=imgTerminar,  highlightthickness = 0, bd = 0)
BotReiniciar = Button(FrameOpciones, image=imgReiniciar,  highlightthickness = 0, bd = 0)
BotTop = Button(FrameOpciones, image=imgTop,  highlightthickness = 0, bd = 0)

Bot1 = Button(FrameJuego, image=img1,  highlightthickness = 0, bd = 0, command=lambda:switch(1))
Bot2 = Button(FrameJuego, image=img2,  highlightthickness = 0, bd = 0, command=lambda:switch(2))
Bot3 = Button(FrameJuego, image=img3,  highlightthickness = 0, bd = 0, command=lambda:switch(3))
Bot4 = Button(FrameJuego, image=img4,  highlightthickness = 0, bd = 0, command=lambda:switch(4))
Bot5 = Button(FrameJuego, image=img5,  highlightthickness = 0, bd = 0, command=lambda:switch(5))

for y in range(5):
    for x in range(5):
        BotBox= Button(FrameJuego, image=imgB0,  highlightthickness = 0, bd = 0)
        BotBox.grid(row=y, column=x)

#Posiciones
LblTitulo.grid(row = 0, column=0, columnspan=6)

FrameJuego.grid(row=1, column=0, columnspan=6)
Bot1.grid(row=0, column=6)
Bot2.grid(row=1, column=6)
Bot3.grid(row=2, column=6)
Bot4.grid(row=3, column=6)
Bot5.grid(row=4, column=6)

#Posición de botones
FrameOpciones.grid(row=2, column=0, columnspan=6)

BotJugar.grid(row=0, column=0)
BotDeshacer.grid(row=0, column=1)
BotTerminar.grid(row=0, column=2)
BotReiniciar.grid(row=0, column=3)
BotTop.grid(row=0, column=4)

#Empaqutados
frame.pack()

#Loop
ventana.mainloop()