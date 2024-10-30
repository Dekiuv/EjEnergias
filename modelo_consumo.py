import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def predecir_consumo(n_personas: int ,precio_energia: float, renovable:int, estacion:str):

    # Leer los datos
    df = pd.read_csv('datos_consumo.csv')

    # Seleccionar las características relevantes y eliminar las columnas innecesarias
    df = df[['consumo', 'personas_vivienda', 'precio_energia', 'tipo_energia', 'renovable', 'estacion']]

    # Codificar variables categóricas (tipo_energia y estacion)
    df = pd.get_dummies(df, columns=['tipo_energia', 'estacion'], drop_first=True)

    # Dividir los datos en características (X) y variable objetivo (y)
    X = df.drop('consumo', axis=1)  # Variables de entrada
    print("X",X.columns)
    y = df['consumo']               # Variable objetivo

    # Dividir el conjunto de datos en entrenamiento y prueba (80%-20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear el modelo de regresión lineal
    model = LinearRegression()

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Hacer predicciones en el conjunto de prueba
    # y_pred = model.predict(X_test)

    # # Calcular el error cuadrático medio (MSE) para evaluar el modelo
    # mse = mean_squared_error(y_test, y_pred)
    # print(f"Error cuadrático medio (MSE): {mse}")

    # # Mostrar los coeficientes del modelo
    # print("Coeficientes del modelo:")
    # for feature, coef in zip(X.columns, model.coef_):
    #     print(f"{feature}: {coef}")

    # Crear tu nuevo dato con las mismas columnas
    nuevo_dato = {
        'personas_vivienda': [n_personas],
        'precio_energia': [precio_energia],
        'renovable': [renovable],
        # Incluir las columnas dummy correspondientes:
        'tipo_energia_eólica': [0],
        'tipo_energia_gas natural': [1],   # Asumimos que la fuente de energía es gas natural
        'tipo_energia_hidroeléctrica': [0],

        # 'tipo_energia_carbón': [0],
        'tipo_energia_nuclear': [0],
        'tipo_energia_solar': [0],
        # 'tipo_energia_geotérmica': [0],
        # 'estacion_invierno': [0],
        'estacion_Verano': [1],             # Por ejemplo, si estás en verano
        # 'estacion_otoño': [0],
        # 'estacion_primavera': [0]
    }

    # Crear un DataFrame para el nuevo dato
    nuevo_dato_df = pd.DataFrame(nuevo_dato)

    # Verifica las columnas de nuevo_dato_df para asegurarte de que coincidan con X
    print("Columnas de nuevo_dato_df:")
    print(nuevo_dato_df.columns)

    # Hacer la predicción con el modelo
    prediccion = model.predict(nuevo_dato_df)

    print(f"Consumo predicho: {prediccion[0]}")
