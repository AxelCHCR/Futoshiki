#Librerías
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from random import randint
from os import startfile

transcurrido=[0,0,0]
limite=[2,0,0]
ganaste=True
numero=1
nivel=[]
juego=[]
continuar=True
dificultad='Facil'
pila=[]
comparaciones=[]
tiempo='S'
top=()
ventanas=[]
nombre=''
cmps=[]

def cargar(numNivel):
    """
    E: Número del nivel (1 al 3)
    S: None
    Función: Inicia el juego
    """
    global transcurrido
    global nivel
    global juego
    global comparaciones
    global pila
    global ganaste
    global cmps

    ganaste=False
    nivel=[numNivel, [], dificultad, tiempo, limite]
    juego=[]
    pila=[]

    base=open(str('Niveles/'+dificultad+'/'+numNivel+'.txt'), 'r', encoding='utf-8')
    numlineas=base.readlines()
    base.seek(0)
    nums=[]
    cmps=[]
    for linea in numlineas:
        for i in linea.strip():
            if i.isdigit():
                nums.append(int(i))
            else:
                cmps.append(i)
    counter=0
    if len(comparaciones)!=0:
        for i in comparaciones:
            i.destroy()
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
                comparaciones.append(Label(frameJuego, image=imagen, bg='#b97a57',  highlightthickness = 0))
                comparaciones[-1].grid(row=i, column=j)
    for i in range(0,25):
        if   nums[i]==1:
            casillas[i].config(image=imgB1_)
        elif nums[i]==2:
            casillas[i].config(image=imgB2_)
        elif nums[i]==3:
            casillas[i].config(image=imgB3_)
        elif nums[i]==4:
            casillas[i].config(image=imgB4_)
        elif nums[i]==5:
            casillas[i].config(image=imgB5_)
        else:
            casillas[i].config(image=imgB0)
    juego=nums
    base=open(str('Niveles/'+dificultad+'/'+numNivel+'_.txt'), 'r', encoding='utf-8')
    numlineas=base.readlines()
    base.seek(0)
    for linea in numlineas:
        for i in linea.strip():
            nivel[1].append(int(i))
    if nivel[3]=='T':
        transcurrido=[limite[0], limite[1], limite[2]]
        segundos.config(text=str(transcurrido[2]))
    else:
        transcurrido=[0,0,-1]
        segundos.config(text=str(0))
    minutos.config(text=str(transcurrido[1]))
    horas.config(text=str(transcurrido[0]))
    print(cmps)
    return

def jugar():
    """
    E/S: None
    Función: Inicia el juego
    """
    if continuar and ganaste:
        ventana.config(bg='brown')
        EntryNombre.delete(0, 'end')
        frame.pack_forget()
        frameNombre.pack()
        cargar(str(randint(1,3)))
    return

def volver():
    """
    E/S: None
    Función: Quita la última acción.
    """
    global pila
    global juego
    if continuar:
        if len(pila)==0:
            print('nohay')
            return
        else:
            ultimo=pila.pop(-1)
        huboCambio=False

        for i in pila:
            if i[1]==ultimo[1]:
                juego[i[1]]=ultimo[0]
                huboCambio=True
                if i[0]==1:
                    casillas[ultimo[1]].config(image=imgB1)
                elif i[0]==2:
                    casillas[ultimo[1]].config(image=imgB2)
                elif i[0]==3:
                    casillas[ultimo[1]].config(image=imgB3) 
                elif i[0]==4:
                    casillas[ultimo[1]].config(image=imgB4)
                else:
                    casillas[ultimo[1]].config(image=imgB5)
        
        if huboCambio==False:
            juego[ultimo[1]]=0
            casillas[ultimo[1]].config(image=imgB0)
    return

def otro():
    """
    E/S: None
    Función: Cambia el nivel a otro de la misma dificultad
    """
    if continuar:
        if len(nivel)!=0:
            numNivel=nivel[0]
            while numNivel==nivel[0]:
                numNivel=str(randint(1,3))
            cargar(numNivel)
    return

def reiniciar():
    """
    E/S: None
    Función: Reinicia el nivel
    """
    if continuar:
        if len(nivel)!=0:
            cargar(nivel[0])
    return

def switch(num):
    """
    E: num (un entero del 1 al 5)
    S: la global numero
    Función: Cambiar de numero
    """
    global numero
    if continuar:
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

def esValido(posicion):
    """
    E: posicion
    S: Bool
    Función: Pone números rojos
    """
    global continuar

    def stop(e):
        """
        E: evento
        S: None
        Función: Quita la pausa y el numero rojo
        """
        global continuar
        LabelE.destroy()
        continuar=True
    if len(nivel)==0:
        return False
    if continuar:
        prueba=[]
        for i in juego:
            prueba.append(i)
        prueba[posicion] = numero

        for i in range(len(nivel[1])):
            if prueba[i]==0:
                pass
            elif prueba[i]!=nivel[1][i] or juego==prueba:
                if juego==prueba:
                    messagebox.showerror('Número ya correcto', 'Pusiste un numero que ya estaba correcto encima de otro.')
                    error=True
                else:
                    error=False
                    for i in range(5):
                        buffer=[]
                        for j in range(5):
                            buffer.append(prueba[i*5+j])
                        print(buffer)
                        for k in buffer:
                            if k!=0 and buffer.count(k)>1 and error==False:
                                messagebox.showerror('Número en fila', 'Ya había un número en la fila')
                                error=True
                        for j in range(5):
                            buffer.append(prueba[j*5+i])
                        print(buffer)
                        for k in buffer:
                            if k!=0 and buffer.count(k)>1 and error==False:
                                messagebox.showerror('Número en columna', 'Ya había un número en la columna')
                                error=True

                LabelE=Label(frameJuego, bg='#b97a57',  highlightthickness = 0)
                if numero==1:
                    LabelE.config(image=imgB1D)
                elif numero==2:
                    LabelE.config(image=imgB2D)
                elif numero==3:
                    LabelE.config(image=imgB3D)  
                elif numero==4:
                    LabelE.config(image=imgB4D)
                else:
                    LabelE.config(image=imgB5D)
                LabelE.grid(row=(posicion//5)*2, column=(posicion%5)*2)
                ventana.bind('<Return>', stop)
                continuar=False
                return False
        return True
    else:
        return False

def apuntar(self, posicion):
    """
    E: Casilla a cambiar, posicion de la casilla.
    S: None
    Función: Pone el numero en el tablero
             Hará alguna función con el registro de la pila, de momento pass
    """
    def win(e):
        """
        E: evento
        S: None
        Función: Quita la pantalla de victoria
        """
        frame.pack()
        frameVictoria.pack_forget()
        ventana.config(bg='#f0f0f0')
        return

    def record(rankig, nuevo):
        print(nivel[2])
        print(nuevo)
        if nivel[2]=='Facil':
            categoria=0
        elif nivel[2]=='Normal':
            categoria=1
        else:
            categoria=2
        for i in range(len(rankig[categoria])):
            t=rankig[categoria][i][1].split(':')
            print(rankig[categoria][i])
            if rankig[categoria][i]==('',''):
                print('Bruh')
                rankig[categoria].insert(i,(str(nombre), str(str(nuevo[0])+':'+str(nuevo[1])+':'+str(nuevo[2]))))
                rankig[categoria].pop()
                return rankig
            if nuevo[0]==int(t[0]):
                print('hora')
                if nuevo[1]==int(t[1]):
                    print('min')
                    if nuevo[2]<int(t[2]):
                        print('seg')
                        rankig[categoria].insert(i,(str(nombre), str(str(nuevo[0])+':'+str(nuevo[1])+':'+str(nuevo[2]))))
                        rankig[categoria].pop()
                        return rankig
                elif nuevo[1]<int(t[1]):
                    rankig[categoria].insert(i,(str(nombre), str(str(nuevo[0])+':'+str(nuevo[1])+':'+str(nuevo[2]))))
                    rankig[categoria].pop()
                    return rankig
            elif nuevo[0]<int(t[0]):
                rankig[categoria].insert(i,(str(nombre), str(str(nuevo[0])+':'+str(nuevo[1])+':'+str(nuevo[2]))))
                rankig[categoria].pop()
                return rankig
        return rankig

    global juego
    global pila
    global ganaste
    print(1)
    if ganaste:
        if nivel[3]=='T' and transcurrido==[0,0,0]:
            messagebox.showerror('¡Tiempo!','Se gastó el tiempo..')
        return
    else:
        if continuar and esValido(posicion):
            juego[posicion] = numero
            pila.append((numero, posicion))
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
            if nivel[1]==juego:
                ganaste=True
                frame.pack_forget()
                frameVictoria.pack()
                ventana.config(bg='orange')
                nota=[]
                if nivel[3]=='T':
                    nota=[nivel[4][0]-transcurrido[0], nivel[4][1]-transcurrido[1], nivel[4][2]-transcurrido[2]]
                else:
                    nota=[transcurrido[0], transcurrido[1], transcurrido[2]]
                LabelTiempo.config(text=str(nota[0])+':'+str(nota[1])+':'+str(nota[2]))

                ListaTop=open('futoshiki2021top10.dat', 'r', encoding='utf-8')
                numlineas=ListaTop.readlines()
                ListaTop.seek(0)
                lineas=[]
                top=[]
                for linea in numlineas:
                    if linea!='D:\n':
                        if ';' in linea:
                            lineas.append((linea.split(';')[0], linea.split(';')[1].replace('\n', '')))
                        else:
                            lineas.append(('',''))
                    else:
                        if len(lineas)!=0:
                            top.append(lineas)
                            lineas=[]
                top.append(lineas)
                print(top)
                record(top, nota)
                print(top)
                ListaTop=open('futoshiki2021top10.dat', 'w', encoding='utf-8')
                i=-1
                j=10
                for linea in range(33):
                    print(i, j)
                    if j==10:
                        if i==-1:
                            ListaTop.write('D:')
                        else:
                            ListaTop.write('\nD:')
                        i+=1
                        j=0
                    else:
                        ListaTop.write(str('\n'+top[i][j][0]+';'+top[i][j][1]))
                        j+=1
                ListaTop.close()
                LabelTiempo.pack()
                ventana.bind('<Return>', win)
    return

def iniciar():
    """
    E/S: None
    Función: Pone el numero en el tablero
    """
    global transcurrido
    global nombre
    nombre=str(EntryNombre.get())
    ventana.config(bg='#f0f0f0')
    frameNombre.pack_forget()
    frame.pack()
    if tiempo=='T':
        transcurrido=[limite[0], limite[1], limite[2]]
        segundos.config(text=str(transcurrido[2]))
    else:
        transcurrido=[0,0,-1]
    minutos.config(text=str(transcurrido[1]))
    horas.config(text=str(transcurrido[0]))
    
    return

def cronometro():
    """
    E/S: None
    Función: Mueve el reloj del juego.
    """
    global transcurrido
    global continuar
    global ganaste
    seg=transcurrido[2]
    minut=transcurrido[1]
    hora=transcurrido[0]
    if continuar and ganaste==False:
        if nivel[3]=='T':
            if hora+minut+seg>0:
                seg-=1
                if seg==-1:
                    if hora+minut>0:
                        seg=59
                        minut-=1
                        if minut==-1:
                            if hora>0:
                                minut=59
                                hora-=1
            else:
                ganaste=True
        else:
            seg+=1
            if seg==60:
                seg=0
                minut+=1
            if minut==60:
                minut=0
                hora+=1
            
        segundos.config(text=str(seg))
        minutos.config(text=str(minut))
        horas.config(text=str(hora))
    transcurrido[2]=seg
    transcurrido[1]=minut
    transcurrido[0]=hora
    frameReloj.after(1000, cronometro)
    return

def top10():
    def seguir():
        frame.pack()
        frameTop.pack_forget()
        ventana.config(bg='#f0f0f0')
    global top
    ventana.config(bg='yellow')
    frame.pack_forget()
    frameTop.pack()
    ListaTop=open('futoshiki2021top10.dat', 'r', encoding='utf-8')
    numlineas=ListaTop.readlines()
    ListaTop.seek(0)
    lineas=[]
    for linea in numlineas:
        if linea!='D:\n':
            if ';' in linea:
                lineas.append((linea.split(';')[0], linea.split(';')[1].replace('\n', '')))
            else:
                lineas.append(('',''))
    top=tuple(lineas)
    print(len(top))
    buffer=1
    for i in top:
        if buffer in [11,22]:
            buffer+=1
        LabelTn= Label(frameTop, text=i[0], font=('Segoe UI', 10), bg='yellow', highlightthickness = 0)
        LabelTt= Label(frameTop, text=i[1],font=('Segoe UI', 10), bg='yellow', highlightthickness = 0)
        LabelTn.grid(row=buffer, column=1, sticky=S)
        LabelTt.grid(row=buffer, column=2, sticky=S)
        buffer+=1
    BotSeguir=Button(frameTop, text='Seguir', command=seguir)
    BotSeguir.grid(row=buffer+1, column=0, columnspan=3, sticky=S)
    return

def configurar():
    def cambioDif(d):
        global dificultad
        dificultad=d
    def cambioReloj(r):
        global tiempo
        global limite
        tiempo=r
        if tiempo=='S':
            radSi.select()
            frameReloj.grid_forget()
            frameReloj.grid(row=3, column=0, columnspan=2, padx=20, pady=30)
        elif tiempo=='N':
            radNo.select()
            frameReloj.grid_forget()
        else:
            radT.select()
            frameReloj.grid_forget()
            frameReloj.grid(row=3, column=0, columnspan=2, padx=20, pady=30)
            print(int(cmbHoras.get()))
            limite=[int(cmbHoras.get()), int(cmbMinutos.get()), int(cmbSegundos.get())]
        return
    def cambioPanel(esDerecha):
        frameNums.grid_forget()
        if esDerecha:
            frameNums.grid(row=1, column=5)
        else:
            frameNums.grid(row=1, column=0)
        return
    def confirmar():
        cambioReloj(tiempo)
        vConfigurar.destroy()
        return
    global imgListo
    vConfigurar = Tk()
    ventanas.append(vConfigurar)
    vConfigurar.title('Configurar')
    frameTiempo = Frame(vConfigurar, bg='light yellow')

    LabelC=Label(vConfigurar, text='Dificultad')
    LabelC.grid(row=0, column=0, pady=(20,0))
    seleccionD=IntVar()
    radFacil=Radiobutton(vConfigurar, text='Fácil', variable=seleccionD, value=1, command=lambda:cambioDif('Facil'))
    radFacil.grid(row=0, column=1, pady=(20,0), sticky=W)
    radNormal=Radiobutton(vConfigurar, text='Normal', variable=seleccionD, value=2, command=lambda:cambioDif('Normal'))
    radNormal.grid(row=1, column=1, sticky=W)
    radDificil=Radiobutton(vConfigurar, text='Difícil', variable=seleccionD, value=3, command=lambda:cambioDif('Dificil'))
    radDificil.grid(row=2, column=1, sticky=W)
    radFacil.select()

    LabelC=Label(vConfigurar, text='Reloj')
    LabelC.grid(row=3, column=0, pady=(20,0))
    seleccionR=StringVar()
    radSi=Radiobutton(vConfigurar, text='Sí', variable=seleccionR, value='S', command=lambda:cambioReloj('S'))
    radSi.grid(row=3, column=1, pady=(20,0), sticky=W)
    radNo=Radiobutton(vConfigurar, text='No', variable=seleccionR, value='N', command=lambda:cambioReloj('N'))
    radNo.grid(row=4, column=1, sticky=W)
    radT=Radiobutton(vConfigurar, text='Timer', variable=seleccionR, value='T', command=lambda:cambioReloj('T'))
    radT.grid(row=5, column=1, sticky=W)
    radSi.select()

    frameTiempo.grid(row=3, column=2, rowspan=3, padx=20, pady=(20,0))
    Label(frameTiempo,           text='Horas',   font=('Segoe UI', 8), bg='light yellow',  highlightthickness = 0).grid(row=0, column=0)
    Label(frameTiempo,           text='Minutos', font=('Segoe UI', 8), bg='light yellow',  highlightthickness = 0).grid(row=0, column=1, padx=20, pady=10)
    Label(frameTiempo,           text='Segundos',font=('Segoe UI', 8), bg='light yellow',  highlightthickness = 0).grid(row=0, column=2)
    sesenta=[i for i in range(60)]
    tres=[i for i in range(3)]
    
    cmbHoras= ttk.Combobox(frameTiempo, value=tres)
    cmbHoras.current(0)
    cmbHoras.grid(row=1, column=0)
    cmbMinutos= ttk.Combobox(frameTiempo, value=sesenta)
    cmbMinutos.current(0)
    cmbMinutos.grid(row=1, column=1)
    cmbSegundos= ttk.Combobox(frameTiempo, value=sesenta)
    cmbSegundos.current(0)
    cmbSegundos.grid(row=1, column=2)

    LabelC=Label(vConfigurar, text='Panel de digitos')
    LabelC.grid(row=6, column=0, pady=(20,0))
    seleccionP=IntVar()
    radD=Radiobutton(vConfigurar, text='Derecha', variable=seleccionP, value=1, command=lambda:cambioPanel(True))
    radD.grid(row=6, column=1, pady=(20,0), sticky=W)
    radI=Radiobutton(vConfigurar, text='Izquierda', variable=seleccionP, value=2, command=lambda:cambioPanel(False))
    radI.grid(row=7, column=1, sticky=W)
    radD.select()

    BotConfirmar = Button(vConfigurar, text='Listo', command=confirmar)
    BotConfirmar.grid(row=8, column=0, columnspan=3)

def ayuda():
    startfile('manual_de_usuario_futoshiki.pdf')
    return

def acerca():
    vAcerca = Tk()
    ventanas.append(vAcerca)
    vAcerca.title('Acerca de...')
    LabelA=Label(vAcerca, text='Futoshiki')
    LabelA.grid(row=0, column=0, columnspan=2)
    LabelA=Label(vAcerca, text='Versión: ')
    LabelA.grid(row=1, column=0)
    LabelA=Label(vAcerca, text='1.0')
    LabelA.grid(row=1, column=1)
    LabelA=Label(vAcerca, text='Fecha:')
    LabelA.grid(row=2, column=0)
    LabelA=Label(vAcerca, text='6/11/21')
    LabelA.grid(row=2, column=1)
    LabelA=Label(vAcerca, text='Autor:')
    LabelA.grid(row=3, column=0)
    LabelA=Label(vAcerca, text='Axel Alexander Chaves Reyes')
    LabelA.grid(row=3, column=1)
    vAcerca.mainloop()

def salir():
    for i in ventanas:
        try:
            i.destroy()
        except:
            pass

def cargarPartida():
    global nombre
    global nivel
    global pila
    global transcurrido
    global dificultad
    global tiempo
    global limite
    global numero
    global juego
    if ganaste:
        save=open('futoshiki2021juegoactual.dat', 'r', encoding='utf-8')
        lineas=save.readlines()
        save.seek(0)
        nombre=lineas[0].replace('\n','')
        nivel=eval(lineas[1].replace('\n',''))
        dificultad=nivel[2]
        tiempo=nivel[3]
        limite=nivel[4]
        juego=[]
        cargar(nivel[0])
        nivel=eval(lineas[1].replace('\n',''))
        pilita=eval(lineas[2].replace('\n',''))
        transcurrido=eval(lineas[3].replace('\n',''))
        for i in pilita:
            numero=i[0]
            apuntar(casillas[i[1]], i[1])
        numero=1
        switch(1)

def guardar():
    if ganaste:
        return
    else:
        save=open('futoshiki2021juegoactual.dat', 'w', encoding='utf-8')
        save.write(str(nombre))
        save.write('\n')
        save.write(str(nivel))
        save.write('\n')
        save.write(str(pila))
        save.write('\n')
        save.write(str(transcurrido))
        save.close()
        messagebox.showinfo('Archivo guardado', 'Tu partida ha sido guardada.')
    return

def limitador(ent):
    if len(ent.get()) > 0:
        #donde esta el :5 limitas la cantidad d caracteres
        ent.set(ent.get()[:20])
#                                                           Objetos de ventana
ventana = Tk()
ventanas.append(ventana)
pantalla_largo=ventana.winfo_screenwidth()//2
pantalla_alto=ventana.winfo_screenheight()//2
ventana.geometry( f'{900}x{900}+{(pantalla_largo)-450}+{(pantalla_alto)-440}')

frameNombre     = Frame(ventana, bg='brown')
frame           = Frame(ventana, bg='#f0f0f0')
frameTop        = Frame(ventana, bg='yellow')
frameVictoria   = Frame(ventana, bg='orange')
frameOpciones   = Frame(frame)
frameNums       = Frame(frame)
frameJuego      = Frame(frame, bg='#b97a57')
frameReloj      = Frame(frameOpciones, bg='light yellow')

ventana.title('Futoshiki')

#                                                           Imágenes
imgTitulo    = ImageTk.PhotoImage(Image.open('images/title.png').resize((448, 152), Image.NONE))

imgListo     = ImageTk.PhotoImage(Image.open('images/listo.png').resize((147, 57), Image.NONE))
imgJugar     = ImageTk.PhotoImage(Image.open('images/jugar.png').resize((147, 57), Image.NONE))
imgDeshacer  = ImageTk.PhotoImage(Image.open('images/volver.png').resize((147, 57), Image.NONE))
imgTerminar  = ImageTk.PhotoImage(Image.open('images/otro.png').resize((147, 57), Image.NONE))
imgReiniciar = ImageTk.PhotoImage(Image.open('images/borrar.png').resize((147, 57), Image.NONE))
imgTop       = ImageTk.PhotoImage(Image.open('images/top.png').resize((147, 57), Image.NONE))
imgGuardar   = ImageTk.PhotoImage(Image.open('images/guardar.png').resize((147, 57), Image.NONE))   
imgCargar    = ImageTk.PhotoImage(Image.open('images/cargar.png').resize((147, 57), Image.NONE))

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

imgB1D        = ImageTk.PhotoImage(Image.open('images/Bloques/1$.png').resize((50, 50), Image.NONE))
imgB2D        = ImageTk.PhotoImage(Image.open('images/Bloques/2$.png').resize((50, 50), Image.NONE))
imgB3D        = ImageTk.PhotoImage(Image.open('images/Bloques/3$.png').resize((50, 50), Image.NONE))
imgB4D        = ImageTk.PhotoImage(Image.open('images/Bloques/4$.png').resize((50, 50), Image.NONE))
imgB5D        = ImageTk.PhotoImage(Image.open('images/Bloques/5$.png').resize((50, 50), Image.NONE))

imgN        = ImageTk.PhotoImage(Image.open('images/Bloques/..png'))
imgA        = ImageTk.PhotoImage(Image.open('images/Bloques/A.png'))
imgB        = ImageTk.PhotoImage(Image.open('images/Bloques/B.png'))
imgC        = ImageTk.PhotoImage(Image.open('images/Bloques/C.png'))
imgD        = ImageTk.PhotoImage(Image.open('images/Bloques/D.png'))

#                                                           Barra
menus=Menu(ventana)
ventana.config(menu=menus)

mnuArchivo=Menu(menus, tearoff=0)
mnuArchivo.add_command(label="Configurar", command=configurar)
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Salir", command=salir)

mnuAyuda=Menu(menus, tearoff=0)
mnuAyuda.add_command(label="Ayuda", command=ayuda)
mnuAyuda.add_command(label="Acerca de...", command=acerca)

menus.add_cascade(label="Archivo", menu=mnuArchivo)
menus.add_cascade(label="Ayuda", menu=mnuAyuda)
#                                                           Otros frames
nombrecillo = StringVar()
EntryNombre=Entry(frameNombre, width=30, font=('Segoe UI', 20), textvariable = nombrecillo)
nombrecillo.trace("w", lambda *args: limitador(nombrecillo))
BotNombre=Button(frameNombre, image=imgListo, activebackground='brown',  highlightthickness = 0, bd = 0, command=lambda:iniciar())
LabelNombre= Label(frameNombre, text='Nombre:',font=('Segoe UI', 20), fg='white', bg='brown', highlightthickness = 0)
LabelNombre.pack(pady=100)
EntryNombre.pack()
BotNombre.pack(pady=100)

LabelTopD= Label(frameTop, text='Fácil:',font=('Segoe UI', 12), bg='yellow', highlightthickness = 0)
LabelTopN= Label(frameTop, text='Normal:',font=('Segoe UI', 12), bg='yellow', highlightthickness = 0)
LabelTopF= Label(frameTop, text='Difícil:',font=('Segoe UI', 12), bg='yellow', highlightthickness = 0)
LabelTopD.grid(row=0, column=0, sticky=W)
LabelTopN.grid(row=11, column=0, sticky=W)
LabelTopF.grid(row=22, column=0, sticky=W)
for fila in [0, 11, 22]:
    LabelTopJ= Label(frameTop, text='Jugador',font=('Segoe UI', 12), bg='yellow', highlightthickness = 0)
    LabelTopT= Label(frameTop, text='Tiempo',font=('Segoe UI', 12), bg='yellow', highlightthickness = 0)
    LabelTopJ.grid(row=fila, column=1)
    LabelTopT.grid(row=fila, column=2)

#                                                           Objetos de la ventana
LblTitulo =  Label(frame, image=imgTitulo, background='#f0f0f0')

BotJugar    = Button(frameOpciones, image=imgJugar,     highlightthickness = 0, bd = 0, command=jugar)
BotDeshacer = Button(frameOpciones, image=imgDeshacer,  highlightthickness = 0, bd = 0, command=volver)
BotTerminar = Button(frameOpciones, image=imgTerminar,  highlightthickness = 0, bd = 0, command=otro)
BotReiniciar= Button(frameOpciones, image=imgReiniciar, highlightthickness = 0, bd = 0, command=reiniciar)
BotTop      = Button(frameOpciones, image=imgTop,       highlightthickness = 0, bd = 0, command=top10)
BotGuardar  = Button(frameOpciones, image=imgGuardar,   highlightthickness = 0, bd = 0, command=guardar)
BotCargar   = Button(frameOpciones, image=imgCargar,    highlightthickness = 0, bd = 0, command=cargarPartida)

Bot1 = Button(frameNums, image=img1_,  highlightthickness = 0, bd = 0, command=lambda:switch(1))
Bot2 = Button(frameNums,  image=img2,  highlightthickness = 0, bd = 0, command=lambda:switch(2))
Bot3 = Button(frameNums,  image=img3,  highlightthickness = 0, bd = 0, command=lambda:switch(3))
Bot4 = Button(frameNums,  image=img4,  highlightthickness = 0, bd = 0, command=lambda:switch(4))
Bot5 = Button(frameNums,  image=img5,  highlightthickness = 0, bd = 0, command=lambda:switch(5))

Bot00 = Button(frameJuego, command=lambda:apuntar(Bot00, 0))
Bot01 = Button(frameJuego, command=lambda:apuntar(Bot01, 1))
Bot02 = Button(frameJuego, command=lambda:apuntar(Bot02, 2))
Bot03 = Button(frameJuego, command=lambda:apuntar(Bot03, 3))
Bot04 = Button(frameJuego, command=lambda:apuntar(Bot04, 4))
Bot10 = Button(frameJuego, command=lambda:apuntar(Bot10, 5))
Bot11 = Button(frameJuego, command=lambda:apuntar(Bot11, 6))
Bot12 = Button(frameJuego, command=lambda:apuntar(Bot12, 7))
Bot13 = Button(frameJuego, command=lambda:apuntar(Bot13, 8))
Bot14 = Button(frameJuego, command=lambda:apuntar(Bot14, 9))
Bot20 = Button(frameJuego, command=lambda:apuntar(Bot20, 10))
Bot21 = Button(frameJuego, command=lambda:apuntar(Bot21, 11))
Bot22 = Button(frameJuego, command=lambda:apuntar(Bot22, 12))
Bot23 = Button(frameJuego, command=lambda:apuntar(Bot23, 13))
Bot24 = Button(frameJuego, command=lambda:apuntar(Bot24, 14))
Bot30 = Button(frameJuego, command=lambda:apuntar(Bot30, 15))
Bot31 = Button(frameJuego, command=lambda:apuntar(Bot31, 16))
Bot32 = Button(frameJuego, command=lambda:apuntar(Bot32, 17))
Bot33 = Button(frameJuego, command=lambda:apuntar(Bot33, 18))
Bot34 = Button(frameJuego, command=lambda:apuntar(Bot34, 19))
Bot40 = Button(frameJuego, command=lambda:apuntar(Bot40, 20))
Bot41 = Button(frameJuego, command=lambda:apuntar(Bot41, 21))
Bot42 = Button(frameJuego, command=lambda:apuntar(Bot42, 22))
Bot43 = Button(frameJuego, command=lambda:apuntar(Bot43, 23))
Bot44 = Button(frameJuego, command=lambda:apuntar(Bot44, 24))

casillas=(
Bot00,Bot01,Bot02,Bot03,Bot04,
Bot10,Bot11,Bot12,Bot13,Bot14,
Bot20,Bot21,Bot22,Bot23,Bot24,
Bot30,Bot31,Bot32,Bot33,Bot34,
Bot40,Bot41,Bot42,Bot43,Bot44)

for i in casillas:
    i.config(image=imgB0, activebackground='#b97a57',  highlightthickness = 0, bd = 0)

#                                                           Posiciones de las cosas
LblTitulo.grid(row=0, column=1, columnspan=4, pady=30)

frameJuego.grid(row=1, column=1, columnspan=4)
frameNums.grid(row=1, column=5)
frameOpciones.grid(row=2, column=0, columnspan=6, pady=20)
frameReloj.grid(row=3, column=0, columnspan=2, padx=20, pady=30)
BotGuardar.grid(row=3, column=2, pady=30)
BotCargar.grid(row=3, column=3, columnspan=2, padx=10, pady=30)

LabelWin= Label(frameVictoria, text='¡EXCELENTE!', font=('Segoe UI', 80), fg='yellow', bg='orange',  highlightthickness = 0)
LabelWin.pack(pady=200)
LabelTiempo= Label(frameVictoria,font=('Segoe UI', 40), fg='yellow', bg='orange',  highlightthickness = 0)

horas = Label(frameReloj,   text='0',       font=('Segoe UI', 12), bg='light yellow',  highlightthickness = 0)
minutos = Label(frameReloj, text='0',       font=('Segoe UI', 12), bg='light yellow',  highlightthickness = 0)
segundos = Label(frameReloj,text='0',       font=('Segoe UI', 12), bg='light yellow',  highlightthickness = 0)

Label(frameReloj,           text='Horas',   font=('Segoe UI', 12), bg='light yellow',  highlightthickness = 0).grid(row=0, column=0)
Label(frameReloj,           text='Minutos', font=('Segoe UI', 12), bg='light yellow',  highlightthickness = 0).grid(row=0, column=1, padx=20, pady=10)
Label(frameReloj,           text='Segundos',font=('Segoe UI', 12), bg='light yellow',  highlightthickness = 0).grid(row=0, column=2)

horas.grid(row=1, column=0)
minutos.grid(row=1, column=1)
segundos.grid(row=1, column=2)

#Bloques
for i in range(9):
    for j in range(9):
        if i%2==1 or j%2==1:
            comparaciones.append(Label(frameJuego, image=imgN, bg='#b97a57',  highlightthickness = 0))
            comparaciones[-1].grid(row=i, column=j)

#Casillas
i=0
for fila in range(5):
    for columna in range(5):
        casillas[i].grid(row=fila*2, column=columna*2)
        i+=1

#Numeros
Bot1.grid(row=0, column=0)
Bot2.grid(row=1, column=0)
Bot3.grid(row=2, column=0)
Bot4.grid(row=3, column=0)
Bot5.grid(row=4, column=0)

#Posición de botones
BotJugar.grid(row=0, column=0)
BotDeshacer.grid(row=0, column=1, padx=30)
BotTerminar.grid(row=0, column=2)
BotReiniciar.grid(row=0, column=3, padx=30)
BotTop.grid(row=0, column=4)

frame.pack()
cronometro()
#                                                           Loop
ventana.mainloop()