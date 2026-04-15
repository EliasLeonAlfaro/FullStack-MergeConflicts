def procesar_nombres(lista_nombres):
    nombres_limpios = []
    
    for nombre in lista_nombres:
  
        nombre_limpio = nombre.strip()
        
        if nombre_limpio: 

            nombres_limpios.append(nombre_limpio.capitalize())
            
    return nombres_limpios

# Ejemplo de uso:
if __name__ == "__main__":
    datos_sucios = ["  juan", "MARÍA  ", "   ", " lUis ", ""]
    resultado = procesar_nombres(datos_sucios)
    print(f"Resultado: {resultado}")
    # Salida esperada: ['Juan', 'María', 'Luis']