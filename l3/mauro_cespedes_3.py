
class Client:
    
    def __init__(self):
              
        self.clients = dict()
        
        
    def check_if_exists(self,dni):
        
        try:
            # --------------- x -----------------
            if self.clients == None:      
                return None
                
            elif self.clients !=None:
                
                for key, value in self.clients.items():
                    if dni == key:
                        return value
            else:
                pass
               
        except Exception as e:
            print ('Ha surgido un error:'+e)
        
   
    def new_cust(self,name,purchase,dni):

        try:
            # Creo el diccionario con los campos
            new_client = {'Nombre': [], 'DNI':[], 'Compras': [], 'Puntos':[]}
            
            # Se calcula el total de puntos a agregar
            add_points = self.add_points(purchase)
            
            
            new_client['Nombre'].append(name)
            new_client['DNI'].append(dni)
            new_client['Compras'].append(purchase)
            new_client['Puntos'].append(add_points)

            # COmo es un cliente nuevo se guarda la informacion 
            # Utilizo self para llamar a otro metodo en esta misma clase.
            # Paso como parametro el objeto
            self.save_new_cust(new_client,dni)
            
            # Regreso el objeto para mostrar en pantalla
            return new_client
    
        except Exception as e:
            print ('Ha surgido un error:'+e)
            
            
    def add_points(self,purchase):     
        
        points = list()
        
        counter = int(purchase)
        
        while counter > 0:
            var = int(5)
            if (counter - 6) >= 0:    
                points.append(var)
                # Resto para poder salir del bucle            
                counter -= 6
            else:
                # Esto lo hago para poder salir del bucle
                counter = 0
        
        # Hago la sumatoria de la lista de puntos acumulados por la compra
        suma_puntos = sum(points)
                 
        return suma_puntos
      
        
    def save_new_cust(self, new_client,dni):    
        
        # Esto es un dict de dicts a amenra de base de datos
        # Utilizo el DNI como clave y el valor es otro diccionario con la info del cliente
        self.clients[dni] = new_client

                    
    def update_acct(self, points, dni, purchase):
        
        for key , value in self.clients.items():
            
            if key == dni:
                for k , v in value.items():
                    
                    if k == 'Compras':
                        v.append(purchase)
                        
                    if k == 'Puntos':
                        v.append(points)
                    
                    
    def clean(self, dni,compras,name):
        # Limpio el string porque salio un poco sucio
                
        to_skip = str(["'"])
                
        # Hago un loop sobre este string para eliminar si existen  , y dejar un string entero       
        for char in to_skip:
            name = name.replace(char, '')
            dni = dni.replace(char,'')
            compras = compras.replace(char,'')
            compras = compras.replace(',','-')
        
        return dni, compras ,name

try:
   
   
    # Creo el objeto con la clase Client
    client = Client() 

    while True:
        
        print('')
        dni = input('Introduzca el DNI del cliente: ')
        
        # Verfico si lo que introdujo el ususario es un numero
        if dni.isdigit():
            # Verifico si el numero que ingreso es un 0
             if int(dni) == 0:          
                break 
             else:
                 continue  
        
        else:
            
            # Utilizo la funcion check para ver si el cliente esta registrado
            exists = client.check_if_exists(dni)
                
            if exists == None:
                
                name = input('Nombre del cliente: ')
                total = input('Total de compra: ')
                
                # Se crea el nuevo cliente con el metodo new_cust
                cliente_nuevo = client.new_cust(name, total,dni)
                # Esto arroja un diccionario  
                
                sum_points = 0
                dni1= ''
                compras = list()
                
                # Recorro el diccionario que recuperó del metodo anterior para sacar los valroes de impresion
                for key, value in cliente_nuevo.items():
                    
                    # Busco la llave que deseo trabajar.
                    if key == 'Puntos':                    
                        sum_points = sum(value)
                        
                    if key== 'DNI':
                        dni1 = str(value)
                        
                    if key == 'Nombre':
                        name = str(value)
                    
                    if key == 'Compras':
                        compras = str(value)

                
                # Utilizo una fucnion para limpiar el resultado de los caracters de más
                primero, segundo, tercero = client.clean(dni1, compras, name)    
            

                print(' EL cliente {} ({}) tiene acumulados {} puntos.'.format(tercero, primero, sum_points))   
                
                print('Sus compras son: {} €'.format(segundo)) 
                
                print('-'*10)
            
            # Exists contiene el objeto del ususario encontrado 
            elif exists:
                
                total = input('Total de compra: ')
                                    
                points = client.add_points(total)
                
                # Actualiza los campos de cada diccionario 
                client.update_acct(points, dni, total)
                
                
                sum_points = 0
                dni1= ''
                compras = list()
                    
                # Recorro el diccionario con clave -valor para tener acceso a todo          
                for key, value in exists.items():                            
                    # Busco la llave que deseo trabajar.
                    if key == 'Puntos':                    
                        sum_points = sum(value)
                        
                    if key== 'DNI':
                        dni1 = str(value)
                        
                    if key == 'Nombre':
                        name = str(value)
                    
                    if key == 'Compras':
                        compras = str(value)
                        
                # Utilizo una fucnion para limpiar el resultado de los caracters de más
                primero, segundo, tercero = client.clean(dni1, compras, name)    
            

                print(' EL cliente {} ({}) tiene acumulados {} puntos.'.format(tercero, primero, sum_points))   
                
                print('Sus compras son: {} €'.format(segundo)) 
                
                print('-'*10)
            else:
                print('-----------------------')
        

except Exception as e:
    print('El siguiente error a surigido',e)