def procesar_nombres(lista_nombres):
    """
    Recibe una lista de nombres y debe devolver una lista 
    con los nombres limpios (sin espacios extra) y en formato correcto.
    """
    return [n.strip().capitalize() for n in lista_nombres if n.strip()]

if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    
    # OPCIÓN A: Crear una nueva lista filtrando los None
    # Esta es la forma más profesional de hacerlo
    resultado = [procesar_nombre(n) for n in nombres_sucios if procesar_nombre(n) is not None]
    
    print(f"Resultado final: {resultado}")
