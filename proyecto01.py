"""
Instrucciones
hacer un programa que juegue piedra, papel o tijera, teniendo al usuario
y la computadora como contrincantes.
"""
import random

#Creamos la funcion, definimos las variables.
def opcion_seleccionada(opt):
    opciones = ["piedra", "papel", "tijera"] 
    return opciones[opt]

print('1) Piedra')
print('2) Papel')
print('3) Tijera')
# Usuario
opcion = int(input('Elige una opcion: '))
juega_usuario = opcion_seleccionada(opcion)
print('Tu eliges: ', juega_usuario)

# PC
#A traves del metodo random hacemos que la computadora elija una de las opciones que hemos definido, al azar.
#Definimos los mensajes a imprimir en pantalla dependiendo de las opciones disponibles.
aleatorio = random.randrange(0, 3)
juega_pc = opcion_seleccionada(aleatorio)
print('La computadora eligió: ', juega_pc)
print('...')
if juega_pc == 'piedra' and juega_usuario == 'papel':
    print('Ganaste, papel envuelve piedra')
    
elif juega_pc == 'papel' and juega_usuario == 'tijera':
    print('Ganaste, Tijera corta papel')
    
elif juega_pc == 'tijera' and juega_usuario == 'piedra':
    print('Ganaste, Piedra pisa tijera')
    
if juega_pc == 'papel' and juega_usuario == 'piedra':
    print('perdiste, papel envuelve piedra')
    
elif juega_pc == 'tijera' and juega_usuario == 'papel':
    print('perdiste, Tijera corta papel')
    
elif juega_pc == 'piedra' and juega_usuario == 'tijera':
    print('perdiste, Piedra pisa tijera')
    
elif juega_pc == juega_usuario:
    print('empate')