"""Instrucciones
Los estudiantes consultan la nota que recibiran segun las calificaciones que obtuvieron.
Ejemplo:
Las calificaciones 4,5,3. Daran la nota 4.
Las calificaciones 3,2,5. Daran la nota 3,33.

Escribe algun codigo para determinar la nota de un estudiante.
"""
#Definimos la función para validar los números de las calificaciones. con la función assert, nos aseguramos de que no
# se retorne un número negativo, nos ayuda a cazar condiciones que no deben ocurrir nunca. 
def validar_numero(nro):
    try:
        assert nro.isnumeric() and int(nro) > 0, "Debes ingresar un numero"
    #El assert es una instruccion de Python que te permite definir condiciones que deban cumplirse siempre. En caso
    #que la expresion booleana sea True assert no hace nada y en caso de False dispara una excepcion.
        return int(nro)
    except AssertionError as ve:
    #Con "AssertionError" se va capturando los errores.
        print(ve)
        return False

#En esta función se realiza la operación de capturar las calificaciones e imprimir en pantalla la nota final.
#Se utiliza round para que puedan mostrarse los resultados con decimales y mostramos hasta 2 decimales en este caso.

def run():

    calif1 = validar_numero(input("Escriba 1ra calificacion: "))
    calif2 = validar_numero(input("Escriba 2da calificacion: "))
    calif3 = validar_numero(input("Escriba 3ra calificacion: "))
    

    total_calificacion = calif1 + calif2 + calif3
    nota = total_calificacion / 3

    print(f"La Nota obtenida es: {round(nota, 2)} ")

if __name__ == '__main__':
    run()
    