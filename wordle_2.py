if __name__ == "__main__":
    print (" Filtrando palabras de 5 letras ")
    diccionario = open(diccionarios.txt)
    lista_palabras = []
    for linea in diccionario:
        linea = diccionario.redline()
        #if letras en palabra = 5 => agregar a lista
        if len(linea) == 5:
            lista_palabras.append(linea)
            
        if linea == 1290:
            break
    #palabras = cantidad de palabras en lista_palabras
    print(" Operación comppletada con exito ")
    print(" Se encontraron str(len(lista_palabras)) palabras de 5 letras ")
