import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Función para clasificar el tipo de energía
def clasificar_energia(consumo: float, renovable: int, nºperson: int, precio_energia: float):
    # Leer los datos
    df = pd.read_csv('datos_consumo.csv')

    # Seleccionar las características y variable objetivo
    df = df[['consumo', 'personas_vivienda', 'precio_energia', 'tipo_energia', 'renovable', 'estacion']]

    # Codificar la variable objetivo `tipo_energia` a valores numéricos
    label_encoder = LabelEncoder()
    df['tipo_energia'] = label_encoder.fit_transform(df['tipo_energia'])

    # Crear variables dummy para la columna `estacion`
    df = pd.get_dummies(df, columns=['estacion'], drop_first=True)
    
    # Dividir el dataset en características (X) y variable objetivo (y)
    X = df.drop('tipo_energia', axis=1)
    y = df['tipo_energia']

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear el modelo de clasificación
    model = RandomForestClassifier(random_state=42)

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Preparar el nuevo dato con las mismas características
    nuevo_dato = {
        'consumo': [consumo],
        'personas_vivienda': [nºperson],
        'precio_energia': [precio_energia],
        'renovable': [renovable]
    }
    
    # Crear un DataFrame para el nuevo dato
    nuevo_dato_df = pd.DataFrame(nuevo_dato)
    
    # Agregar las columnas dummy de `estacion` para coincidir con `X_train`
    columnas_esperadas = X.columns
    for col in columnas_esperadas:
        if col not in nuevo_dato_df.columns:
            nuevo_dato_df[col] = 0
    
    # Reordenar las columnas para que coincidan con `X_train`
    nuevo_dato_df = nuevo_dato_df[columnas_esperadas]

    # Hacer la predicción
    prediccion_codificada = model.predict(nuevo_dato_df)

    # Convertir la predicción a la categoría original de `tipo_energia`
    prediccion = label_encoder.inverse_transform(prediccion_codificada)

    return prediccion[0]