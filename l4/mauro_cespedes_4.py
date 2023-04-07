

class Lista:
    
    def __init__(self):
              
        self.list = list()
        
    def get_userinfo():
        my_str= input('Introduzca una linea con los números separados por espacios: ')
        return my_str

    #@functools.lru_cache(maxsize = None)           
    def new_list(self):

        try:
            
            my_str= Lista.get_userinfo()
            
            # Utilizo la funcion split para dividir la lista
            # Por defecto es el espacio pero se le puede definir el delimitador como parametro
            my_list = my_str.split()
            
            new_lista = list()
            
            
            # TEngo que identificar si viene la palabra STOP en cualquiera de sus variables 
            for i in my_list:
                
                # Aqui verifico si esta compuesto de solo letras o si vienen numeros
                # Me da TRUE si solo contine letras
                # Si es el caso analizamos si vienen la palabra STOP con cualquie r variante
                if i.isalpha():
                    my_list.clear()
                    print('Vuelta ',i)
                    
                    resp = Lista.check_stop(i)
                    
                    print('Esta es la respuesta de la funcion check_stop'+ str(resp))

                    # SI la palabra coincide con alguna de las combinaciones
                    if str(resp) == 'True':  
                             
                        print(' Resultado de verificar si la cadena está entre las opciones: TRUE')                                        
                        return new_lista  
                    else:
                        print(' Ingreso una cadena invalida. Intente nuevamente')   
                        
                        Lista.new_list(self)
                          
                        break

                    break
      
                else:
                    new_lista.append(i)
            
            print('Esta es la lista nueva dentro de New_list',new_lista)
            
            # new_lista = [i if i.isalpha()[if Lista.check_stop(i) == True] else i for i in my_list]

            return new_lista
        
        except Exception as e:
            print ('Ha surgido un error:'+e)     
            
    def check_stop(cadena):
        
        
        print('Esta es la cadena que recibo en el check_stop')
        print(cadena)
        
        
        
        word = 'stop'
        
        dict_options = list()
        
        for i in range (len(word)):
            
            x = word.replace(word[i:], word[i:].upper())
            dict_options.append(x) 

        for j in range (len(word)):
            
            x1 = word.replace(word[:j], word[:j].upper())

            dict_options.append(x1) 
        
        
        print(dict_options)
        
        # Ahora verifco si la cadena esta en la lista que acbo de generar.
        if cadena in dict_options:                         
            return True               
        else:
            return False

    def sum(new_lista):
        
        try:
            int_list = [int(i) for i in new_lista]    
    
            suma = sum(int_list)
            
            return suma
        
        except Exception as e:    
            print(e)
        
    def ordenar(new_lista):
        
        print(new_lista)

try:
   
   
    # Creo el objeto con la clase Client
    lista = Lista() 
    
    

    while True:
        lista_nueva = lista.new_list()

        try:
            print('*'*10)
            print('Lista nueva final: ', lista_nueva)
            #suma = lista.sum(lista_nueva)
            
            #ordenada = lista.ordenar(lista_nueva)
            
            #print('La suma total es: {}'.format(suma))
            
            #print('La lista ordenada es: {}'.format(ordenada))

        except Exception as e:
            
            print('Alguno de los caracteres ingresados no son números')
            print('Por vafor ingrese la lista nuevamente')
            continue
                  

except Exception as e:
    print('El siguiente error a surigido',e)