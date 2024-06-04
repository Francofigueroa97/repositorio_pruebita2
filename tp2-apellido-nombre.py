from os import system
def borrar_pantalla():
   '''para limpiar la pantalla le pedi a python que quiero importar la funcion system (y a diferencia de
       linux o mac OS se utiliza "clear" y en windosw se utiliza "cls")'''
   system("cls")
   return
from pickle import TRUE
import time
'''le pedi que me importe la funcion tiempo para poder usar intervalos de tiempo'''

borrar_pantalla()
'''defini la funcion para poder limpiar la pantalla de carga'''

mensaje_de_carga = ("cargando...")

'''cree el punto que queria hacer acontinuacion (pero no pude hacer que me quede acontinuacion del cargando)'''
print(mensaje_de_carga)
time.sleep(3)
'''imprimi el mensaje "cargando". '''

borrar_pantalla()

print("¿hola buenos dias como te llamas?")
time.sleep(2)
'''imprimi el mensaje tiempo despues de haber borrado el anterior cartel y le pedi 2 segundos despues'''

def pedir_nombre():
      print ("nombre:", {nombre})
      return
nombre = input("nombre: ").strip()
'''defini la funcion nombre, y le pedi que me lo guarde'''


def pedir_apellido():
    print ("apellido: ",{apellido})
    return
apellido = input("apellido: ").strip()
'''defini la funcion apellido, y le pedi que me lo guarde los caracteres y borre los espacios en blanco'''


apellido_letras = ''
for letras in apellido:
     if letras.isalpha():
          apellido_letras += letras
'''le solicite que verificara que si todos los caracteres que tiene la cadena que introduci estan en el alfebeto y te entrega un TRUE
si es correcto y FALSE si no lo es'''


nombre_letras = ''
for letras in nombre:
     if letras.isalpha():
          nombre_letras += letras
'''repito lo echo anteriormente'''
          

apellido_editado = apellido_letras[0].upper() + apellido_letras[1:].lower()
nombre_editado = nombre_letras[0].upper() + nombre_letras[1:].lower()
'''cree que el nombre completo pidiendo que entregue solamente la primer letra en mayuscula con .upper y el resto de las letras 
en minusculas con .lower y que siempre respete esta confifuracion'''


nombre_completo = apellido_editado + ', ' + nombre_editado 

'''pregunta completa y saludo al usuario'''
nombre_y_pregunta = ("hola " + apellido_editado + ', ' + nombre_editado + '. ')

print(nombre_y_pregunta)
lista_parientes = []

'''consulta si quiere continuar con el programa'''
while True:
    respuesta_usuario = input("¿deseas continuar? (si/no): ").strip().lower()
    '''si quiere continuar te pregunta si nos preguntarias con quien vive'''
    
    if respuesta_usuario == "si":
        
        input("con quien vives?(solo introduce un nombre): ")
        while True:
            
            respuesta_usuario = input("con alguien mas?:  ").strip().lower()
            if respuesta_usuario == "si":
                pariente = input("nombre: ")
                lista_parientes.append(pariente)
                '''si no quiere le diga que cierre el bucle y diga "okey, que tenga buen dia."'''
            elif respuesta_usuario == "no":
                print("Okey, Que tenga un buen día.")
                break
            else:
                print("Por favor, responda 'si' o 'no'.")
                
            
    elif respuesta_usuario == "no":
        print("Okey, Que tenga un buen día!.")
        
        break
    else:
        print("Por favor, responda 'si' o 'no'.")
       
borrar_pantalla()


print( "tus parientes son:",lista_parientes) 
time.sleep(2)     
'''imprime la lista de personas con las que vive'''


borrar_pantalla()
'''borrras la pantalla para poder seguir con otro ejercicio sobre ecuaciones'''

numero_decimal = float(input("introduce un numero decimal para sumar: "))
'''introduce un numero decimal y usando un floal para que entienda que puede ser un numero decimal'''
        
numero_entero = int (input("introduce el numero entero: "))
'''introduce el numero entero que va a usar en la ecuacion explicando que solo quiero un numero entero'''

'''resuelve la ecuacion'''
resultado = (numero_decimal * numero_entero)

'''imprime el mensaje de la ecuacion'''
mensaje_ecuacion = "el resultado de la otra ecuacion es de ", numero_decimal, "*", numero_entero, "es ", resultado
print (mensaje_ecuacion)
time.sleep(2.5)
borrar_pantalla()

'''hago un diccionario donde estan los alumnos con los que curso y la clave el es el lugar donde se encuentran centado'''
diccionario = {}
'''le pido que agrege a un alumno'''
while True:
    
    print("agrege el nombre del alumno: ")
    diccionario[input("agregue el lugar del alumno: ")] = input()
    time.sleep(2)
    alumno_agregado = input("quiere agregar mas alumnos (si/no): ")

    if  alumno_agregado == "si":
         print("agrege el nombre del alumno: ")
        
        diccionario.append[input("agregue el lugar del alumno: ")] = input()
    
    elif alumno_agregado != "si" , "no":


    '''imprime el diccionario'''
    print("los alumnos que estan en el aula son ",diccionario)
    
        



          
