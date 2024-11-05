import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# Cargar los datos
df = pd.read_csv('datos_consumo.csv')

# Seleccionar características relevantes incluyendo la variable objetivo
df = df[['consumo', 'personas_vivienda', 'precio_energia', 'tipo_energia', 'renovable', 'estacion']]

# Codificar variables categóricas (tipo_energia y estacion)
df = pd.get_dummies(df, columns=['tipo_energia', 'estacion'], drop_first=True)

# Separar las variables de entrada (X) y la variable objetivo (y)
X = df.drop('consumo', axis=1)  # Variables de entrada
y = df['consumo']               # Variable objetivo

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lista de modelos para evaluar
models = {
    'Decision Tree': DecisionTreeRegressor(max_depth=5, random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),
    'Support Vector Regressor': SVR(kernel='rbf', C=1.0, epsilon=0.1),
    'K-Nearest Neighbors': KNeighborsRegressor(n_neighbors=5)
}

# Evaluar cada modelo
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"{name} MSE: {mse}")
