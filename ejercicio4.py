"""Instrucciones
Un numero Armstrong es un numero que es la suma de sus propios digitos
elevados cada uno a la potencia de la cantidad de digitos.
Ejemplo:
9 es un numero Armstrong, porque 9^1 = 9
10 noes un numero de Armstrong, porque 10 != 1^2 + 0^2 = 1
153 es un numero de Armstrong, porque 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 no es un numero de Armstrong, porque= 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

Escribe algun codigo para determinar si un numero es un numero Amstrong

"""

#Solicitamos al usuario que ingrese un numero para verificar si es o no un numero de Amstrong.
numero = int(input("Ingresa un numero para verificarlo: "))

#Inicializamos la suma.
suma = 0

#Hacemos que se halle en la operacion si el numero es o no de Amstrong.
temp = numero
while temp > 0:
   digito = temp % 10
   suma += digito ** 3
   temp //= 10

#Dependiendo del numero ingresado, se muestra el mensaje en pantalla.
if numero == suma:
   print(numero,", es un numero de Amstrong")
else:
    print (numero,", no es un numero de Amstrong")