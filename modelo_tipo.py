def clasificar_energia(consumo, personas, es_renovable):
    if consumo < 100 and es_renovable == "Sí":
        return "Energía renovable baja demanda"
    elif consumo >= 100 and es_renovable == "Sí":
        return "Energía renovable alta demanda"
    elif consumo < 100 and es_renovable == "No":
        return "Energía no renovable baja demanda"
    else:
        return "Energía no renovable alta demanda"