import random
import string
Contraseñas = {}




def menu():
    
    
 print("***********WELCOME***********")
 print("Generador de Contraseñas V0.1")
 print("*****************************")
 #print("Seleccione una de las siguientes opciones:")
 while True:
        print("Seleccione una de las siguientes opciones:")
        print("1. Generar Contraseña solo de Letras")
        print("2. Generar Contraseñas solo de Numeros")
        print("3. Generar Contraseña Letras y Numeros")
        print("4. Generar Contraseña Letras, Numeros y Caracteres")
        print("5. Salir")
        

        print("-----------------------------------------")
        opcion = input("Escriba la opción seleccionada: ")
        if opcion == '5' :
            print("Gracias por utilizar el Generador De Contraseñas, Hasta Luego")
            print("Saliendo......")
            break

        
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        if opcion == '1':
           contraseña = Generar_Letras(longitud)
           print("----------------------------------")
           print(f"Contraseña Generada: {contraseña}")
           print("----------------------------------")
  

        elif opcion == '2':
            contraseña = Generar_Numeros(longitud)
            print("----------------------------------")
            print(f"Contraseña Generada: {contraseña}")
            print("----------------------------------")
        elif opcion == '3':
            contraseña = Generar_LetNum(longitud)
            print("----------------------------------")
            print(f"Contraseña Generada: {contraseña}")
            print("----------------------------------")
        elif opcion == '4': 
             contraseña = Generar_LetNumCar(longitud)
             print("----------------------------------")
             print(f"Contraseña Generada: {contraseña}")
             print("----------------------------------")
        

def Generar_Letras(longitud) :
     letras = string.ascii_letters  # Letras mayúsculas y minúsculas
     return ''.join(random.choice(letras) for _ in range(longitud))

def Generar_Numeros(longitud):
    numeros = string.digits  # Números del 0 al 9
    return ''.join(random.choice(numeros) for _ in range(longitud))

def Generar_LetNum(longitud):
    letras_numeros = string.ascii_letters + string.digits
    return ''.join(random.choice(letras_numeros) for _ in range(longitud))

def Generar_LetNumCar(longitud):
    completos = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(completos) for _ in range(longitud))


# Iniciar el programa
menu()