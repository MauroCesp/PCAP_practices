print('abc'+'xy'*2+'a'*3)
# C---------> abcxyxyaaa
# El orden de prioridad de las operaciones define el resultado
# Primero se ejecutan las mutiplicaciones y despues las sumas

salida = '-'

for ch in 'ZYX':
    salida = salida +chr(ord(ch)-1)*2

print(salida)

print(ord('Z'))
print(ord('Y'))
print(ord('X'))

# B----------------> -YYXXWW

#Z = 90
#Y = 89
#X = 88

# (90-1 = 89)*2

# (89-1 = 88)*2 

# (88-1 = 87)*2


# Por eso es que aparce la W en logar de la X
# SOlo tienen un guion porque en la segunda vuelta ya viene con el valor de la primera vuelta.

a = '2.1'

b= float(a)
c = int(b)
#d = int(a)
d = int(b)
idc = id(c)
idd = id(d)

print(idc)
print(idd)


# D ---------> El programa dar{a un error}

# Al intentar asignar el valor de A a D
# El formato con punto hace referencia a un flotante
# NO se puede tratar de pasar de cadena a entero con una cadena que hace referencia a un decimal.
# Python lo lee como un error


milista = ['aa','AA','a']

milista1 = milista[:]
milista.sort()

print(milista)
print(milista1)

for i in milista:
    print(i, end='-')
    
for i in milista1:
    print(i, end='-')

print(' ')
    
# B --------------------------> AA-a-aa-aa-AA-a-
# Aqui es importante recordar que las letras mayusculas tienen un numero mas bajo que las minusculas
# Entonces el programa lee que AA es el mero de todos y ordena la lista AA-a-aa
# La primera lista se adjunta a la segunda que mantienen el orden original.

mi_lista = [[i if j > 1 else -1 for i in range(4)] for j in range(0,4) if j %2 == 0]

print(mi_lista)

myList = list()

myList1 = list()

for i in range(4):
    if i %2 == 0:
        myList.append(i)
        
print(myList)

# B ----------------------> [[-1, -1, -1, -1], [0, 1, 2, 3]]
# Primero se ejecuta el FOR de abajo (0,4)
# Como pide que que sea numeros pares solo quedan dos numeros = 0,2

# COn estos dos numeros ejecuto el loop de arria  range(0)
# Va a comprobar 4 veces cada resultado de j
# Revisa cuatro veces que 0 > 1 , guarda el 1 cuatro veces en la primera vuelta de i
# En la segunda vuelta 2 > 1 , guarda lso resultados en una segunda lista.
# Como el resultado es TRUE guarda el valor de la posicion de i (0,1,2,3)

print(ord('z')-ord('y'))




for i in range(-1,4):
    
    print('---'*10)
    print(i)
    
mi = [i*5 if i > -1 else 0 for i in range(-1,4)]
    
print('MADRID'> 'madrid')