<<<<<<< HEAD
import pandas as pd 
from sklearn.preprocessing import LabelEncoder, MinMaxScaler 
from sklearn.impute import SimpleImputer 
import numpy as np  


# F1 Eliminación de valores nulos
def remove_nulls(df):
    return df.dropna()

Función 3: Normalización de datos numéricos 
def normalizar_datos(df, columnas): 
    """Normaliza columnas numéricas entre 0 y 1.""" 
    df_normalizado = df.copy() 
    scaler = MinMaxScaler() 
    df_normalizado[columnas] = scaler.fit_transform(df_normalizado[columnas]) 
    return df_normalizado

    Función 5: Imputación de valores faltantes 
def imputar_valores(df, estrategia='media'): 
    """Imputa valores faltantes con media, mediana o moda.""" 
    df_imputado = df.copy() 
    imputer = SimpleImputer(strategy=estrategia) 
    df_imputado[df.columns] = imputer.fit_transform(df_imputado) 
    return df_imputado 
=======
import pandas as pd

# F2: Codificación de variables categóricas
def encode_categorical(df):
    """
    Codifica variables categóricas usando One-Hot Encoding
    """

    # Limpiar espacios en columnas tipo texto
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Eliminar columna ID si existe
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    # Detectar columnas categóricas
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Aplicar One-Hot Encoding
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df_encoded


# 🔽 Esto es para probar el código (opcional pero recomendado)
if __name__ == "__main__":
    df = pd.read_csv("churn.csv")
    df_encoded = encode_categorical(df)
    print(df_encoded.head())
>>>>>>> luz_f2
