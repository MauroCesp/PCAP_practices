class MiClase:
    var=0
    def __func():

        MiClase.var +=1 
        return MiClase.var
    
o = MiClase()

# using the instance method call syntax is not correct
o._MiClase__func()

print(o._MiClase__func())




# Un guion bajo significa que la clase es privada.
# Pero si uso dos guines bajo
# Esto da un error esto activa una funcionalidada que cambia el nombre del metodo a _MiClase__func()
# Entonces cuando imprimo en pantalla sigo llamando a un metodo privado sin haberle cambialo el nombre
# Porque utilizo el nombre que ahora tienen ese metodo, que sigue siendo privado


#################################

'''
¿Cuál o cuáles de las siguientes líneas de código funcionarán sin problemas 
cuando se sustituya el comentario por ella dentro del método inc() para que 
la salida del fragment de código sea igual a 3? (una o varias opciones)


A) put(self.prop + val)
B) self.put(self.get() + val)---------------->
C) self.put(get() + val)
D) self.put(self.prop + val) ---------> 
E) self.put(prop + val)
'''
class MiClase:
    var=0
    def __init__(self):
        MiClase.var +=1 
        self.prop = MiClase.var
    
    def get(self):
        return self.prop
    
    def put(self, val):
        self.prop = val
    
    def inc(self, val):
        # Aqui va la linea de codigo
        
    
o = MiClase()

o.inc(2)
print(o.get)

#######################################

# Esta es la respuesta correcta
# E ---------------> False == 0
# F----------------> 46 == 46.0
# C---------------> 'a' not in 'ABC'

##########################################

def mi_funcion(x, y=1):
    if x == 1:
        return 1
    return x + mi_funcion(x-y)

print (mi_funcion(2))

# El resultado es 3
# Porque X toma el valor de 2
# Como X no es igual a 1 ejecuta el segundo return
# Aqui X es igual a 2 y el resultado de la funcion es 1 (2-1), entonces los sumo
# Revisar si escibi el ejercicio correctamente

###########################################

def mi_funcion(n):
    for i in range(1,n+1,2):
        yield i

for i in mi_funcion(4):
    print(i, end='')

# El resultado es 1 3
# Recibo 4 como argumento dentro de la funcion
# Al trabajar con range voy a comenzar desde la posicion 1 hasta la posicion n+1 (4), con un salto de 2
# Es decir que el rango es (0,1,2,3,4) y me quedarias un rango de (1,3) 
# Una vez que se ejecuta el Yield me regresa dos valores (1,3)
# Al llamar el objeto iterador se le indica que haga un print sin salto de linea, por lo que los dos valores quedan sobre una misma linea


###########################################   --------- REVISAR Jupyter
# Si necesitas capturar y manejar dos excepciones diferentes llamadas Ex1 y
# Ex2 en una única rama except, puedes escribirlo de la siguiente manera o maneras: (una o varias opciones)

# A) except Ex1 Ex2:
# B) except (Ex1, Ex2):
# C) except Ex1, Ex2:
# D) except Ex1+Ex2:

############################################

i = -5
while i < 0:
    i = i // 2
    if i % 3 == 0:
        break
else:
    i -= 4
print(i)

# -3
# The reason for this is that the // operator in Python performs integer division and rounds the result down to the nearest integer. 
# #In this case, -5 divided by 2 would result in -2.5, but since the result is rounded down to the nearest integer, it becomes -3.


#############################################

list1 = [1,2,3,4]
list2 = list1[-3: -1]

print('Antes', list2)


# Aqui lo que pasa es que asigna la negacion del primer elemento 
# Es decir no cambia toda la lista sino solo ese elemento. Entonces pasa a ser -3
list2[0] = -list2[1]

print(list1, list2)


##############################################

#Un constructor de una clase superclase: (una o varias opciones)

# A) Puede devolver cualquier valor con la sentencia return.
# B) No puede ser invocado directamente dentro de la clase.
# C) Puede ser invocado directamente por cualquiera de sus subclases.
# D) Puede ser invocado directamente por cualquiera de sus superclases.

###############################################

# Dada la siguiente función, selecciona la línea o líneas de código que al
# ejecutarse posteriormente no terminarán en excepcion: (una o varias opciones)

def mi_funcion(a, b = 0):
    c = a*b 
    # Linea de codigo

''' 
A) x = mi_funcion(b=1)
B) mi_funcion(b=1)
C) x = mi_funcion(a=0)
D) mi_funcion(a=0)
# Dan error porque si se llama a un argumento por key word, tiee que estar siempre detras de los argumetnos de posicion. EN estos ejemplos se coloca de primero
E) x = mi_funcion(b=1, 0)
F) mi_funcion(b=1, 0)
G) x = mi_funcion(1)
H) mi_funcion(1)

'''

###########################################333

'''
Si necesitas leer un sólo caracter desde un stream llamado s, ¿qué
instrucción utilizarías? (1 opción)
A) ch = read (s, 1)
B) ch= s.input (1)
C) ch= input (s, 1)
D) ch= s.read (1)
'''

#################################################


'''
Porque si no encuentra el metodo dentro de la misma clase se va a buscar dentro de la clase padre. En el primero caso es en este caso A y el segundo caso es B. 

Al llamar al metdo do() se invoca un metodo self.b() que solo existe en la clase A. 

Pero en el caso de self.a(), como le metodo se puede localizar dentro de la misma clase toma el valor de la clase y no del valor de A. 
'''
class A:
    def a(self):
        print('A', end ='')
    def b(self):
        self.a()

class B(A):
    def a(self):
        print('B', end ='')
    def do(self):
        self.b() 

class C(B):
    def a(self):
        print('C', end ='')
    def do(self):
        self.b() 

B().do()
C().do()

#############################################
'''
No se puede realizar una resta de cadenas de texto porque son inmutables. Ademas no se les puede aplicar una operación aritmetica pues no son enteros o flotantes. 
'''
s = '******'
s = s - s[1:2]
print(s)

############################################

mi_variable = ()
'''
¿Cuál o cuáles de las siguientes acciones se puede realizar después de
declarar la variable mi_variable de la siguiente forma? (una o varias opciones)

# Esto hace un slice pero sigue siendo un atupla vacia
A) mi_variable[:]

# La tuplas son inmutables , no s epueden modificar una vez creadas.
B) mi_variable.append(0)

# Esto no vale porque la tupla no tiene ningun elemento
C) mi_variable[0]

# Aqui tambien se intenta modificar la tupla
D) mi_variable[0] = 5

# Esto si se puede hacr para eliminar la tupla por completo de la memoria.
E) del mi_variable

'''
###############################################

x = a.b.c.f()
'''
¿Qué se puede deducir de la siguiente línea? (una o varias)

# No es necesario un import porque no se trata de un paquete.
A) Que antes de dicha línea hace falta poner import a.b.c

# A es un objeto con un atributo b, que a su vez tiene un atributo c, que tiene una funcion f().
#Entonces a la hora de llamar a la funcion f(), esta llama al metodo c que es atributo de B y a su vez atributo de A
B) Que f() se define en un subpaquete c de un subpaquete b de un
paquete a

C) Que antes de dicha línea hace falta poner from a.b.c import f

# La linea funcion correctamente
D) La línea es incorrecta

# La funcion que se esta invocando se llama f(). Por justamente lo que dice la respusta B
E) El nombre de la función que se está invocando se llama a.b.c.f()
'''

###############################################

lst = [x+1 for i in range(5) if x < 3]
lst = list(map(lambda x: x**1 **2, lst))
print(lst)
###############################################

def mi_funcion(x):
    if x <=0:
        print('*', end = '')
    elif x >=2:
        print('*' * 2, end = '')
    else:
        print('*' * 1, end = '')

for i in range(1:4):
    mi_funcion(i)

###############################################

x = ' Maria'
y = 'maria'

if x == y:
    print('IGUAL')
elif x < y:
    print('MENOR')
else:
    print('MAYOR')

###############################################
# ¿Cuántos asteriscos se van a mostrar por pantalla al ejecutar el siguiente código? (1 opción)

def o (p):
    def q(a):
        return '*' + '*' + p 
    return q 

r = o(2)
s = o(3)

try:
    print(r(2), end='')
except:
    pass 
else:
    print('*', end= '')


try:
    print(s(), end='')
except:
    pass
else:
    print('*',end='')

############################################

class I:

    def __init__(self):
        self.s = 'abc'
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == len(self.s):
            raise StopInteraction
        v = self.s[self.i]
        self.i += 1
        return v 

for x in I():
    print(x, end='')

###########################################







