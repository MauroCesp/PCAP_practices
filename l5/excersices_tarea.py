# La respuesta correcta es la C ----------------> 2 3 4 2 y dará un error
class ClaseA:
    
    A = 1
    
    def __init__(self, a):
        
        self.a = a
class ClaseB(ClaseA):
    
    B = 2
    
    def __init__(self, a , b):
        ClaseA.A = a
        ClaseB.B = b

o1 = ClaseA(3)
o2 = ClaseB(2,4)

# El primero pensamiento es decir que A es igual a 1 porque es lo que obtuve del primer objeto
# Pero no hay que olvidar que cuando se creo el segundo objeto se modifico el valor y se sobreescribio por un 2
# Hay que tener mucho cuidado con esos detalles
# POr lo demas el ejercicio simple
print(o1.A, end=" ")
print(o1.a, end=" ")
print(o2.B, end=" ")
print(o2.A, end=" ")

# EL truco aqui es que "a" es una vairable de instancia
# SOlo cunado se suscribe ese objeto se puede accedera a ella.

# Lo cmmento para que no de error
#print(o2.a, end=" ")

###############################################################3


# Las respuestas correntas son:
        # C ------------> Si ejecuto print(o1.a, o1.b, o1.c) devolverá un error 
        
        # F ------------> Si ejecuto print(o1.a, o1.b) devolverá un error 
                    # Aqui lo que hay que tomar en cuenta es que cuando se crea un objeto nuevo se inicializa self.a ---->   Pero NO self.b hasta que se ejecute el metodo
                    # Entonces si no llamo a la funcion dará un error cuando intento llamar la variable.     
                    
        # H ------------ > Si ejecuto print(o2.a, o2.b, o2.c) devolverá un error
                    # Hay que recordar que este valor (C) es inicializado en el objeto o1, no funciona con el objeto o2
                    
        # I -------------> Si ejecuto print(o2.a, o2.b) mostrará 15, 20
                    # Porque al ejecutar el metodo1 se inicializa el valor de c
class A:
    
    # Aqui lo que hay que tomar en cuenta es que cuando se crea un objeto nuevo se inicializa self.a ---->   Pero NO self.b hasta que se ejecute el metodo
    # Entonces si no llamo a la funcion dará un error cuando intento llamar la variable.
    def __init__(self):
        self.a = 10
    
    def metodo1(self):
        self.b = 20


o1 = A()

# Hay que recordar que este valor es inicializado en el objeto o1, no funciona con el objeto o2
o1.c = 30
o2 = A()
o2.a = 15
o2.metodo1()

print(o2.a, o2.b)

###############################################################
'''
Si se define una superclase llamada A y una subclase llamaB, cuál o cuáles de
los siguientes fragmentos de código debería sustituir al comentario para que
cualquier objeto de clase B tuviese el atributo ‘a’ (una o varias opciones)
'''

# Las respuestas correctas son:

# B ------------------_>  A.__init__(self)
# D------------------__>  super.__init__()

# Existen dos maneras de declarar una super clase
# Dentro de la clase que hereda
        # La diferencia con la clase anterior tengo que Llamar directamente el nombre de la clase
        # Y tambien tengo que llamar SELF ------------------------------------------------------------> OJO
        # Magdalena.__init__(self)
        
        # Me ayuda a inicializar el constructor de la clase padre. ------------------------------> OJO
        # NO tengo que pasarle SELF solo los parametros que deseo inicializar.
        #super().__init__(peso)
        
class A:
    
    A = 1
    
    def __init__(self):
        
        self.a = 1
        
class B(A):
    
    def __init__(self):
        
        super().__init__()
        
        self.b = 2

obj  = B()

print(obj.a)

###############################################################


# La respuesta correcta es:  C  ------------> True c

# issubclass(class, classinfo)
# True if class is subclass of a class, or any element of the tuple
# Aqui hay que entender la pregunta y para ello se tiene que tener claro d nde va cada elemento
# La pregunta comienza ----> Es D una subclase de C
# Como D hereda de C entonces si es una subclase.
# Tambiene s importante recordar el orden de herencia.
# Primero busca dentro de la misma clase y despues en las clases padres comenzando de izquierda a derecha


class A:
    
    def metodo(self):
        
        print('a')
        
class B:
    
    def metodo(self):
        
        print('b')
 
class C(B):
    
    def metodo(self):
        
        print('c')
        
class D(C,A):
    
    pass

obj  = D()

print(issubclass(D,C), ' ', end='')

obj.metodo()