#	variables
		#numeros(int,float,complex) (se pueden realizar operaciones entre todos los tipos de numeros)

numero_entero = 3		#puede ser decimal(poner numero), octal(anteponer 0o), hexadecimal(anteponer 0x) o binario(anteponer 0b)

numero_flotante = 2.99		#son cosa medio rara(probar print(1.1 + 2.2)) se representan como fracciones de base 2(binario), asi que son una estimacion de un flotante real

numero_complejo = 1 + 2j		#para acceder a la parte real "numero_complejo.real" para acceder a la parte imaginaria "numero_complejo.img"

		#texto(str) (secuencia inmutable de caracteres Unicode)

cadena_de_texto = 'Hola Mundo'		#se pueden multiplicar(str*numero) y sumar(concatenar)(str1 + str2)

		#booleano(bool) (cualquier objeto puede ser usado como un booleano)
				  #(por defecto, cualquier objeto es considerado como verdadero, a excepcion de (None,False, 0, 0.0, '', [], (), {}, set(), range(0), etc...))

valor_booleano = True

# fstrings(esta desde la version 3.6, se usa para evitar concatenar)
	nombre  = 'Gonzalo'
	fstring  = f'hola {nombre}, tenes {100} pesos?'

#	metodos de strings

		len(cadena_de_texto)	#regresa la longitud de la cadena o lista

		#metodos de formato
			cadena_de_texto.capitalize()		#convierte la primer letra en mayuscula
			cadena_de_texto.lower()			#convierte todo el texto a minuscula
			cadena_de_texto.upper()			#convierte todo el texto en mayuscula
			cadena_de_texto.swapcase()		#invierte minusculas y mayusculas
			cadena_de_texto.center(longitud, "caracter de relleno") #centra el texto Ej: cadena_de_texto.center(50, "=")

		#metodos de busqueda
			cadena_de_texto.count('a')		#cuenta la cantidad de apariciones de la subcadena 'a'. count("subcadena", posicion_inicio, posicion_fin)
			cadena_de_texto.find("Hola")		#encuentra la posicion de la subcadena "Hola". find("subcadena", posicion_inicio, posicion_fin)

		#metodos de validacion
			cadena_de_texto.startswith("Hola")		# retorna true si la cadena empieza con la subcadena "Hola"
			cadena_de_texto.endswith("Mundo")		# retorna true si la cadena termina con la subcadena "Mundo"
			cadena_de_texto.isalnum()		# retorna true si la cadena es alfanumerica
			cadena_de_texto.isalpha()		# retorna true si es alfabetica
			cadena_de_texto.isdigit()		# retorna true si es numerica
			cadena_de_texto.islower()		# retorna true si es todo minusculas
			cadena_de_texto.isupper()		# retorna true si es todo mayusculas

		#metodos de sustitucion
			cadena_de_texto.replace("Hola", "Adios")		# sustituye Hola por Adios
			#cadena_de_texto.format(*args, **kwargs)		#remplaza el format "texto {0}"
		
		#metodos de union y division
			cadena_de_texto.join()		#agrega el parametro en cada iteracion de la cadena
			cadena_de_texto.split(" ")		#divide la cadena por los espacios. Salida: ["hola", "mundo"]



#	if/else/else if
	
	#está la version estandar
	
		if ():	#condicion 1
			#
		elif():	#condicion 2
			#
		else:	#todos los demas casos
			#
	#y la version compacta(no se puede usar el elif en esta versión)
	
		b = 5
		a = 1 if b > 5 else 2		#se puede usar para asignar valores
		print(a if a != 3 else b)		#o para imprimirlos

#	while
	i = 0
	while (i <= 10):		# su suele usar un contador "i" para limitar el bucle, tambien se suele usar un True, pero debe incluir un break
		print(i)
		if (i == 3):
			break			# "break" detiene el bucle
		if(i == 10):
			continue		# "continue" salta a la siguiente iteracion(ignorando las siguientes instrucciones), como el i += 1 esta luego de esta linea, el 10 se imprimiria indefinidamente
		i += 1
		if(i==5):
			pass		#"pass" es decir basicamente none, que no haga nada
#	for
	for letra in cadena_de_texto:	#for valor in (lista,string,tupla,set)
		print(cadena_de_texto)
	

	for i in range(0,10,2):		# range(inicio,fin,salto) crea una lista numerica salida: [2,4,6,8]	si se dejan campos vacios seria como range(0,fin,1) el parametro "fin" es obligatorio
		print numero_entero



#	listas(clase <list>,son siempre listas dinamicas)

	lista = [1,'hola', 12.3, "mundo", True, [1,2,3,4,5], 23]
	lista2 = list('Hola Mundo')		# tambien se pueden crear con el constructor de la clase list('iterable') salida: ["H","o","l","a"," ","M","u","d","o"]
	[1,2,3,4]+[5,6,7,8]		#junta ambas listas
	print(lista[0])		#imprime primer elemento de la lista
	lista3 = lista[0:5:2]		# sirve para crear una sublista con los valores lista[inicio:fin:salto] salida: [0, 12.3, True]		valores por defecto: lista[0:-1:1]
	print(lista[5][2])		#imprime el objeto '3' de la sublista
	print(lista[-1])		#imprime el ultimo objeto('23') de la lista 

		#metodos

		lista.append('a')		#agrega el elemento 'a' al final de la lista
		lista.extend(lista2)	#agrega un iterable al final de la lista, puede ser cadena o otra lista
		lista.insert(2, 'alfajor')		#agrega el elemento 'alfajor' en el indice 2 de la lista
		lista.remove('a')		#elimina la primera aparacion del elemento 'a' en la lista
		lista.pop()			#elimina el ultimo elemento, si se le pone un numero elimina el elemento en ese indice, sino esta -1 por defecto
		lista.clear()		#borra todos los elementos
		del lista[2:6]		#elimina de la lista segun el indice
		lista.index('hola')		#regresa el indice de la primera aparicion del objeto 'hola'
		lista.count('a')		#cuenta y devuelve la cantidad de veces que se repite el objeto en la lista
		lista.sort()			#ordena la lista de menor a mayor
		lista.reverse()		#obtiene los objetos de la lista en orden inverso
		lista.copy()		#devuelve una copia poco profunda de la lista
		len(lista)		#devuelve la cantidad de elementos de la lista
		print('b' in lista)		# operador in comprueba si el elemento se encuentra en el iterable salida: False

#	tuplas(son como las listas, pero no estan son modificables sus elementos)

	tupla = h,o,l,a, ,m,u,n,d,o			# se puede declarar separando los elementos por comas, los parentesis no son necesarios
	tupla2 =(H,O,L,A, ,M,U,N,D,O)		#
	print(tupla[1])			#pueden verse los elementos, pero no modificarse


#	conjuntos(coleccion no ordenada sin objetos repetidos, mucho mas rapida en sus operaciones que la lista)
	conjunto = set()		#crea un conjunto vacio
	conjunto2 = {1,2,3,4,5,6,7,'a','b',True}
	conjunto3 = {1,2,3,4,5,6,7,8,8,8,9}		#eliminaria los objetos repetidos en este caso
	conjunto3.add(4)		#añade el elemento al set
	conjunto3.remove(4)		#quita el elemento del set
	conjunto2.union(conjunto3)		# junta ambos conjuntos

	print a 			# regresa los elementos en a

	print a - b 		# elementos en a pero no en b

	print a | b 		# elementos en a,b o ambos

	print a & b       	# elementos en ambos conjuntos

	print a ^ b      	# elementos en a o b pero no en ambos


#	diccionarios(como las listas, pero en vez de asociarlos con indices, se asocian con claves)

	diccionario = {'hola':'mundo','mundo':12, 'a': True}		#{clave:valor} 
	
	print(diccionario['hola'])		#regresa 'mundo'
	
	del diccionario['hola']			#borra el par clave valor del diccionario
	
	diccionario['adios'] = 'abcd'		#crea un nuevo par clave valor en el diccionario
	
	print(list(lista.keys()))				#regresa todas las claves del diccionario en una lista
	print(list(diccionario.values()))		#regresa todos los valores del diccionario en una lista
	
	dict(sape=4139, guido=4127, jack=4098) #otra forma de crear diccionarios
	
	#for key in diccionario:		#se puede iterar sobre un diccionario de esta forma
		#print(keys,diccionario[key])
	#for key,value in diccionario.items(): # o de esta forma
		#print(key,value)
	{x: x**2 for x in (2, 4, 6)}		#salida {2: 4, 4: 16, 6: 36}



#	comprension(es una forma de crear objetos iterables con una iteracion, solo se usa en python )

x = [x for w in range(5)]		# se compone de la siguiente manera [elemento a añadir, bucle]
y = [[0 for y in range(100)] for y in range(5)]		#produce 5 listas, cada una con 100 ceros
z = [z for z in range(100) if z % 5 == 0] #crea lista de los multiplos de 5 hasta el 100
i = {i:0 for i in range(200)} # crea un diccionario con clave del 1 al 200 y valores 0 en todas las claves
b = tuple(i for i in range(200)) #crea una tupla



#	funciones
	def funcion(a, b, c = None):		#se le pueden asignar valores por defecto a las variables, para no asignarles ninguno y que no de error al no llamarlas, asignales el None
		return a*b, a+b 	#al poner mas de una salida en el return, va a producir una tupla 
	print(function(2,4))			#salida: (8,6)

	salida1, salida2 = function(2,4)	#de esta forma al tener mas de una salida, se asigna un valor a cada variable y no sale en forma de tupla
	print(function(2,4)[2], function(2,4)[1]) #esta es otra forma, ya que es una tupla se puede acceder por el indice.	

	
	def func(x):

		def func2():
			print(x)
		return func2

	print(func(3))		#esto regresaria la funcion func2, la cual es manipulada dentro de func como un objeto
	func(3)()		#esto ejecutaria lo que esta dentro de func2
	x = func(2)
	x()		#esto es lo mismo de arriba, pero mucho mas claro



#	operador de desempaque(se suele usar para pasar listas,dicc o tuplas como argumentos a funciones)

	v = [1,23,5,454,6,765,767,7,334]
	print(*v)		#va a imprimir cada elemento de la lista como elementos individuales separados por coma salida: 1,23,5,etc...
	


	def funcion2(x,y):
   		print(x,y)
	
	z = {'x':'valor1','y':'valor2'}
	
	funcion(**z)	#va a pasar los valores con los mismos nombres como argumentos a la funcion


	def funcion3(x,y):

		print(x,y)


	g = [(1,2),(3,4),(78,54)]

	for pares in g:
		funcion3(*g)	#de esta forma se usa para pasar listas como argumentos a funciones, notese que son pares ordenados, si fuera una lista pura tendrian que ser tantos valores como variables 







#	*args & **kwargs(se suele usar cuando no sabes cuantas entradas tendra tu funcion)

	def funcion4(*args, **kwargs):
		print(args,kwargs)			#si quisiera desempaquetarlos para usarlos, habria que usar print(*args) y para los kwargs no funciona, no sé ni idea, fijate vos. 


	funcion4(1,2,3,4,5, uno = 23, dos = 13) #esto produce la siguiente salida (1,2,3,4,5) {'uno':23,'dos':13}

#	manejo de errores

	raise Exception('algo salio mal!') #esto mostraria un mensaje de excepcion diciendo el texto detallado, se puede usar cualquier tipo de error, no solo Exception

	try:
		x = 7 / 0
	except Exception as e:		#guarda la excepcion en la variable e, puede usarse el except solo, o poner excepciones en especifico
		print(e)
	finally:		#este bloque se ejecuta si o si, sin importar si ocurrio una excepcion, suele usarse para hacer guardados aunque hayan errores
		print('fin')


#	lambda(es una funcion anonima(ya que no requiere nombre) de una linea)
	x = lambda x: x+5 		#esta no es la forma correcta de usarla, pero es perfectamente posible
	y = lambda x,y: x+y 	#lambda variables: operaciones
	x(5)		#salida: 10
	y(3,8)		#salida: 11


#	map y filter(son funciones toman todos los valores de una lista y los modifican con una iteracion a traves de una funcion)

	lista_ejemplo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
	mp = map(lambda i: i*2, lista_ejemplo)		#la funcion map toma dos argumentos 1) la funcion que modifica 2) la lista base 
	print(list(mp))		#el list() es necesario ya que el map regresa un objeto map, y una lista es mas util

	ft = filter(lambda i: i%2 == 0, lista_ejemplo)		#el filter es una funcion filtro, la cual requiere que la funcion regrese true o false para saber si agregar el elemento a la nueva lista
	#filter(filtro(true o false), lista base)		en este caso crearia una lista con todos los valores pares
	print(list(ft))












#	programación orientada a objetos
	

	class Perro:		#la convencion es poner mayuscula la primera letra del nombre de la clase y si es mas de una palabra usar CamelCase
		
		color = "blanco"	#atributo de clase, general a todos los objetos de la clase, para hacer atributos de objetos hay usar self

		def __init__(self, name,age):		#el metodo especial init se ejecuta al crear el objeto
			self.nombre = name		#esto es un atributo, el self se usa para hacer referencia al nombre que tendra el objeto creado a partir de esta clase
			self.edad = age
			print(name)
			print(self)		#el self esta para hacer referencia al objeto especifico de la clase 
		def grrrr(self, x):
			return (f'Grrrrr {x}')


		def ladrido(self):	#esto es un metodo, basicamente una funcion que va adentro de una clase, todos empiezan con el parametro self
			print('ladrido')

		def get_name(self):
			return self.nombre

		def get_age(self):
			return self.age

		def set_age(self, age):
			self.edad = age

	
	#esto es crear una instancia de la clase Perro, asi que ahora flufi va a ser un objeto del tipo Perro, tambies es aca donde se ejecuta el metodo __init__
	
	perro1  = Perro("Flufi",66)	#en los parentesis van los parametros pasados al metodo __init__
	print(perro1.name)		#esto imprimiria el atributo name
	type(perro1)		#type() te dice de que tipo es el objeto.
	

	print(perro1.get_name())
	
	print(perro1.get_age())
	
	print(perro1.grrrr(20))






















class Alumno:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade 	# 0 - 100
	def get_grade(self):
		return self.grade


class Curso:
	def __init__(self, name, max_students):
		self.name = name 
		self.max_students = max_students
		self.students = []
		self.average_note = 0
	
	def add_student(self,student):
		if(len(self.students) < self.max_students):
			self.students.append(student)
			return True
		else:
			return False

	def get_average_grade(self):
		for student in self.students:
			self.average_note += student.get_grade()
		return self.average_note/len(self.students)



jose = Alumno('jose', 16, 78)
maria = Alumno('maria', 16, 70)
pedro = Alumno('pedro', 17, 60)

clase2a = Curso('2A', 22)

clase2a.add_student(jose)
clase2a.add_student(maria)
clase2a.add_student(pedro)

print(clase2a.students)
print(clase2a.students[0].name)