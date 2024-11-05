import pandas as pd
import os

# se define una función que leerá los datasets, los unificará y retornará uno solo con toda la data
def merge_files(root_folder):
    """
    Lee todos los archivos Parquet en múltiples carpetas dentro de una carpeta raíz,
    y los unifica en un único DataFrame.

    Parámetros:
    - root_folder (str): La ruta de la carpeta raíz que contiene subcarpetas con archivos Parquet.

    Retorna:
    - pd.DataFrame: Un DataFrame unificado con todos los datos de los archivos Parquet.
    """
    # Lista para almacenar todos los DataFrames leídos
    data_frames = []

    # Recorre todas las carpetas y archivos en el directorio raíz
    for dirpath, _, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith('.parquet'):
                file_path = os.path.join(dirpath, file)
                
                # Intenta leer el archivo Parquet y añade el DataFrame a la lista
                try:
                    print(f"Leyendo archivo: {file_path}")
                    df = pd.read_parquet(file_path)
                    data_frames.append(df)
                    print(f"Archivo {file} leído exitosamente con {len(df)} registros.")
                except Exception as e:
                    print(f"Error al leer {file_path}: {e}")

    # Concatenar todos los DataFrames en uno solo
    if data_frames:
        unified_df = pd.concat(data_frames, ignore_index=True)
        print(f"Todos los archivos Parquet han sido unificados en un único DataFrame con {len(unified_df)} registros.")
        return unified_df
    else:
        print("No se encontraron archivos Parquet en las carpetas especificadas o todos fallaron al leerse.")
        return None  # Devuelve None si no hay DataFrames para concatenar

def get_frequency(dfr, elem):
    '''
    Recibe un DataFrame y el nombre de la columna sobre la cual sacar la frecuencia.
    Retorna un DataFrame con los elementos únicos, la cantidad de veces que aparece y el porcentaje de estos respecto al total de valores en el DataFrame.
    '''
    # si no existe una columna de control, se aisla la columna necesaria
    df = dfr[[elem]]

    # se calcula la frecuencia
    freq = df[elem].value_counts().reset_index()
    freq.columns = [elem, 'frequency']

    # se calcula el porcentaje
    freq['percentage'] = round((freq['frequency'] / freq['frequency'].sum()) * 100, 2)

    return freq