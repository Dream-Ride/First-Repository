from colorama import init, Fore
import random

if __name__ == "__main__":
    init()

    print (" Filtrando palabras de 5 letras ")
    with open ('diccionarios.txt', 'r') as diccionario:
        listaPalabras = [str(linea) for linea in diccionario if len(linea) == 6]

        print(" Operación completada con exito ")
        print(" Se encontraron ", str(len(listaPalabras)), " palabras de 5 letras ")
        
        palabra = random.choice(listaPalabras)
        print(palabra)

        entrada = input( " Escribe una palabra de 5 letras: " )

        if entrada in str(listaPalabras) and len(entrada) == 5:
            entrada = entrada
            print(Fore.GREEN + " La palabra es valida " )
        elif len(entrada) == 5 and entrada.isalpha() and entrada not in str(listaPalabras):
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

        numer_letra = 0
        
        for letra in entrada:
            if letra in palabra:
                if letra == palabra[numer_letra]:
                    print(Fore.GREEN + letra, end= "")
                else:
                    print(Fore.YELLOW + letra)
            else:
                print(Fore.RED + letra)
            
            numer_letra += 1
            
