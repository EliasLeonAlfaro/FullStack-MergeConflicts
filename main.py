def procesar_nombres(lista_nombres):
    nombres_limpios = []
    
    for nombre in lista_nombres:
        nombre_limpio = nombre.strip()
        # Seguridad: Si después de limpiar no está vacío, lo procesamos
        if nombre_limpio:
            nombres_limpios.append(nombre_limpio.capitalize())
            
    return nombres_limpios

if __name__ == "__main__":
    datos_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    resultado = procesar_nombres(datos_sucios)
    print(f"Resultado final: {resultado}")
