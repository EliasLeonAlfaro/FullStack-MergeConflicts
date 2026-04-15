def procesar_nombre(entrada):
    # 1. Limpieza: Quitar espacios laterales
    nombre_limpio = entrada.strip()
    
    # 3. Seguridad: Ignorar si queda vacío
    if not nombre_limpio:
        return None  # O puedes lanzar un error o retornar un mensaje
    
    # 2. Normalización: Formato "Nombre"
    nombre_normalizado = nombre_limpio.capitalize()
    
    return nombre_normalizado

# Ejemplos de uso:
entradas = ["  elias  ", "   ", "JOAQUIN", "  JOAlias  "]

for e in entradas:
    resultado = procesar_nombre(e)
    if resultado:
        print(f"Procesado: '{resultado}'")
    else:
        print("Entrada ignorada por estar vacía.")