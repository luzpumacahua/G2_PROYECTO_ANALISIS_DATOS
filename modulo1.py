import pandas as pd

def cargar_datos(nombre_archivo):
    """
    Carga un archivo CSV y devuelve un DataFrame
    """
    return pd.read_csv(nombre_archivo)
