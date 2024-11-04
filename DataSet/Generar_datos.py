import csv
import random

# Función para generar DNI aleatorio
def generar_dni():
    numero = random.randint(10000000, 99999999)
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra = letras_dni[numero % 23]
    return f"{numero}{letra}"

# Listas de datos ficticios ampliadas
nombres = [
    "Luis", "Carlos", "María", "Ana", "Javier", 
    "Laura", "Pedro", "Carmen", "Lucía", "Manuel", 
    "Sara", "Raúl", "Paula", "David", "Fernando", 
    "Teresa", "Rafael", "Silvia", "Cristina", "José", 
    "Cesar", "Diego", "Salim", "Iván", "Joan"
]

ciudades_personas_vivienda = {
    "Madrid": 3,
    "Barcelona": 2,
    "Valencia": 4,
    "Sevilla": 3,
    "Bilbao": 2,
    "Málaga": 5,
    "Zaragoza": 3,
    "Murcia": 4,
    "Palma": 3,
    "Las Palmas": 6,
    "Valladolid": 2,
    "Córdoba": 5,
    "Granada": 3,
    "Tenerife": 7,
    "Alicante": 4,
    "San Sebastián": 2,
    "Salamanca": 3,
    "Almería": 5,
    "Castellón": 4,
    "Oviedo": 3
}

tipos_energia_info = {
    "solar": [0.10, 1],
    "eólica": [0.08, 1],
    "hidroeléctrica": [0.06, 1],
    "nuclear": [0.12, 0],
    "carbón": [0.14, 0],
    "gas natural": [0.11, 0]
}

estaciones = {"Verano" : 0.30,
              "Invierno" : 0.70}

renovables = {
    1 : 0.6,
    0 : 0.4
}

# Crear y escribir el archivo CSV en formato UTF-8
with open(r'C:\Users\joant\Desktop\EjEnergias\DataSet\datos_consumo.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir encabezados
    writer.writerow(["id", "nombre", "consumo", "ciudad", "personas_vivienda", "precio_energia", "tipo_energia", "renovable", "estacion"])

    # Generar 5 filas de datos
    for i in range(1500):
        # GENERAR DNI
        id_dni = generar_dni()

        # NOM RANDOM DE LA LLISTA
        nombre = random.choice(nombres)

        # ESCOLLIR ESTACIO DE L'ANY (ESTIU/HIVERN)
        estacion = random.choice(list(estaciones.keys()))

        # SELECCIONAR TIPUS D'ENERGIA RANDOM
        tipo_energia = random.choice(list(tipos_energia_info.keys()))

        # DETERMINAR EL PREU DE LA ENERGIA
        precio_energia = round(tipos_energia_info[tipo_energia][0], 2)  # precio en €/kWh

        # OBTENIR SI ES RENOVABLE
        renovable = tipos_energia_info[tipo_energia][1]

        # DETERMIANR LA CIUTAT
        ciudad = random.choice(list(ciudades_personas_vivienda.keys()))

        # DETERMINAR EL NUMERO DE PERSONES PER CASA
        personas_vivienda = random.randint(max(1, ciudades_personas_vivienda[ciudad] - 2), ciudades_personas_vivienda[ciudad] + 2)

        # CALCULAR EL CONSUM A PARTIR DE LES DADES OBTINGUDES
        consumo = round(estaciones[estacion] + (personas_vivienda * precio_energia), 2)     

        # ESCRIURE CSV
        writer.writerow([id_dni, nombre, consumo, ciudad, personas_vivienda, precio_energia, tipo_energia, renovable, estacion])
