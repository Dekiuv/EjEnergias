import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Leer los datos
df = pd.read_csv('datos_consumo.csv')

# Seleccionar las características relevantes y eliminar las columnas innecesarias
df = df[['consumo', 'personas_vivienda', 'precio_energia', 'tipo_energia', 'renovable', 'estacion']]

# Codificar variables categóricas (tipo_energia y estacion)
df = pd.get_dummies(df, columns=['tipo_energia', 'estacion'], drop_first=True)

# Dividir los datos en características (X) y variable objetivo (y)
X = df.drop('consumo', axis=1)  # Variables de entrada
y = df['consumo']               # Variable objetivo

# Dividir el conjunto de datos en entrenamiento y prueba (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el error cuadrático medio (MSE) para evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio (MSE): {mse}")

# Mostrar los coeficientes del modelo
print("Coeficientes del modelo:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")
