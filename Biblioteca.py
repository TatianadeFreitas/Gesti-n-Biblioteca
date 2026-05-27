#Archivo principal

#Importo los modulos
import sys
from Libros import *

# sys.argv[1] es la opcion que escribe el usuario en la consola
opcion = sys.argv[1]

if opcion == "registrar_libro":
    codigo=sys.argv[2]
    titulo=sys.argv[3]
    autor=sys.argv[4]
    anio=int(sys.argv[5]) #Lo convierto en un número
    genero=sys.argv[6]

    Libros.registrar_libro(codigo, titulo, autor, anio, genero)

elif opcion == "listar_libros":
    Libros.listar_libros()