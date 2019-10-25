

from tkinter import *
import ctypes
import os
from time import *
from pyttsx3 import *

class Grafo:
	def estado_p(self):
		if velocidad_de_ejecucion.get()>0:
			voz.say("estado p")
			voz.runAndWait()

	def estado_q(self):
		if velocidad_de_ejecucion.get()>0:
			voz.say("estado q")
			voz.runAndWait()

	def estado_r(self):
		if velocidad_de_ejecucion.get()>0:
			voz.say("estado r")
			voz.runAndWait()		
	def palindrome(self):
		
		voz.say("la palabra es palindrome")
		voz.runAndWait()

	def cargar_grafo_1(self):
		Label(ventana,image=cargar_imagen_grafo_1).place(x=100,y=250)
		if velocidad_de_ejecucion.get()>0:
			ventana.after(velocidad_de_ejecucion.get()*200,self.estado_p)
		ventana.after(velocidad_de_ejecucion.get()*400,self.cargar_grafo_2)
		
		#voz.say("estado p")
		#voz.runAndWait()

	def cargar_grafo_2(self):
		Label(ventana,image=cargar_imagen_grafo_2).place(x=100,y=250)
		

	def cargar_grafo_3(self):
		Label(ventana,image=cargar_imagen_grafo_3).place(x=100,y=250)
		ventana.after(velocidad_de_ejecucion.get()*200,self.estado_p)
		if velocidad_de_ejecucion.get()>0:
			ventana.after(velocidad_de_ejecucion.get()*400,self.cargar_grafo_2)
		#voz.say("estado p")
		#voz.runAndWait()

	def cargar_grafo_4(self):
		Label(ventana,image=cargar_imagen_grafo_4).place(x=100,y=250)
		ventana.after(velocidad_de_ejecucion.get()*400,self.cargar_grafo_5)
		if velocidad_de_ejecucion.get()>0:
			ventana.after(velocidad_de_ejecucion.get()*200,self.estado_q)
		#voz.say("estado q")
		#voz.runAndWait()
		
	def cargar_grafo_5(self):
		Label(ventana,image=cargar_imagen_grafo_5).place(x=100,y=250)
		
	def cargar_grafo_6(self):
		Label(ventana,image=cargar_imagen_grafo_6).place(x=100,y=250)
		ventana.after(velocidad_de_ejecucion.get()*400,self.cargar_grafo_5)
		if velocidad_de_ejecucion.get():
			ventana.after(velocidad_de_ejecucion.get()*200,self.estado_q)

	def cargar_grafo_7(self):
		Label(ventana,image=cargar_imagen_grafo_7).place(x=100,y=250)
		if velocidad_de_ejecucion.get()>0:
			ventana.after(velocidad_de_ejecucion.get()*400,self.cargar_grafo_8)
		ventana.after(velocidad_de_ejecucion.get()*200,self.estado_r)
		#voz.say("estado r")
		#voz.runAndWait()

	def cargar_grafo_8(self):
		Label(ventana,image=cargar_imagen_grafo_8).place(x=100,y=250)
		
		ventana.after(velocidad_de_ejecucion.get()*100,self.palindrome)
		
		
class Validar:
	def __init__(self,palabra_a_validar):
		self.estado="P"
		self.estado_anterior="P"
		self.desplazamiento_puntero=27
		self.cadena=Cadena()
		self.cadena.cargar_cadena_en_lista(palabra_a_validar)
		self.cinta=Cinta(self.cadena.lista_de_la_cadena)
		self.cinta.dibujar_cinta()
		self.pila=Pila()
		self.grafo=Grafo()
		self.primera_vez=True
		self.f1()




	def cargar_palindrome(self):

		Label(ventana,image=cargar_imagen_palindrome).place(x=0,y=100)

	def cargar_no_palindrome(self):
		Label(ventana,image=cargar_imagen_no_palindrome).place(x=0,y=90)
	
			

	def f1(self,caracter_numero_=0):

		if caracter_numero_<len(self.cadena.lista_de_la_cadena):
			self.cinta.recorrer_cinta(self.desplazamiento_puntero)#va la funcion recorrer cinta de la clase Cinta para mover la flecha lectora
			self.desplazamiento_puntero+=50#se usa para incremenar la coordenada, y de esta manera dar el efecto de mover la flecha
			self.pila.dibujar_pila()
			ventana.after(velocidad_de_ejecucion.get()*500,lambda:self.f2(caracter_numero_))			

		if caracter_numero_==len(self.cadena.lista_de_la_cadena):
			#valindando fin de la cadena
			#ejevcutara la transicion de q a r
			#self.estado=self.cadena.valida_y_elimina_el_primer_elemento_de_pila(self.pila,self.estado,caracter_numero_)
			ventana.after(velocidad_de_ejecucion.get()*500,lambda:self.f2(caracter_numero_))
	

	def f2(self,caracter_numero_):
		#validando caracter de cadena
			#va a la funcio "valida_y_elimina_el_primer_elemento_de_pila" validando el caracter de la cadena
				#validando el 1 elemento de la pila, retornando el estado en el que se encuentra,
				#si la validacion no es correcta retorna error ya que no cumple con el automata
		self.estado_anterior=self.estado
		self.estado=self.cadena.valida_y_elimina_el_primer_elemento_de_pila(self.pila,self.estado,caracter_numero_)#
		
		try:
			if self.primera_vez:
				#Label(ventana,image=cargar_imagen_grafo_1).place(x=100,y=250)
				ventana.after(velocidad_de_ejecucion.get()*400,self.grafo.cargar_grafo_1)
				self.primera_vez=False
			elif self.estado!="ERROR" and self.estado_anterior=="Q" and (len(self.cadena.lista_de_la_cadena)==(caracter_numero_) ):
				
				ventana.after(velocidad_de_ejecucion.get()*400,self.grafo.cargar_grafo_7)

			elif self.estado!="ERROR" and self.estado_anterior=="P" and (self.cadena.lista_de_la_cadena[caracter_numero_]=="a" or self.cadena.lista_de_la_cadena[caracter_numero_]=="b"):
				ventana.after(velocidad_de_ejecucion.get()*400,self.grafo.cargar_grafo_3)
				
			elif self.estado!="ERROR" and self.estado_anterior=="P" and self.cadena.lista_de_la_cadena[caracter_numero_]=="c":
				ventana.after(velocidad_de_ejecucion.get()*400,self.grafo.cargar_grafo_4)

			elif self.estado!="ERROR" and self.estado_anterior=="Q" and (self.cadena.lista_de_la_cadena[caracter_numero_]=="a" or self.cadena.lista_de_la_cadena[caracter_numero_]=="b"):
				ventana.after(velocidad_de_ejecucion.get()*400,self.grafo.cargar_grafo_6)

			
		except:
			pass
		
		if self.estado=="ERROR":#
			caracter_numero_=len(self.cadena.lista_de_la_cadena)
			ventana.after(velocidad_de_ejecucion.get()*400,lambda:self.f3(caracter_numero_))
			
		else:
			self.pila.dibujar_pila()	
			
			ventana.after(velocidad_de_ejecucion.get()*800,lambda:self.f3(caracter_numero_))

	def f3(self,caracter_numero_):
			if caracter_numero_==len(self.cadena.lista_de_la_cadena):	
				
				if self.estado=="R":
					
					#ventana.after(velocidad_de_ejecucion.get()*200,self.cargar_grafo_8)
					ventana.after(velocidad_de_ejecucion.get()*800,self.cargar_palindrome)
					
					
					boton_ejecutar.config(state="normal")
				else:
					ventana.after(velocidad_de_ejecucion.get()*200,self.cargar_no_palindrome)
					voz.say("la palabra no es palindrome")
					voz.runAndWait()	
					
					boton_ejecutar.config(state="normal")
					
			
			elif caracter_numero_<len(self.cadena.lista_de_la_cadena):
				self.cadena.agrega_el_nuevo_elemento_a_la_pila(self.pila)
				
				self.pila.dibujar_pila()
		
				caracter_numero_+=1
				

				ventana.after(velocidad_de_ejecucion.get()*800,lambda:self.f1(caracter_numero_))
		
class Cadena:
	def __init__(self):
		self.lista_de_la_cadena=[]
		self.p_a_numeral=False
		self.p_a_a=False
		self.p_a_b=False

		self.p_b_numeral=False
		self.p_b_a=False
		self.p_b_b=False

		self.p_c_numeral=False
		self.p_c_a=False
		self.p_c_b=False

		self.q_a_a=False
		self.q_b_b=False

		self.r_vacio_numeral=False
		

	def cargar_cadena_en_lista(self,palabra_a_validar):
		for i in range(len(palabra_a_validar)):
			self.lista_de_la_cadena.append(palabra_a_validar[i])
				
	def valida_y_elimina_el_primer_elemento_de_pila(self,pila,estado,tope):
		try:
			#validanodo fin de cadena
			if estado=="Q" and len(pila.pila)==1 and pila.pila[len(pila.pila)-1]=="#" and tope==len(self.lista_de_la_cadena):
				
				pila.pila.pop()
				self.r_vacio_numeral=True
				return "R"
			#leyendo a estado a estando en p
			elif self.lista_de_la_cadena[tope]=="a" and estado=="P":
				if pila.pila[len(pila.pila)-1]=="#":
					pila.pila.pop()
					self.p_a_numeral=True

				elif pila.pila[len(pila.pila)-1]=="a":
						pila.pila.pop()
						self.p_a_a=True
					
				elif pila.pila[len(pila.pila)-1]=="b":	
						pila.pila.pop()
						self.p_a_b=True
						
				return estado

			#leyendo b en estado p
			elif self.lista_de_la_cadena[tope]=="b" and estado=="P":
				if pila.pila[len(pila.pila)-1]=="#":
					pila.pila.pop()
					self.p_b_numeral=True
					
				elif pila.pila[len(pila.pila)-1]=="a":
						pila.pila.pop()
						self.p_b_a=True
				
				elif pila.pila[len(pila.pila)-1]=="b":	
						pila.pila.pop()
						self.p_b_b=True
				return estado

			#leyendo c en estando en p
			elif self.lista_de_la_cadena[tope]=="c" and estado=="P":
				if pila.pila[len(pila.pila)-1]=="#":
					pila.pila.pop()
					self.p_c_numeral=True

				elif pila.pila[len(pila.pila)-1]=="a":
						pila.pila.pop()
						self.p_c_a=True
						
				
				elif pila.pila[len(pila.pila)-1]=="b":	
						pila.pila.pop()
						self.p_c_b=True
						
						
						
				estado="Q"
				return estado

			#leyendo a estando q
			elif self.lista_de_la_cadena[tope]=="a" and estado=="Q":
				if pila.pila[len(pila.pila)-1]=="a":
					pila.pila.pop()
					
					return estado
				else:
				
					return "ERROR"

			#leyendo b estando en q
			elif self.lista_de_la_cadena[tope]=="b" and estado=="Q":
				if pila.pila[len(pila.pila)-1]=="b":
					
					pila.pila.pop()
					return estado
				else:
					return "ERROR"		
			else:
				
				return "ERROR"
		except:
			self.estado="ERROR"
			return self.estado		
		



	def agrega_el_nuevo_elemento_a_la_pila(self,pila):
		if self.p_a_numeral:
			pila.pila.append("#")
			pila.pila.append("a")
			self.p_a_numeral=False

		if self.p_a_a:
			pila.pila.append("a")
			pila.pila.append("a")
			self.p_a_a=False

		if self.p_a_b:
			pila.pila.append("b")
			pila.pila.append("a")
			self.p_a_b=False

		#cuando leo b en p
		if self.p_b_numeral:
			pila.pila.append("#")
			pila.pila.append("b")
			self.p_b_numeral=False

		if self.p_b_a:
			pila.pila.append("a")
			pila.pila.append("b")
			self.p_b_a=False
		
		if self.p_b_b:
			pila.pila.append("b")
			pila.pila.append("b")
			self.p_b_b=False

		#cuando leo c en p
		if self.p_c_numeral:
			pila.pila.append("#")
			self.p_c_numeral=False

		if self.p_c_a:
			pila.pila.append("a")
			self.p_c_a=False

		if self.p_c_b:
			pila.pila.append("b")
			self.p_c_b=False

		#cuando estoy en q y leo cualquier caracter agrego vacio por eso 
		#no hago los metodos de agregar en la pila

		#cuando leo vacio en R, es decir estoy en el fin de la cadena
		if self.r_vacio_numeral:
			pila.pila.append("#")
			self.r_vacio_numeral=False

class Cinta:
	def __init__(self,lista_de_la_cadena):
		self.lista_de_la_cadena=lista_de_la_cadena
		self.primera_vez=True
		self.puntero=0

	def dibujar_cinta(self):
		desplazamiento_horizontal=10
		#print(self.lista_de_la_cadena)
		for i in range(len(self.lista_de_la_cadena)):
			Label(ventana,image=cargar_imagen_cinta).place(x=desplazamiento_horizontal,y=100)
			#cargando los caracteres en la cinta
			
			Label(ventana,text=self.lista_de_la_cadena[i],font=("Verdana",14),bg="white",pady=0).place(x=desplazamiento_horizontal+18,y=109)
			desplazamiento_horizontal+=50

	def recorrer_cinta(self,desplazamiento_horizontal=27):
		if self.primera_vez:
			
			self.primera_vez=False
			self.puntero=Label(ventana,image=cargar_imagen_puntero)
			self.puntero.place(x=desplazamiento_horizontal,y=150)
		else:
			self.puntero.place(x=desplazamiento_horizontal,y=150)	

class Pila:
	def __init__(self):
		self.pila=[]
		self.pila.append("#");
		
	def dibujar_pila(self):
		pila=Label(ventana,image=cargar_imagen_pila)
		pila.place(x=40,y=480)
		coordenada_horizontal=54
		for i in range(len(self.pila)):
			pilaa=(Label(ventana,text=self.pila[i],font=("Verdana",12)))
			pilaa.place(x=coordenada_horizontal,y=500)
			coordenada_horizontal+=40
			
def funcion_boton():
	Label(ventana,image=cargar_imagen_limpiar).place(x=0,y=100)
	Label(ventana,image=cargar_imagen_grafo_0).place(x=100,y=250)
	boton_ejecutar.config(state="disabled")
	objeto_validar=Validar(entry_ingresar_cadena.get())

voz=init()
#detecta la resolucion de la pantalla
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho_de_la_pantalla = user32.GetSystemMetrics(0)
alto_de_la_pantalla = user32.GetSystemMetrics(1)
#establesco el ancho y el alto de la ventana 
ancho_de_la_ventana=str(int(ancho_de_la_pantalla/2))
alto_de_la_ventana=str(int(alto_de_la_pantalla/2))
#creo la ventana con su respectivo tamaño
ventana = Tk()
ventana.geometry(ancho_de_la_ventana+"x"+alto_de_la_ventana+"+800+30")  #opcional, la uso para que veas mejor
#deslizador de velocidad
velocidad_de_ejecucion=Scale(ventana,width=20,troughcolor="#F0F0F0",activebackground="#F0F0F0",orient="horizontal",length=200,takefocus=10,from_=0.0,to=3.0,tickinterval=0.25)
velocidad_de_ejecucion.place(x=10,y=20)
#label insertar cadena
label_insertar_cadena=Label(ventana,text=" Insertar Cadena ",font=("Chiller",24),width=0,height=0,pady=0,bg="#F0F0F0")
label_insertar_cadena.place(x=250,y=20)
#entry validar cadena
entry_ingresar_cadena=Entry(ventana,width=17,justify=CENTER,font=("Chiller",24),bg="#FFFFCC") 
entry_ingresar_cadena.place(x=500,y=20)
entry_ingresar_cadena.focus()
#boton ejecutar
icono_ejecutar=PhotoImage(file="ejecutar.png")
boton_ejecutar=Button(ventana,text="correr",image=icono_ejecutar,command=funcion_boton)
boton_ejecutar.place(x=833,y=6)
#cargar imagenes a utilizar
cargar_imagen_cinta=PhotoImage(file="cinta.png")
cargar_imagen_puntero=PhotoImage(file="puntero.png")
cargar_imagen_pila=PhotoImage(file="pila.png")
cargar_imagen_grafo_0=PhotoImage(file="grafo0.png")
cargar_imagen_grafo_1=PhotoImage(file="grafo1.png")
cargar_imagen_grafo_2=PhotoImage(file="grafo2.png")
cargar_imagen_grafo_3=PhotoImage(file="grafo3.png")
cargar_imagen_grafo_4=PhotoImage(file="grafo4.png")
cargar_imagen_grafo_5=PhotoImage(file="grafo5.png")
cargar_imagen_grafo_6=PhotoImage(file="grafo6.png")
cargar_imagen_grafo_7=PhotoImage(file="grafo7.png")
cargar_imagen_grafo_8=PhotoImage(file="grafo8.png")
cargar_imagen_palindrome=PhotoImage(file="palindrome.png")
cargar_imagen_no_palindrome=PhotoImage(file="no_palindrome.png")
cargar_imagen_limpiar=PhotoImage(file="limpiar.png")
#cargado grafo por defecto
#Label(ventana,image=cargar_imagen_grafo_0).place(x=100,y=230)
Label(ventana,image=cargar_imagen_grafo_0).place(x=100,y=250)
Label(ventana,image=cargar_imagen_pila).place(x=40,y=480)
Label(ventana,text="#",font=("Verdana",12)).place(x=54,y=500)
##runAndWait()

ventana.resizable(False,False)
ventana.title("Automata de Pila")

ventana.mainloop()
