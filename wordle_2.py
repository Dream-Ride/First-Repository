import random

if __name__ == "__main__":
   
    print (" Filtrando palabras de 5 letras ")
    with open ('diccionarios.txt', 'r') as diccionario:
        listaPalabras = [str(linea) for linea in diccionario if len(linea) == 6]

        print(" Operación completada con exito ")
        print(" Se encontraron ", str(len(listaPalabras)), " palabras de 5 letras ")

        def palabra_madre(listaPalabras):
            palabra = random.choice(listaPalabras)
            return palabra
        print(palabra_madre(listaPalabras))        

        entrada = input( " Escribe una palabra de 5 letras: " )

        if entrada in str(listaPalabras) and len(entrada) == 5:
            print( " La palabra es valida " )
        elif len(entrada) == 5 and entrada.isalpha() and entrada not in str(listaPalabras):
            print( " ERROR: La palabra no es valida " )
        elif len(entrada) == 5 and not entrada.isalpha():
            print ( " ERROR: La palabra contiene caracteres no validos " )
        elif len(entrada) != 5 and entrada.isalpha():
            print ( " ERROR: la palabra no contiene 5 letras " )
        elif len(entrada) != 5 and not entrada.isalpha():
            print( " ERROR: La palabra no contiene 5 letras ni caracteres validos " )
