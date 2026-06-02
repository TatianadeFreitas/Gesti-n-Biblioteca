#Funciones relacionadas a libros

Libros = [] # lista donde se guardan todos los libros

#Función de agregar libros
def registrar_libro(codigo, titulo, autor, anio, genero): #libro es un diccionario individual (es como ponerle nombre a la i)

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

def listar_libros(estado=None):
    for libro in Libros:
        #Si no se pasa un estado como argumento muestra todo, sino solo los que coincidan con el argumento pasado
        if estado==None or libro["estado"]==estado:
            print(libro["codigo"], libro["titulo"], libro["autor"], libro["estado"])

#Función para verificar que exista el libro que se quiere prestar
def buscar_libro(codigo):     
    for libro in Libros:
        if libro["codigo"] == codigo:  #recorre y se fija si el codigo esta en los libros agregados
            return libro
    return None 

