# PREGUNTA 1

from mimodulo1 import *
from mimodulo2 import *
from mimodulo1 import *
from mimodulo2 import *

print(MODULO)

# La respuesta correcta es B ----> MODULO 1 MODULO2 2
    # Cada importacion de los modulos se realiza una sola vez
    # Se inicializa el modulo la primera vez que se importa
    # Como la ultima importacion es del modulo 2, el valor que adquiere la variable MODULO es la de este modulo



# PREGUNTA 2

# La respuesta correcta es la C -----------> Index Error
    # Python vaintentado cada exception en order descendente. Si el error no pertenece a una Exepcion pasa a la siguiente.
    # En este caso mi_lista no tiene un indice 3, por lo cual es un index error


# Pregunta 3
# La respuesta correcta es la_
    # B ---------> Value Error porque se intenta leer como entero un numero decimal
    # E ---------> FINALLY  porque esta instruccion se ejecuta siempre, no importa si el programa da error o no
    



# Pregunta 4
# La respuesta correcta es la B ------------> ***

        # DEfino una funcion dentro de la fucnion para que devuelve el valor o el objeto que he  creado dentro
        # Si yo quiero el resultado en cualquier momento fuera de la funcion lo puedo tener con el cierre
        # el '*' se multiplica por el numero que recibe por parametro.
        # Accedo a los valores y los sumo dentro del print.


def o (p):
    
    def q():
        return p * '*'
    return q

r = o(1)
s = o(2)

print(r() + s())

# Pregunta 5
# La respuesta correcta es la  E --------------> [4,16,36,64]

# La funcion no devuelve el valor sino el objeto iterador
# El rango que se toma de la cadena es '2,4,6,8', porque tiene un el range tien un salto de 20 y comienza desde  el elemento 1
# La cadema se convierte en entero y se pasa
# Creo la lista a partir de los que me regresa la funcion I()
# Despues se utiliza map para regresar una nueva lista con lo que regrese la funcion Lambda, la cual eleva al cuadrado cada elemento de mi_lista
# FInalmente se imprime la nueva lista.