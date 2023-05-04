# Abro el archivo como lectura
with open('fichero.txt', 'r') as file:
    # Indico que deseo leer todas las lineas, una por una
    lines = file.readlines()
    
#------- INIT Variables
# Creo una lista para guardar las notas
notes = []
# Un contador para las lineas que se han leido y no son notas validas
excluded_lines = 0


#----- LOOP FOR
# Iteractuo con cada linea dentro del objeto lineas.
for line in lines:
    # Elimino los espacios en blanco
    line = line.strip()
    
    #--- IF NOT NOTA
    # En caso de que no sea una linea la excluyo
    if not line:
        # Le sumo uno al contador de lineas excluidas
        excluded_lines += 1
        
        # COntinuo para seguir con la siguiente linea cuando llegue
        continue
    
    try:
        # Intento convertir la linea a un float, asi descubro si es un numero
        note = float(line)
        
        # SI efectivamente lo es lo guardo en la lista de notas
        notes.append(note)
    
    # Utilizo la exception para sumar al contador de lineas excliudas en caso de que de error
    except ValueError:
        excluded_lines += 1
        
        # No se rompe en programa sino que sigue con la siguiente linea.
        continue

# Utilizando el metodo Sort() filtro de menor a mayor los valores de la lista
notes.sort()

print(f'Las notas leidas son:{notes}')


sobresaliente = [note for note in notes if note >= 9.0]
print(f'Notas con sobresaliente:{sobresaliente}')

print(f'Numero de lineas excluidas: {excluded_lines}')

