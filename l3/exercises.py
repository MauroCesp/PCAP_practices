
"""
 mi_lista = [1,2,3,4]

# Cuando uso el : la cosa cambia y no modifica sino que crea un objeto nuevo
mi_lista2 = mi_lista[:]
mi_lista2.append(5)
print(id(mi_lista)==id(mi_lista2))

#print(len(mi_lista))
#print(len(mi_lista2))

# B ----------> Porque se crea un objeto nuevo con otro ID
                # Entonces es una lista nueva con un elemento más
                
# F -------> Como son dos ojetos diferentes tiene un numero de proceso diferente. COmo se comparan los ID el resultado sera false.   
    
    
"""

"""
 mi_lista = [1,2,3,4,-1,-2]


mi_lista = mi_lista[-1:3:-1]
print(mi_lista)
x=6

for elemento in mi_lista:
    # Esto es solo un truco para distraer
    # Es correcto pero de hecho de manera dificil para hacerlo parecer mal
    # ------------> x /=mi_lista[elemento]  Es es lo mismo
    x /=mi_lista[mi_lista[elemento]]
    
    # Un numero dividido entre un negativo simpre da negativo
    # Acordarse que la salida de la X se convierte en este resultado y entra como eso de nuevo.
    
    #1---> X = 6/-2 ---> -3
    #2---> X = -3/-1 --> 3


print(x)   
    
    
"""

"""
    
 # -----------------------Slices
# Es muy recurrente en la PCAP

mi_estruct =(1,2,4,8)

id1 =id(mi_estruct)

mi_estruct = mi_estruct[1:-2]

# El truco aqui es que inicia donde termina
# Hay que recordar que el final no se incluye
# Entonces termina en 4 pero no se incluye :)
# Tiene que lelvar coma para que lo reconozca python como una tupla
# [2,]


id2 = id(mi_estruct)

print(id1, id2, mi_estruct)


# B--------------->  Tiene que lelvar coma para que lo reconozca python como una tupla
# D -----------------> Las tuplas permiten hacer Slicing pero no modificar. Al tener una tupla como entrada la salida en un tupla
# G ----------------> Como no se puede modificar un tupla se crea un objeto nuevo    
    

    
"""

# Por defecto el diccionario arroja las llaves
# Si se quiere interactuar con el contenido se puede utilizar metodos value(), items()
# En el bucle primero se recorre el elemento en la posiicon 0
# Solo 

# Para acceder a clave valor al mismo tiempo es necesario itulizar un metos values() o items() 

mi_dic = {1:[1,3], 2:[2,1], 3:{3,2}}

for item in mi_dic:
    #mi_dic[item][0] = mi_dic[item][1]
    
    print(mi_dic[item][0])
    

# EL programa dar{ aun error