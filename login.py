import tkinter as tk

ventana = tk.Tk()

def pantalla():
    ventana.geometry("800x600") #Ancho x Alto
    ventana.title("Proyecto")#Titulo
    ventana.resizable(False,False)#Para no Poder estirar la pantalla
pantalla()

ventana.mainloop() #Este llama a la ventana para poder verla
#Geometry para darle el tamaño a la pantalla



#Grupo: Juan Fontalvo Rojas, Angel Gonzalez y  Luis Moso