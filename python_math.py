import math

x = 2.345

 # print(round(x)) # redondea el valor segun el primer decimal dejando solo la parte entera 
 # print(round(x,1)) # puede tener de 2do parametro el nro de digitos decimales redondeados

print(math.ceil(x)) # siempre redondea hacia arriba sin importar el primer decimal
print(math.floor(x)) # siempre redondea hacia abajo sin importar el primer decimal
print(math.trunc(x)) # solo retorna la parte entera

numeros = [1,2,3,4,5,6,7,8,9,10]

print(math.fsum(numeros)) #suma todos los objetos de un iterable

print(math.fabs(-4)) #devuelve el valor absoluto de un numero

print(math.fmod(17,6)) # devuelve el modulo(residuo) de dividir el primer parametro por el segudo

print(math.exp(2)) # rotorna e(2.71828) elevado al parametro dado

print(math.pi) # simplemente pi

print(math.pow(2,6)) # eleva al primer parametro por el segundo

print(math.sqrt(64)) # raiz cuadrada

print(math.hypot(2,3)) # dado los dos catetos te la la hipotenusa de un triangulo rectangulo

print(math.radians(90)) # convierte los grados a radianes

print(math.sin(90)) # devuelve el seno de los grados pasados

print(math.remainder(16, 5)) #devuelve el residuo
