#Archivo principal
#Importo los modulos
import sys
import Libros
import Prestamos


# sys.argv[1] es la opcion que escribe el usuario en la consola
opcion = sys.argv[1]

if opcion == "registrar_libro":
    codigo=sys.argv[2]
    titulo=sys.argv[3]
    autor=sys.argv[4]
    anio=int(sys.argv[5]) #Lo convierto en un número
    genero=sys.argv[6]

    Libros.registrar_libro(codigo, titulo, autor, anio, genero)
    Libros.guardar_libros()

elif opcion == "listar_libros":
    if len(sys.argv) > 2: #Si la cantidad de ELEMENTOS de la lista es mayor a dos es porque el usuario especifica que libros quiere listar, entonces (estado) se pasa como argumento
        estado = sys.argv[2]
        Libros.listar_libros(estado)
    else:
        Libros.listar_libros() #Si no se epecifica lista todo

elif opcion == "prestar_libro":
    codigo_libro=sys.argv[2]
    nombre_persona=sys.argv[3]
    fecha_prestamo=sys.argv[4]
    fecha_devolucion=sys.argv[5]

    Prestamos.prestar_libro(codigo_libro, nombre_persona, fecha_prestamo, fecha_devolucion)
    Prestamos.guardar_prestamos()
    Libros.guardar_libros() # Se usa aca también ya que se genera una modificación en el archivo


elif opcion == "devolver_libro":
    codigo_libro=sys.argv[2]

    Prestamos.devolver_libro(codigo_libro)
    Prestamos.guardar_prestamos()
    Libros.guardar_libros()

elif opcion == "listar_prestamos":
    Prestamos.listar_prestamos()

else:
    print("Error: Opción no válida.")
    sys.exit()

