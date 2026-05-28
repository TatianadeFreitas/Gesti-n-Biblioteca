#Funciones relacionadas a los préstamos
from datetime import datetime #funcion de python que se usa para convertir texto en una fecha real que Python pueda operar
import Libros #Modulo 

Prestamos = [] #lista donde se guardan prestamos 

def prestar_libro(codigo, nombre_persona, fecha_prestamo_str, fecha_devolucion_str):

    libro = Libros.buscar_libro(codigo)  # busca funcion en modulo Libros
    if libro is None:
        print("Error: No existe un libro con el código:", codigo)
        return  # sale de la función  

    if libro["estado"] != "DISPONIBLE":
        print("Error: El libro", codigo, "no está disponible")
        return #en caso de si estar disponible, sigue con el codigo de fechas de prestamo y devolución

    fecha_p = datetime.strptime(fecha_prestamo_str, "%Y-%m-%d") #convierte el texto que ingresa el usuario en fecha
    fecha_d = datetime.strptime(fecha_devolucion_str, "%Y-%m-%d") #analiza fecha de devolución
    
    if fecha_d < fecha_p:
        print("Error: La fecha de devolución no puede ser anterior al préstamo")
        return   
    Prestamos.append({ #se agrega un nuevo prestamo a la lista mediante un diccionario
        "codigo_libro": codigo,
        "nombre_persona": nombre_persona,
        "fecha_prestamo": fecha_prestamo_str,
        "fecha_devolucion": fecha_devolucion_str
    })
    libro["estado"] = "PRESTADO"
    print("Libro prestado con éxito.")