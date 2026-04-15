def procesar_nombre(entrada):
    # 1. Limpieza
    nombre_limpio = entrada.strip()
    
    # 3. Seguridad: Si después de strip() está vacío, retornamos None
    if not nombre_limpio:
        return None
    
    # 2. Normalización
    return nombre_limpio.capitalize()

if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    
    # OPCIÓN A: Crear una nueva lista filtrando los None
    # Esta es la forma más profesional de hacerlo
    resultado = [procesar_nombre(n) for n in nombres_sucios if procesar_nombre(n) is not None]
    
    print(f"Resultado final: {resultado}")
