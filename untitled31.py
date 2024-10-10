import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import ipywidgets as widgets
from IPython.display import display

# Cargar datos
df = pd.read_csv('perros_y_gatos.csv')

# Definir características y etiquetas
X = df.drop('Especies', axis=1)
y = df['Especies']

# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un pipeline que incluya el preprocesamiento y el clasificador
categorical_features = X.select_dtypes(include=['object']).columns
numeric_features = X.select_dtypes(exclude=['object']).columns

# Crear el transformador
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)  # Ignorar categorías desconocidas
    ])

# Crear el modelo con el pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', KNeighborsClassifier(n_neighbors=3))
])

# Entrenar el modelo
model.fit(X_train, y_train)

# Función para clasificar animales
def clasificador_animal(Comportamiento, Entrenamiento, Ejercicio, Comunicacion, Habilidades,
                        Cuidado, Tamaño, Cabeza, Vision, Pelaje, Orejas, Cola, Mandibula, Movimiento):
    try:
        # Construir un DataFrame con las características para la predicción
        caracteristicas = pd.DataFrame({
            'Comportamiento': [Comportamiento],
            'Entrenamiento': [Entrenamiento],
            'Ejercicio': [Ejercicio],
            'Comunicacion': [Comunicacion],
            'Habilidades': [Habilidades],
            'Cuidado': [Cuidado],
            'Tamaño': [Tamaño],
            'Cabeza': [Cabeza],
            'Vision': [Vision],
            'Pelaje': [Pelaje],
            'Orejas': [Orejas],
            'Cola': [Cola],
            'Mandibula': [Mandibula],
            'Movimiento': [Movimiento]
        })

        # Realizar la predicción
        prediccion = model.predict(caracteristicas)
        return prediccion[0]

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Definir los widgets para la entrada
Comportamiento = widgets.Dropdown(options=['Juguetón', 'Amistoso', 'Calmado', 'Curioso', 'Activo'], description='Comportamiento:')
Entrenamiento = widgets.Dropdown(options=["difícil", "fácil", "moderado"], description='Entrenamiento:')
Ejercicio = widgets.Dropdown(options=["Alto", "Bajo", "Moderado"], description='Ejercicio:')
Comunicacion = widgets.Dropdown(options=["Silencioso", "Vocal", "Vocal y físico"], description='Comunicación:')
Habilidades = widgets.Dropdown(options=['Inteligente y cazador', 'Rescate y perro de terapia'], description='Habilidades:')
Cuidado = widgets.Dropdown(options=["Alto", "Bajo", "Moderado"], description='Cuidado:')
Tamaño = widgets.Dropdown(options=["Grande", "Mediano", "Pequeño"], description='Tamaño:')
Cabeza = widgets.Dropdown(options=["difícil", "fácil", "moderado"], description='Cabeza:')
Vision = widgets.Dropdown(options=["Buena", "Excelente", "Muy buena"], description='Visión:')
Pelaje = widgets.Dropdown(options=["Corto y suave","Corto y denso","Largo y sedoso","Corto y áspero",
 "Largo y grueso","Sin pelaje","Largo y esponjoso","Largo y suave",
 "Corto y rizado","Largo y denso","Corto y brillante","Corto y grueso",
 "Largo y rizado","Rizado"], description='Pelaje:')
Orejas = widgets.Dropdown(options=["Caídas", "Erguidas"], description='Orejas:')
Cola = widgets.Dropdown(options=["Corta", "Larga"], description='Cola:')
Mandibula = widgets.Dropdown(options=["Fuerte", "Pequeña"], description='Mandíbula:')
Movimiento = widgets.Dropdown(options=["Ágil y alegre", "Lento"], description='Movimiento:')

# Botón para clasificar
button = widgets.Button(description="Clasificar Animal")

# Función al hacer clic en el botón
def on_button_click(b):
    try:
        prediccion_especie = clasificador_animal(Comportamiento.value, Entrenamiento.value,
                                                  Ejercicio.value, Comunicacion.value,
                                                  Habilidades.value, Cuidado.value,
                                                  Tamaño.value, Cabeza.value,
                                                  Vision.value, Pelaje.value,
                                                  Orejas.value, Cola.value,
                                                  Mandibula.value, Movimiento.value)

        print(f"El animal clasificado es: {prediccion_especie}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Asociar la función al botón
button.on_click(on_button_click)

# Mostrar widgets
display(Comportamiento, Entrenamiento, Ejercicio, Comunicacion, Habilidades,
        Cuidado, Tamaño, Cabeza, Vision, Pelaje,
        Orejas, Cola, Mandibula, Movimiento, button)

datos_de_columna_especies = df['Pelaje'].unique()
print(datos_de_columna_especies)

