

class Lista:
    
    def __init__(self):
        # Inicializo las listas que voy a utilizar en el ejercicio para poder llamarlas desde todos los metodos
        self.list = list()
        self.elementos = list()
        
    def new_list(self):

        try:
            
            the_input = input('Introduzca una línea con los números separados por espacios: ')
            self.elementos = the_input.split()
            
            # Utilizo la funcion split para dividir la lista
            # Por defecto el separador es el espacio, pero se le puede definir el delimitador como parametro
            # SI no se puede pasar a float salta un value error y analizo si es la palabra stop
            self.list = [float(i) for i in self.elementos]

            print('La suma total es de: ', self.sum())
            
            print('La lista ordenada es :', self.ordenar())

        
        # INtenté aqui comenzar a jugar con la excepciones para filtrar
        except ValueError:
            # Aqui verifico si esta compuesto de solo letras o si vienen numeros
            # Me da TRUE si solo contine letras
            # Si es el caso analizamos si viene la palabra STOP con cualquier variante
            #COn cada elemento pruebo si está la palabra STOP en cualquiera de sus variantes
            
            my_list = self.check_stop()
            
            self.list = my_list
            print('La suma total es de: ', self.sum())
            print('La lista ordenada es :', self.ordenar())
            
    def check_stop(self):
        
        try:
            # Creo una lista nueva para almacenar solo los datos antes de la palabra stop
            new_list = list()
            
            for item in self.elementos:
                
                # Simplemente pasamos todo a minuscula y comparamos.
                if item.lower() == "stop":
                    break
                # Lo agrago en float solo para asegurarme que puedo utiliar la lista par asumar y ordenar.
                new_list.append(float(item))

            return new_list
        
        # En caso que se haya introducido un valor que no es el stop se le solicita la informacion de nuevo al usuario.
        # Jugamos con la exception para comenzar de nuevo
        except ValueError:
            print("Ha introducido un caracter no valido. Por favor intente de nuevo")
            Lista.new_list()

    def sum(self):
        # Utilizo el metodo sum para realizar la suma
        suma = sum(self.list)
        return suma
            
    def ordenar(self):
    
        # Utilizo el metodo sorted para ordenar los valores de mayor a menor
        ordenar = sorted(self.list, reverse=True)
        return ordenar

try:
   
   
    # Creo el objeto con la clase Client
    lista = Lista() 

    # Hago un loop para que el programa se ejecute sin interrupcion
    while True:
        
        # Inicializo el objeto y llamo al metodo new_list
        # Toda la ejecucion se realiza dentro de la clase.
        lista.new_list()

except Exception as e:
    print('El siguiente error a surigido',e)