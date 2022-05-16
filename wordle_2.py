if __name__ == "__main__":
   
    print (" Filtrando palabras de 5 letras ")
    with open ('diccionarios.txt', 'r') as diccionario:
        listaPalabras = [str(linea) for linea in diccionario if len(linea) == 6]

    print(" Operación completada con exito ")
    print(" Se encontraron ", str(len(listaPalabras)), " palabras de 5 letras ")
