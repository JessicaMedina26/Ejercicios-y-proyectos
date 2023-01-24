"""Instrucciones
Crear una funcion para validacion de nombres de usaurios.
Dicha funcion debera validar lo siguiente:
- El nombre de usuario debe contener un minimo de 6 caracteres y un maximo de 12
- El nombre de usuario debe ser alfanumerico.

Requisitos
1- Nombre de usuario con menos de 6 caracteres, retorna el mensaje. 
'El nombre de usuario debe contener al menos 6 caracteres'
2- Nombre de usuario con mas de 12 caracteres, retorna el mensaje.
'El nombre de usuario no puede ontener mas de 12 caracteres'
3- Nombre de usuario con caracteres distintos a los alfanumericos, retorna el mensaje.
'El nombre de usuario puede contener solo letras y numeros'
4- Nombre de usuario valido, retorna 'Correcto!'
"""
#Definimos la funcion para validar el nombre de usuario y determinamos que es un str y otorgamos una variable que lea caracteres alfanumericos.
def validar_usuario(nombre_usuario: str):
    try:
        longitud_usuario = len(nombre_usuario)
        es_alfanumerico = nombre_usuario.isalnum()
    #definimos que si tiene menos de 6 caracteres, imprima el mensaje y que vuelva a ingresar otro nombre. 
        if longitud_usuario < 6:
            raise ValueError("El nombre de usuario debe contener al menos 6 caracteres")
      #validamos que no deba tener mas de 12 caracteres.  
        if longitud_usuario > 12:
            raise ValueError("El nombre de usuario no puede ontener mas de 12 caracteres")
     #validamos que si se ingresa caracteres especiales, imprima el mensaje.   
        if es_alfanumerico == False:
            raise ValueError("El nombre de usuario puede contener solo letras y numeros")

        return True        
    except ValueError as ve:
        print(ve)
        return False

#Hacemos que mientras no se ingrese el nombre de forma correcta, siga pidiendo al usuario que ingrese otro nombre.
def run():
    usuario_valido = False
    while usuario_valido == False:
        nombre_usuario = input("Escribe el nombre de usuario: ")
        if validar_usuario(nombre_usuario) == True:
            print("Correcto!")
            usuario_valido = True


if __name__ == '__main__':
    run()