import pandas as pd 
from sklearn.preprocessing import LabelEncoder, MinMaxScaler 
from sklearn.impute import SimpleImputer 
import numpy as np  


# F1 Eliminación de valores nulos
def remove_nulls(df):
    return df.dropna()

#Función 3: Normalización de datos numéricos 
def normalizar_datos(df, columnas): 
    """Normaliza columnas numéricas entre 0 y 1.""" 
    df_normalizado = df.copy() 
    scaler = MinMaxScaler() 
    df_normalizado[columnas] = scaler.fit_transform(df_normalizado[columnas]) 
    return df_normalizado

#Función 5: Imputación de valores faltantes 

def imputar_valores(df, estrategia='media'): 
    """Imputa valores faltantes con media, mediana o moda.""" 
    df_imputado = df.copy() 
    imputer = SimpleImputer(strategy=estrategia) 
    df_imputado[df.columns] = imputer.fit_transform(df_imputado) 

    return df_imputado 



