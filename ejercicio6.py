import math 

def calcular_media_basico(lista):
    if not lista:
        return 0.0
    return sum(lista) / len(lista)

def calcular_desviacion_estandar_basico(lista, media):
    n = len(lista)
    if n < 2:
         
         return 0.0
    
    suma_cuadrados = 0
   
    for x in lista:
      
        suma_cuadrados += (x - media) ** 2
        
    varianza = suma_cuadrados / n 
    
    return math.sqrt(varianza)

def calcular_norma_vector_basico(lista):
    suma_cuadrados = 0
    for x in lista:
        suma_cuadrados += x ** 2
        
    return math.sqrt(suma_cuadrados)

def normalizar(lista, modo):
    if not lista:
        return []
    
    if modo != "minmax" and modo != "zscore" and modo != "unit":
        print(f"Error: Modo de normalización '{modo}' no es válido.")
        return []
    
    lista_normalizada = []

    if modo == "minmax":
        min_val = min(lista)
        max_val = max(lista)
        rango = max_val - min_val
        
        if rango == 0:
            return [0.0] * len(lista)
            
        for x in lista:
            lista_normalizada.append((x - min_val) / rango)
        return lista_normalizada

    elif modo == "zscore":
        media = calcular_media_basico(lista)
        desviacion = calcular_desviacion_estandar_basico(lista, media)
        
        if desviacion == 0.0:
            return [0.0] * len(lista)

        for x in lista:
            lista_normalizada.append((x - media) / desviacion)
        return lista_normalizada

    elif modo == "unit":
        norma = calcular_norma_vector_basico(lista)
        
        if norma == 0.0:
            return [0.0] * len(lista)
            
        for x in lista:
            lista_normalizada.append(x / norma)
        return lista_normalizada

if __name__ == "__main__":
    valores = [10, 20, 30]
    
    print("   ")
    print(f" Original: {valores}")

    print(f" [minmax]: {normalizar(valores, 'minmax')}") 
    print(f" [zscore]: {normalizar(valores, 'zscore')}") 
    print(f" [unit]:   {normalizar(valores, 'unit')}")