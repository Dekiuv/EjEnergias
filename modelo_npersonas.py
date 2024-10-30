def calcular_personas(consumo, precio_energia, tipo_energia, renovable, estacion):
    
    base_personas = 1
    ajuste_consumo = consumo / 50 
    ajuste_precio = precio_energia / 100 
    
    
    if renovable == "Sí":
        ajuste_renovable = 0.9
    else:
        ajuste_renovable = 1.1

    if estacion == "Invierno":
        ajuste_estacion = 1.2
    elif estacion == "Verano":
        ajuste_estacion = 1.0
    else:
        ajuste_estacion = 1.1

    # Cálculo final de personas
    estimacion_personas = base_personas + (ajuste_consumo * ajuste_precio * ajuste_renovable * ajuste_estacion)
    
    return max(1, round(estimacion_personas))