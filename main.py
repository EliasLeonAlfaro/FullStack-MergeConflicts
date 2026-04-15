def procesar_nombres(lista_nombres):
    """
    Recibe una lista de nombres y debe devolver una lista 
    con los nombres limpios (sin espacios extra) y en formato correcto.
    """
    return [n.strip().capitalize() for n in lista_nombres if n.strip()]

if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    resultado = procesar_nombres(nombres_sucios)
    print(f"Resultado final: {resultado}")
