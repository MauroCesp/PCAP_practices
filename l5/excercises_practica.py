
# La función incorporada hasattr() toma como argumentos un objeto y el nombre de un atributo y retorna True si el objeto contiene dicho atributo.
class A:
    a= 1

# Aqui el error est{a en que para que reconozca el atributo  tiene que  ir como cadena de texto
# Si se declara como variable tiene que estar ya configurado con el SELF del metodo init
#print(hasattr(A,a))


class A:
    x = 0
    def __init__(self, v=0):
        self.y = v
        A.x += v

a = A()
b = A(1)
c =A(2)

# Aqui el truco esta en que no hay que pensar como si estuvieramos haciendo un bucle FOR
# Si el ultimo objeto deja X como 3 entonces cuando llamamos el atributo en los tres objetos nosva a dar 3 en todos ---------- OJO
print(a.x, b.x, c.x)



class A:
    
    def __init__(self, v):
        self.__a = v +1

# Los argumentos privados no pueden ser mostrados desde afuera
# Existe una manero pero no se utiliza
a = A(0)
#print(a.__a)

class A:
    pass
class B(A):
    pass

# issubclass(class, classinfo)
# True if class is subclass of a class, or any element of the tuple
# Aqui hay que entender la pregunta y para ello se tiene que tener claro d nde va cada elemento
# La pregunta es: Es A una suclase de B
# Pero en realidad cuando B tiene a A como parametro significa que B es una sub clase de A
print(issubclass(A,B))



# En este es necesario seguir el orden de los argumentos para la subclase.
# Primero busca en si misma 
# Despues busca en la primera clase padre que tenga como argumento
class A:
    def a (self):
        print('a')
class B:
    def a (self):
        print('b')
        
class C(B,A):
    def c(self):
        self.a()
        
o = C()
o.c()
        

class A:
    
    b = 3
    
    def __init__(self, x, y=1):
        self.a = x+y
        A.b = self.a
        
o1 = A(1)
o2 =A(1,2)

print(o1.a,o1.b, o2.a, o2.b)