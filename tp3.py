import time
import os

# Definir el número de repeticiones
num_repeticiones = 2

# Definir el intervalo de tiempo entre repeticiones en segundos
intervalo_tiempo = 1

# Bucle que se ejecutará num_repeticiones veces
while num_repeticiones > 0:
    # Imprimir el mensaje
    print("Este es un mensaje temporal")

    # Esperar el intervalo de tiempo especificado
    time.sleep(intervalo_tiempo)

    # Decrementar el número de repeticiones
    num_repeticiones -= 1

    lista_de_familiares = []

     

     
     
def borrar_pantalla():
   os.system ('cls')
   return


borrar_pantalla()
print("ya se limpio")

import os
import time

def borrar_pantalla():
    '''Limpia la pantalla. En Windows se usa "cls" y en Unix (Linux/macOS) se usa "clear".'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Configuración del mensaje de carga
repeticiones = 3
intervalo = 1
mensaje_de_carga = "cargando"

# Bucle para mostrar el mensaje de carga con puntos actualizándose
for i in range(repeticiones):
    borrar_pantalla()
    puntos = '.' * (i % 3 + 1)  # Genera de 1 a 3 puntos
    print(mensaje_de_carga + puntos)
    time.sleep(intervalo)

# Limpia la pantalla al final del proceso
borrar_pantalla()
print("Proceso completado.")
while True:
    respuesta_usuario = input("deseas continuar?:  ").strip().lower().isalpha()

    if respuesta_usuario == "si":
        pariente = print("genial! ")
        time.sleep(2)
    elif respuesta_usuario == "no":
        print("Okey, Que tenga un buen día.")
        break
    else:
        print("Por favor, responda 'si' o 'no'.")
borrar_pantalla()

''' esto es lo que tengo que modificar'''
comentarios = []

while True:
    respuesta_usuario = input("deseas continuar?:  " "si/no").strip().lower()

    if respuesta_usuario == "si":
        respuesta_usuario = print("genial! ")
        time.sleep(2)
    elif respuesta_usuario == "no":
        print("Okey, Que tenga un buen día.")
        break
    else:
        print("Por favor, responda 'si' o 'no'.")
borrar_pantalla()
print( " tus parientes son:", comentarios)