from tkinter import *
from  pyttsx3 import *
from threading import *
from time import *
import random
from multiprocessing import *
from threading import *

def archivo1():
	valor=0
	with open("archivo1","w") as archivo:
		for i in range(100000):
			valor=random.randrange(100,200)
			archivo.write(str(valor)+"\n")
	archivo.close()

def archivo2():
	valor=0
	with open("archivo2","w") as archivo:
		for i in range(100000):
			valor=random.randrange(100,200)
			archivo.write(str(valor)+"\n")
	archivo.close()

def secuencial():
	decir=init()
	decir.say("ejecucion secuencial")
	decir.runAndWait()

	inicio=time()
	salida.config(text="")
	
	archivo1()
	archivo2()
	fin=time()
	
	salida.config(text="Tiempo: " +str(fin-inicio))


def por_procesos():
	decir=init()
	decir.say("ejecucion por procesos")
	decir.runAndWait()

	inicio=time()
	salida.config(text="")
	p1=Process(target=archivo1)
	p2=Process(target=archivo2)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	fin=time()
	
	salida.config(text="Tiempo: " +str(fin-inicio))
def por_hilos():
	decir=init()
	decir.say(" ejecucion por hilos")
	decir.runAndWait()
	inicio=time()
	salida.config(text="")
	hilo1=Thread(target=archivo1)
	hilo2=Thread(target=archivo2)
	hilo1.start()
	hilo2.start()		
	hilo1.join()
	hilo2.join()	
	fin=time()
	
	salida.config(text="Tiempo: " +str(fin-inicio))

if __name__=="__main__":

	
	"""
	
	print("sali")"""

	ventana=Tk()
	ventana.geometry("180x400")
	boton_procesos=Button(ventana,text="   Procesos  ",command=por_procesos)
	boton_hilos=Button(ventana,text="   Hilo   ",command=por_hilos)
	boton_secuencial=Button(ventana,text=" Secuencial ",command=secuencial)

	boton_procesos.place(x=60,y=20)
	boton_hilos.place(x=60,y=60)
	boton_secuencial.place(x=60,y=100)

	salida=Label(ventana,text="")
	
	salida.place(x=18,y=160)
	

	ventana.mainloop()




	
	