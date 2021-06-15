#Librerías
from tkinter import *
from PIL import ImageTk, Image
from random import randint

numero=1

def cargar(dificultad):
    """
    Entradas: dificultad (string 'Facil', Normal, Dificil)
    Salidas: pass
    Función: Cargar los niveles
    """
    base=open(str('Niveles/'+dificultad+'/'+str(randint(1,3))+'.txt'), 'r', encoding='utf-8')
    numlineas=base.readlines()
    base.seek(0)
    nums=[]
    cmps=[]
    for linea in numlineas:
        for i in linea.strip():
            if i.isdigit():
                nums.append(i)
            else:
                cmps.append(i)
    counter=0
    for i in range(9):
        for j in range(9):
            if i%2==1 or j%2==1:
                if cmps[counter]=='.':
                    imagen=imgN
                elif cmps[counter]=='A':
                    imagen=imgA
                elif cmps[counter]=='B':
                    imagen=imgB
                elif cmps[counter]=='C':
                    imagen=imgC
                else:
                    imagen=imgD
                counter+=1
                LabelCmp= Label(FrameJuego, image=imagen, bg='#b97a57',  highlightthickness = 0)
                LabelCmp.grid(row=i, column=j)
    for i in range(0,25):
        if   nums[i]=='1':
            casillas[i].config(image=imgB1_)
        elif nums[i]=='2':
            casillas[i].config(image=imgB2_)
        elif nums[i]=='3':
            casillas[i].config(image=imgB3_)
        elif nums[i]=='4':
            casillas[i].config(image=imgB4_)
        elif nums[i]=='5':
            casillas[i].config(image=imgB5_)
        else:
            casillas[i].config(image=imgB0)
def switch(num):
    """
    Entradas: num (un entero del 1 al 5)
    Salidas: la global numero
    Función: Cambiar de numero
    """
    global numero
    numero=num
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

def apuntar(self, posicion):
    """
    Entradas: Casilla a cambiar, posicion de la casilla.
    Salidas: None
    Función: Pone el numero en el tablero
             Hará alguna función con el registro de la pila, de momento pass
    """
    print(posicion)
    if numero==1:
        self.config(image=imgB1)
    elif numero==2:
        self.config(image=imgB2)
    elif numero==3:
        self.config(image=imgB3)    
    elif numero==4:
        self.config(image=imgB4)
    else:
        self.config(image=imgB5)

#Objetos de ventana
ventana = Tk()
frame = Frame(ventana)

FrameOpciones = Frame(frame)
FrameNums = Frame(frame)
FrameJuego = Frame(frame, bg='#b97a57')

#Cambios a ventana
ventana.title('Futoshiki')

#Imágenes

imgTitulo    = ImageTk.PhotoImage(Image.open('images/title.png').resize((448, 152), Image.NONE))

imgJugar     = ImageTk.PhotoImage(Image.open('images/jugar.png').resize((147, 57), Image.NONE))
imgDeshacer  = ImageTk.PhotoImage(Image.open('images/volver.png').resize((147, 57), Image.NONE))
imgTerminar  = ImageTk.PhotoImage(Image.open('images/juzgar.png').resize((147, 57), Image.NONE))
imgReiniciar = ImageTk.PhotoImage(Image.open('images/borrar.png').resize((147, 57), Image.NONE))
imgTop       = ImageTk.PhotoImage(Image.open('images/top.png').resize((147, 57), Image.NONE))

img1         = ImageTk.PhotoImage(Image.open('images/Numeros/1.png').resize((50, 50), Image.NONE))
img2         = ImageTk.PhotoImage(Image.open('images/Numeros/2.png').resize((50, 50), Image.NONE))
img3         = ImageTk.PhotoImage(Image.open('images/Numeros/3.png').resize((50, 50), Image.NONE))
img4         = ImageTk.PhotoImage(Image.open('images/Numeros/4.png').resize((50, 50), Image.NONE))
img5         = ImageTk.PhotoImage(Image.open('images/Numeros/5.png').resize((50, 50), Image.NONE))

img1_         = ImageTk.PhotoImage(Image.open('images/Numeros/1_.png').resize((50, 50), Image.NONE))
img2_         = ImageTk.PhotoImage(Image.open('images/Numeros/2_.png').resize((50, 50), Image.NONE))
img3_         = ImageTk.PhotoImage(Image.open('images/Numeros/3_.png').resize((50, 50), Image.NONE))
img4_         = ImageTk.PhotoImage(Image.open('images/Numeros/4_.png').resize((50, 50), Image.NONE))
img5_         = ImageTk.PhotoImage(Image.open('images/Numeros/5_.png').resize((50, 50), Image.NONE))

imgB0         = ImageTk.PhotoImage(Image.open('images/Bloques/0.png').resize((50, 50), Image.NONE))
imgB1         = ImageTk.PhotoImage(Image.open('images/Bloques/1.png').resize((50, 50), Image.NONE))
imgB2         = ImageTk.PhotoImage(Image.open('images/Bloques/2.png').resize((50, 50), Image.NONE))
imgB3         = ImageTk.PhotoImage(Image.open('images/Bloques/3.png').resize((50, 50), Image.NONE))
imgB4         = ImageTk.PhotoImage(Image.open('images/Bloques/4.png').resize((50, 50), Image.NONE))
imgB5         = ImageTk.PhotoImage(Image.open('images/Bloques/5.png').resize((50, 50), Image.NONE))

imgB1_        = ImageTk.PhotoImage(Image.open('images/Bloques/1_.png').resize((50, 50), Image.NONE))
imgB2_        = ImageTk.PhotoImage(Image.open('images/Bloques/2_.png').resize((50, 50), Image.NONE))
imgB3_        = ImageTk.PhotoImage(Image.open('images/Bloques/3_.png').resize((50, 50), Image.NONE))
imgB4_        = ImageTk.PhotoImage(Image.open('images/Bloques/4_.png').resize((50, 50), Image.NONE))
imgB5_        = ImageTk.PhotoImage(Image.open('images/Bloques/5_.png').resize((50, 50), Image.NONE))

imgN        = ImageTk.PhotoImage(Image.open('images/Bloques/..png'))
imgA        = ImageTk.PhotoImage(Image.open('images/Bloques/A.png'))
imgB        = ImageTk.PhotoImage(Image.open('images/Bloques/B.png'))
imgC        = ImageTk.PhotoImage(Image.open('images/Bloques/C.png'))
imgD        = ImageTk.PhotoImage(Image.open('images/Bloques/D.png'))

#Labels
LblTitulo =  Label(frame, image=imgTitulo, background='light gray')

#casillas
BotJugar = Button(FrameOpciones, image=imgJugar,  highlightthickness = 0, bd = 0, command=lambda:cargar('Facil'))
BotDeshacer = Button(FrameOpciones, image=imgDeshacer,  highlightthickness = 0, bd = 0)
BotTerminar = Button(FrameOpciones, image=imgTerminar,  highlightthickness = 0, bd = 0)
BotReiniciar = Button(FrameOpciones, image=imgReiniciar,  highlightthickness = 0, bd = 0)
BotTop = Button(FrameOpciones, image=imgTop,  highlightthickness = 0, bd = 0)

Bot1 = Button(FrameNums, image=img1_,  highlightthickness = 0, bd = 0, command=lambda:switch(1))
Bot2 = Button(FrameNums,  image=img2,  highlightthickness = 0, bd = 0, command=lambda:switch(2))
Bot3 = Button(FrameNums,  image=img3,  highlightthickness = 0, bd = 0, command=lambda:switch(3))
Bot4 = Button(FrameNums,  image=img4,  highlightthickness = 0, bd = 0, command=lambda:switch(4))
Bot5 = Button(FrameNums,  image=img5,  highlightthickness = 0, bd = 0, command=lambda:switch(5))

Bot00 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot00, 0))
Bot01 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot01, 1))
Bot02 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot02, 2))
Bot03 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot03, 3))
Bot04 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot04, 4))
Bot10 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot10, 5))
Bot11 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot11, 6))
Bot12 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot12, 7))
Bot13 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot13, 8))
Bot14 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot14, 9))
Bot20 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot20, 10))
Bot21 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot21, 11))
Bot22 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot22, 12))
Bot23 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot23, 13))
Bot24 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot24, 14))
Bot30 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot30, 15))
Bot31 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot31, 16))
Bot32 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot32, 17))
Bot33 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot33, 18))
Bot34 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot34, 19))
Bot40 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot40, 20))
Bot41 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot41, 21))
Bot42 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot42, 22))
Bot43 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot43, 23))
Bot44 = Button(FrameJuego, image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0, command=lambda:apuntar(Bot44, 24))

casillas=(
Bot00,Bot01,Bot02,Bot03,Bot04,
Bot10,Bot11,Bot12,Bot13,Bot14,
Bot20,Bot21,Bot22,Bot23,Bot24,
Bot30,Bot31,Bot32,Bot33,Bot34,
Bot40,Bot41,Bot42,Bot43,Bot44)
#Posiciones
LblTitulo.grid(row = 0, column=0, columnspan=6)

FrameJuego.grid(row=1, column=0, columnspan=6)
FrameNums.grid(row=1, column=5)
FrameOpciones.grid(row=2, column=0, columnspan=6)

#Bloques
for i in range(9):
    for j in range(9):
        if i%2==1 or j%2==1:
            LabelCmp= Label(FrameJuego, image=imgN, bg='#b97a57',  highlightthickness = 0)
            LabelCmp.grid(row=i, column=j)

Bot00.grid(row=0, column=0)
Bot01.grid(row=0, column=2)
Bot02.grid(row=0, column=4)
Bot03.grid(row=0, column=6)
Bot04.grid(row=0, column=8)
Bot10.grid(row=2, column=0)
Bot11.grid(row=2, column=2)
Bot12.grid(row=2, column=4)
Bot13.grid(row=2, column=6)
Bot14.grid(row=2, column=8)
Bot20.grid(row=4, column=0)
Bot21.grid(row=4, column=2)
Bot22.grid(row=4, column=4)
Bot23.grid(row=4, column=6)
Bot24.grid(row=4, column=8)
Bot30.grid(row=6, column=0)
Bot31.grid(row=6, column=2)
Bot32.grid(row=6, column=4)
Bot33.grid(row=6, column=6)
Bot34.grid(row=6, column=8)
Bot40.grid(row=8, column=0)
Bot41.grid(row=8, column=2)
Bot42.grid(row=8, column=4)
Bot43.grid(row=8, column=6)
Bot44.grid(row=8, column=8)

#Numeros
Bot1.grid(row=0, column=0)
Bot2.grid(row=1, column=0)
Bot3.grid(row=2, column=0)
Bot4.grid(row=3, column=0)
Bot5.grid(row=4, column=0)

#Posición de casillas

BotJugar.grid(row=0, column=0)
BotDeshacer.grid(row=0, column=1)
BotTerminar.grid(row=0, column=2)
BotReiniciar.grid(row=0, column=3)
BotTop.grid(row=0, column=4)

#Empaqutados
frame.pack()

#Loop
ventana.mainloop()