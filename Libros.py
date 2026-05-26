#Funciones relacionadas a libros

Libros = [] # lista donde se guardan todos los libros

#Función de agregar libros
def registrar_libro(libros, codigo, titulo, autor, anio, genero): #libro es un diccionario individual (es como ponerle nombre a la i)

    for libro in Libros:
        if libro["codigo"]==codigo:
            print("Error: Ya existe un libro con el código", codigo)
        return
    
    nuevo_libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "genero": genero,
        "estado": "DISPONIBLE"
    }
    Libros.append(nuevo_libro)
    print("Libro registrado con éxito")


'''
PRUEBAS

Ejecución 1: Registrar libro
    registrar_libro(Libros, "L001", "El principito", "Antoine", 1943, "Novela") Funciona

'''