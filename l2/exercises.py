'''
x = 3 

def fun(x):
    x = x + 3 *2
    return x
print(fun(x+3),x,sep='')
'''



## El resultado de la funcion es 12.
## EN el print, se adjunta el valor inicial de x con el resultado de la funcion x,por medio de la separacion ""


# Va a dar error porque esta esperando dos parametros de entrada, y solo se esta asignando uno

'''
def fun(x,y):
    return x** 3 ** y
print(fun(2))
'''

# La primera funcion recibe el parametro x=2
# Regresa x =0, y reemplaza la variabel global x
#La segunda funcion no importa lo que reciba va a regresar 3
# Al imprimir el valor global de x, el resultado es x=0

#---------------------------------------------

def fun(x,y=4,z=6):
    return x+y/z
print(fun(20,z=2))

## la variable z, entra como 2.
# Primero se debe de realizar la division y despues la suma
# El resultado de la funcion es float por defecto a menos que se indique que es otro tipo de variable
