"""
Instrucciones
Escribir un programa en el que se pregunte al usuario por una frase y una letra
y muestre por pantalla el numero de veces que aparece la letra en la frase,
seguido del porcentaje de veces que aparece la letra en la frase
"""
#Primeramente definimos la función  para obtener el porcentaje y asignamos los parámetros, nombres de variables en los cuales se almacenará la información ingresada por el usuario así como el tipo de variable. 
def obtener_porcentaje(cantidad, cadena):
    longitud = len(cadena)
    porcentaje = cantidad * 100 / longitud
    return porcentaje

def run():
    
    #Definimos la variable y el campo para ingresar la frase.
        frase = input("Escribe una frase: ")
        
        #definimos que la frase debe contener mas de una letra.
        if len(frase) <= 1:
            raise ValueError("Debe escribir una frase")

        letra = input("Escriba una letra: ")
        if len(letra) <= 0 or len(letra) > 1:
            raise ValueError("Debe escribir una letra")
        #Definiendo la variable ocurrencias determinamos que es igual a la frase con el metodo count para verificar cuantas veces aparece la letra elegida, en la frase, pasandole el argumento letra.
        ocurrencias = frase.count(letra)
        #Determinamos el porcentaje de la ocurrencia.
        porcentaje_ocurrencias  = obtener_porcentaje(ocurrencias, frase)
        print(f"El nro. de veces que aparece la letra ingresada es: {ocurrencias} siendo un porcentaje de: {porcentaje_ocurrencias}%")
    

if __name__ == '__main__':
    run()