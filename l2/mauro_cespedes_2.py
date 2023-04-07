
class Math:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def irpf(self):
        
        try:
            # --------------- x -----------------
            if self.x  >=0 and  self.x  <12450.00:      
                a = (self.x /100)*19.00
                
            elif self.x >= 12450.00 and self.x  < 20200.00:
                a = (self.x /100)*24.00
                
            elif self.x  >= 20200.00 and self.x  < 28000.00:
                a = (self.x /100)*30.00

            elif self.x  >= 28000.00 and self.x  < 35200.00:
                a = (self.x /100)*30.30

            elif self.x  >= 35200.00 and self.x  < 50000.00:
                a = (self.x /100)*37.10
                
            else:
                a = (self.x /100)*37.20
            #---------------- Y -------------------    
            if self.y  >=0 and  self.y  <12450.00:      
                b = (self.y /100)*19.00
                
            elif self.y >= 12450.00 and self.y  < 20200.00:
                b = (self.y /100)*24.00
                
            elif self.y  >= 20200.00 and self.y  < 28000.00:
                b = (self.y /100)*30.00

            elif self.y  >= 28000.00 and self.y  < 35200.00:
                b = (self.y /100)*30.30

            elif self.y  >= 35200.00 and self.y  < 50000.00:
                b = (self.y /100)*37.10
                
            else:
                b = (self.y /100)*37.20
            
            return a,b
        
        except Exception as e:
            print ('Ha surgido un error:'+e)
   
    def neto(self, a, b):
       
       obj1 = self.x - a
       obj2 = self.y - b
    
       return obj1 , obj2 

try:
    
    
    var = True 
    while var == True:
        
        x = float(input('Ingrese el PRIMER salario bruto: '))
        
        if x < 0:
            print(' Debe de introducir un salario mayor o igual a 0 euros')
            
        else:  
            
            vary = True
            while vary ==  True:                     
                y = float(input('Ingrese el SEGUNDO salario bruto: '))
            
                if y < 0:
                    print(' Debe de introducir un salario mayor o igual a 0 euros')
                else:
                    break
            break


    
    objeto = Math(x,y)

    a, b = objeto.irpf()
    
    sa1, sa2 = objeto.neto(a,b)

    print('******', end='\n')  
    print('El salario bruto anual de la pareja es: '+str(x+y))
    print('El salario neto anual de la pareja es: '+str(sa1+sa2))
    print()
    print('******')
except Exception as e:
    print(e)