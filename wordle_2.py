from colorama import init, Fore
import random

def evaluar(entrada):
    while entrada not in str(listaPalabras):
        if len(entrada) == 5 and entrada.isalpha() and entrada not in str(listaPalabras):
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

def analizar(entrada):
    for letra in entrada and numer_letra in range (0,4):
        if letra in palabra:
            if letra == palabra[numer_letra]:
                print(Fore.GREEN + letra, end= "")
            else:
                print(Fore.YELLOW + letra, end= "")
            if letra not in palabra:
                print(Fore.RED + letra, end= "")
            break

if __name__ == "__main__":
    init()

    print (" Filtrando palabras de 5 letras ")
    with open ('diccionarios.txt', 'r') as diccionario:
        listaPalabras = [str(linea) for linea in diccionario if len(linea) == 6]

        print(" Operación completada con exito ")
        print(" Se encontraron ", str(len(listaPalabras)), " palabras de 5 letras ")
        
        palabra = random.choice(listaPalabras)
        print(palabra)

        entrada = input( " Escribe una palabra de 5 letras: " ).casefold()
        n_entrada = 0
        evaluar(entrada)

        while n_entrada < 5:
            if entrada == palabra:
                    print (Fore.GREEN + palabra)
                    print (Fore.WHITE + " La palabra es valida \n Palabara encontrada " )
                    break
            numer_letra = 0
            numer_letra += 1
            if numer_letra == 5:
                entrada = input( " Introduce otra palabra " )
                evaluar(entrada)
                n_entrada += 1
                break
            if n_entrada == 5 and entrada != palabra:
                print(Fore.RED + " Perdiste " )

            
