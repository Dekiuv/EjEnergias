import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def calcular_personas(consumo: float, precio_energia: float, tipo_energia: str, renovable: int, estacion: str):
    
   # Leer los datos
    df = pd.read_csv('datos_consumo.csv')

    # Seleccionar las características relevantes y eliminar las columnas innecesarias
    df = df[['consumo', 'personas_vivienda', 'precio_energia', 'tipo_energia', 'renovable', 'estacion']]

    # Codificar variables categóricas (tipo_energia y estacion)
    df = pd.get_dummies(df, columns=['tipo_energia', 'estacion'], drop_first=False)

    # Dividir los datos en características (X) y variable objetivo (y)
    X = df.drop('personas_vivienda', axis=1)  # Variables de entrada
    #print("X",X.columns)
    y = df['personas_vivienda']               # Variable objetivo

    # Dividir el conjunto de datos en entrenamiento y prueba (80%-20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

    # Crear el modelo de regresión lineal
    model = LinearRegression()

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Crear tu nuevo dato con las mismas columnas

    nuevo_dato = {
        'consumo': [consumo],
        'precio_energia': [precio_energia],
        'tipo_energia': [tipo_energia],
        'renovable': [renovable],
        'estacion': [estacion]        
    }

    # Crear un DataFrame para el nuevo dato
    nuevo_dato_df = pd.DataFrame(nuevo_dato)
  
    nuevo_dato_df = pd.get_dummies(nuevo_dato_df, columns=['tipo_energia', 'estacion'], drop_first=False)

    columnas_esperadas = [
    'consumo', 'precio_energia', 'renovable',
    'tipo_energia_carbón', 'tipo_energia_eólica', 'tipo_energia_gas natural',
    'tipo_energia_hidroeléctrica', 'tipo_energia_nuclear', 'tipo_energia_solar',
    'estacion_Invierno', 'estacion_Verano'
    ]

    # Agrega las columnas faltantes con ceros
    for col in columnas_esperadas:
        if col not in nuevo_dato_df.columns:
            nuevo_dato_df[col] = 0

    # Reordena las columnas para que coincidan con el DataFrame de entrenamiento
    nuevo_dato_df = nuevo_dato_df[columnas_esperadas]

    # Hacer la predicción con el modelo
    prediccion = model.predict(nuevo_dato_df)

    return 1 if int(prediccion[0]) < 0 else int(prediccion[0]) 

print(calcular_personas(2.4,1.3,"eólica",1,"Invierno"))