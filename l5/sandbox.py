class Library():
    
    num_totales = 0
    
    # Para guardar todos los ejemplares por codigo
    db_all = []
    
    
    # Aqui contobilizo los ejemplares prestados
    num_prestados = 0
        
    def __init__(self, codigo, titulo, ID, type):
        
        # Inicializo estas variables para poder utilizarlas en los metodos de library
        self.codigo = codigo
        self.titulo = titulo
        self.id = ID
        self.type = type
        
        #Inicializo como no prestado
        self.is_borrowed = 'NO PRESTADO'

        # Guardo las variables dentro de la variable de clase, aqui estan todos los recursos disponibles
        self.mi_objeto = {'Type':type, 'Id': ID,'title': titulo, 'Code' :codigo,  'Borrowed': self.is_borrowed}
        
        # Aljunto el nuevo objeto a mi lista de diccionarios
        Library.db_all.append(self.mi_objeto)

        # Inicializo el contador de total ejemplares
        Library.num_totales += 1
        
          
    def prestar(self):
        
        for dict in Library.db_all:
            
            for key, value in dict.items():
                
                if key == 'Code' and value == self.codigo:
                    
                    dict['Borrowed'] = 'PRESTADO'
                    
                    # Sumo al contador de recursos prestados
                    Library.num_prestados +=1
                    
                    # Aqui acutalizo el objeto self con el nuevo valor
                    self.is_borrowed = dict['Borrowed']
                    
                    # Imprimo codigo y estado por pantalla
                    print (value, dict['Borrowed'] )
        
        

    def devolver(self):
        
        for dict in Library.db_all:
            
            for key, value in dict.items():
                
                if key == 'Code' and value == self.codigo:
                    
                    dict['Borrowed'] = 'NO PRESTADO'
                    
                    # Resto al contador de recursos prestados
                    Library.num_prestados -=1   
                    
                    # Aqui acutalizo el objeto self con el nuevo valor
                    self.is_borrowed = dict['Borrowed']
                    
                    # Imprimo codigo y estado por pantalla
                    print (value, dict['Borrowed'] )
                    
                                 
class Libro(Library):
    
    
    num_libros_totales= 0
    
    
    # La clase se inicializa con tres parametros
    def __init__(self, code, title, isbn):
        
        # Me ayuda a inicializar el constructor de la clase padre. ------------------------------> OJO
        # Le paso el peso para que pueda inicializar el constructor de arriba
        # Esta forma no necsito SELF --------------------------------------------------------------OJO
        super().__init__(code, title, isbn, 'book')
    

        # -----------Variable de clase(contador)--------------
        
        # Este contador  ya no es parte del objeto self.
        # Lo llamo directo con el nombre de la clase
        Libro.num_libros_totales += 1
        
              
    # Creo un objeto string para devolver la representacion del objeto en forma de cadena de texto
    def __str__(self):
        
        # Llamo las variables de mi clase padre pues ya las inicialice con los valores que recibi por parametro
        # Si no tengo que repetir variables en cada clase y obtengo los valores directamente de la clase padre.
        return f"{self.codigo } - {self.titulo} - {self.is_borrowed} ({self.id})"    
        
        
class Revista(Library):
    
    
    num_revistas_totales= 0
    
    # La clase se inicializa con tres parametros
    def __init__(self, code, title, number):
        
        # Me ayuda a inicializar el constructor de la clase padre. ------------------------------> OJO
        # Le paso el peso para que pueda inicializar el constructor de arriba
        # De est manera simepre tengo que incluir el SELF
        Library.__init__(self, code, title, number, 'revista')
        
        # -----------Variable de clase(Contador)--------------
        
        # Este contador  ya no es parte del objeto self.
        # Lo llamo directo con el nombre de la clase
        Revista.num_revistas_totales += 1
        
              
    # Creo un objeto string para devolver la representacion del objeto en forma de cadena de texto
    def __str__(self):
        
        # Llamo las variables de mi clase padre pues ya las inicialice con los valores que recibi por parametro
        # Si no tengo que repetir variables en cada clase y obtengo los datos directamtne de la clase padre.
        return f"{self.codigo } - {self.titulo} - {self.is_borrowed}({self.id})"     


try:
    libro1 = Libro('L1_123', "La bestia", '78479482739472')
    # Accedo a los variables de instancia y los metodos de la clase directamente desde el print.
    print('Mi primer libro es:', libro1)
    print('Numero ejemplares totales:', libro1.num_totales)
    print('Numero libros totales:', libro1.num_libros_totales)
    print('Numero ejemplaresprestados:', libro1.num_prestados,'\n')



    libro2 = Libro('L2_456', "Ultimos dias en Berlin", '78479482739472')
    # Accedo a los variables de instancia y los metodos de la clase directamente desde el print.
    print('Mi primer libro es:', libro2)
    print('Numero de ejemplares totales:', libro1.num_totales)
    print('Numero libros totales:', libro2.num_totales)
    print('Numero ejemplaresprestados:', libro1.num_prestados,'\n')



    revista1 = Revista('R1_HJKH', "National Geografic", '5')
    print('Mi primera revista es:', revista1)
    print('Numero de ejemplares totales:', revista1.num_totales)
    print('Numero de revistas totales:', revista1.num_revistas_totales)
    print('Numero ejemplares prestados:', revista1.num_prestados, '\n')


    revista2 = Revista('R2_UOUI', "National Geografic", '23')
    print('Mi primera revista es:', revista2)
    print('Numero de ejemplares totales:', revista2.num_totales)
    print('Numero de revistas totales:', revista2.num_revistas_totales)
    print('Numero ejemplares prestados:', revista2.num_prestados, '\n')

    revista1.prestar()
    libro1.prestar()

    print('Numero ejemplares prestados:', libro1.num_prestados)

    libro1.devolver()

    print('Numero ejemplares prestados', libro1.num_prestados,'\n')
    
    
except Exception as e:
    print(' Ha ocurrido el siguiente error genérico')