import pandas as pd

# Función para limpiar y preparar los datos
def clean_and_prepare_data(df):
    # Verificar valores faltantes y eliminar filas con valores faltantes
    df = df.dropna()

    # Verificar y eliminar filas duplicadas
    df = df.drop_duplicates()

    # Crear una columna de categorías de edad
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Joven adulto', 'Adulto', 'Adulto mayor']
    df['Categoría de Edad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

    # Guardar el DataFrame limpio en un archivo CSV
    df.to_csv('datos_limpios.csv', index=False)

    return df

# Leer el archivo "registros_ventas.txt" en un DataFrame
# Asumimos que la edad está en una columna llamada 'Edad'; ajusta según sea necesario
df = pd.read_csv('registros_ventas.txt', delimiter='\t')  # Ajusta el delimitador según sea necesario

# Llamar a la función con el DataFrame
datos_limpios = clean_and_prepare_data(df)

# Imprimir el DataFrame limpio
print(datos_limpios)
