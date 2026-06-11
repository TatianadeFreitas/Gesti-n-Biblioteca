#Funciones relacionadas a los préstamos
import json
from datetime import datetime #funcion de python que se usa para convertir texto en una fecha real que Python pueda operar
import Libros #Modulo 

Prestamos = [] #lista donde se guardan prestamos 


def prestar_libro(codigo_libro, nombre_persona, fecha_prestamo_str, fecha_devolucion_str):

    libro = Libros.buscar_libro(codigo_libro)  # busca funcion en modulo Libros
    if libro is None:
        return 1  # sale de la función  

    if libro["estado"] != "DISPONIBLE":
        return 2 #en caso de si estar disponible, sigue con el codigo de fechas de prestamo y devolución

    fecha_p = datetime.strptime(fecha_prestamo_str, "%Y-%m-%d") #convierte el texto que ingresa el usuario en fecha
    fecha_d = datetime.strptime(fecha_devolucion_str, "%Y-%m-%d") #analiza fecha de devolución
    
    if fecha_d < fecha_p:
        return 3  
    
    Prestamos.append({ #se agrega un nuevo prestamo a la lista mediante un diccionario
        "codigo_libro": codigo_libro,
        "nombre_persona": nombre_persona,
        "fecha_prestamo": fecha_prestamo_str,
        "fecha_devolucion": fecha_devolucion_str
    })
    libro["estado"] = "PRESTADO"
    return 0


def devolver_libro(codigo_libro): #funcion devolver libro
    global Prestamos  # Se declara global para que Python modifique la lista original del módulo y no cree una copia local
    libro = Libros.buscar_libro(codigo_libro) #llama la funcion definida en el modulo Libros
    if libro is None:      
        return 1
    
    if libro["estado"] != "PRESTADO": #corroboramos que el libro este prestado
        return 2

    for i, prestamo in enumerate(Prestamos): #enumerate va contando la posicion de i / enumerate da la posición y el valor
        if prestamo["codigo_libro"] == codigo_libro:
            Prestamos.pop(i) #con pop frenamos la lista y nos quedamos con ese valor de i , encontrado por enumerate
            break
    libro["estado"] = "DISPONIBLE"
    return 0

def listar_prestamos():
    if not Prestamos: #si la lista esta vacia
        return False

    for p in Prestamos: #p es cada prestamo de la lista
        print(p["codigo_libro"], p["nombre_persona"], p["fecha_prestamo"], p["fecha_devolucion"])
    return True

def guardar_prestamos():
    with open("Prestamos.json", "w", encoding="utf-8") as archivo_Pres:
        json.dump(Prestamos, archivo_Pres, ensure_ascii=False, indent=4) 

def cargar_prestamos():
    global Prestamos
    try:
        with open("Prestamos.json", "r", encoding="utf-8") as archivo_Pres:
            Prestamos = json.load(archivo_Pres)
    except:
        Prestamos = []

