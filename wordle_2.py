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

    filtrar_palabras()        
    palabra = random.choice(lista_palabras)
    
    print(Fore.WHITE + " Tienes 5 intentos para encontrar la palabra. " )
    print(Fore.WHITE + " Si la letra aparece en " + Fore.GREEN + " verde" + Fore.WHITE + ", entonces la letra se encunetra en ese lugar. " )
    print(Fore.WHITE + " Si la letra aparece en " + Fore.YELLOW + " amarillo" + Fore.WHITE + ", entonces la letra pertenece a la palabra pero no se encuentra en ese lugar. " )
    print(Fore.WHITE + " Si la letra aparece en " + Fore.RED + " rojo" + Fore.WHITE + ", entonces la letra no pertenece a la palabra. " )
    
    entrada = input( " Escribe una palabra de 5 letras: " ).casefold()
    n_entrada = 0

    for n_entrada in range (0,5):
        while entrada not in str(lista_palabras):
            if len(entrada) == 5 and entrada.isalpha() and entrada not in str(lista_palabras):
                print(Fore.RED + " ERROR: La palabra no es valida " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " ).casefold()
            elif len(entrada) == 5 and not entrada.isalpha():
                print (Fore.RED + " ERROR: La palabra contiene caracteres no validos " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " ).casefold()
            elif len(entrada) != 5 and entrada.isalpha():
                print (Fore.RED + " ERROR: la palabra no contiene 5 letras " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " ).casefold()
            elif len(entrada) != 5 and not entrada.isalpha():
                print(Fore.RED + " ERROR: La palabra no contiene 5 letras ni caracteres validos " )
                entrada = input(Fore.WHITE + " Introduce otra palabra: " ).casefold()
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
