from ast import For
import colorama 
from colorama import Fore, Back
colorama.init(autoreset=True)

import random

lista_palabras = []
diccionario = open("diccionarios.txt", mode= "r")

def filtrar_palabras():
    cantidad_de_palabras = 0
    for palabra in diccionario:
        if len(palabra) == 6:
            lista_palabras.append(palabra.strip("\n"))
            cantidad_de_palabras += 1

def analizar(entrada):
    numer_letra = 0
    for letra in entrada:
        if letra in palabra:
            if letra == palabra[numer_letra]:
                print(Fore.GREEN + letra, end= "")
            else:
                print(Fore.YELLOW + letra, end= "")
        else:
            print(Fore.RED + letra, end= "")
        numer_letra += 1
        if numer_letra == 5:
            break

if __name__ == "__main__":

    print (" Filtrando palabras de 5 letras ")
    filtrar_palabras()
    print(" Operación completada con exito ")
    print(" Se encontraron ", str(len(lista_palabras)), " palabras de 5 letras ")
        
    palabra = random.choice(lista_palabras)
    print(palabra) 

    entrada = input( " Tienes 5 intentos para encontrar la palabra. \n Escribe una palabra de 5 letras: " ).casefold()
    n_entrada = 0

    for n_entrada in range (0,5):
        while entrada not in str(lista_palabras):
            if len(entrada) == 5 and entrada.isalpha() and entrada not in str(lista_palabras):
                print(Fore.RED + " ERROR: La palabra no es valida " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " )
            elif len(entrada) == 5 and not entrada.isalpha():
                print (Fore.RED + " ERROR: La palabra contiene caracteres no validos " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " )
            elif len(entrada) != 5 and entrada.isalpha():
                print (Fore.RED + " ERROR: la palabra no contiene 5 letras " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " )
            elif len(entrada) != 5 and not entrada.isalpha():
                print(Fore.RED + " ERROR: La palabra no contiene 5 letras ni caracteres validos " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " )
            else:
                break
        if n_entrada == 4 and entrada != palabra:
            print(Fore.RED + " \n Perdiste " )
            break
        if entrada != palabra:
            analizar(entrada)
            entrada = input(Fore.WHITE + " \n Introduce otra palabra: " ).casefold()
            n_entrada += 1
        if entrada == palabra:
            print (Fore.GREEN + palabra)
            print(Fore.GREEN + " \n Palabra encontrada " )
            break
