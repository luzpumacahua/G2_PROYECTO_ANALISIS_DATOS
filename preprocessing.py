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