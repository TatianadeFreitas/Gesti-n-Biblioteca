#Funciones relacionadas a libros
import json

Libros = [] # lista donde se guardan todos los libros

#Función de agregar libros
def registrar_libro(codigo, titulo, autor, anio, genero): #libro es un diccionario individual (es como ponerle nombre a la i)

    for libro in Libros:
        if libro["codigo"]==codigo:
            return False
    
    nuevo_libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "genero": genero,
        "estado": "DISPONIBLE"
    }
    Libros.append(nuevo_libro)
    return True

def listar_libros(estado=None):
    for libro in Libros:
        #Si no se pasa un estado como argumento muestra todo, sino solo los que coincidan con el argumento pasado
        if estado==None or libro["estado"]==estado:
            print(libro["codigo"], libro["titulo"], libro["autor"], libro["estado"])

#Función para verificar que exista el libro que se quiere prestar
def buscar_libro(codigo):     
    for libro in Libros:
        if libro["codigo"] == codigo:  #Recorre y se fija si el codigo esta en los libros agregados
            return libro
    return None 

def guardar_libros():
    with open("Libros.json", "w", encoding="utf-8") as archivo_Lib:
        json.dump(Libros, archivo_Lib, ensure_ascii=False, indent=4) # Primero va lo que quiero guardar (en este caso la lista Libros), después va en donde lo guardamos (en este caso en el archivo Libros.json esta almacendao en la variable archivo_Lib)

def cargar_libros(): #Función usada para leer el contenido del archivo json creado con la función guardar_libros
    global Libros # Sirve para que la función use la variable Libros que ya existe fuera de ella
    try:
        with open("Libros.json", "r", encoding="utf-8") as archivo_Lib:
            Libros = json.load(archivo_Lib)
    except:
        Libros = []

   