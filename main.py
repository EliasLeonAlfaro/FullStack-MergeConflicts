def procesar_nombre(entrada):
    # 1. Limpieza: Quitar espacios laterales
    nombre_limpio = entrada.strip()
    
    # 3. Seguridad: Ignorar si queda vacío
    if not nombre_limpio:
        return None  # O puedes lanzar un error o retornar un mensaje
    
    # 2. Normalización: Formato "Nombre"
    nombre_normalizado = nombre_limpio.capitalize()
    
    return nombre_normalizado

if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    resultado = procesar_nombres(nombres_sucios)
    print(f"Resultado final: {resultado}")
