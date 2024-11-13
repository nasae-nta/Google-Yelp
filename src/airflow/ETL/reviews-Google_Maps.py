import pandas as pd
import numpy as np
import warnings
import os
import sys
import logging

# Ignorar advertencias
warnings.filterwarnings('ignore')

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Navegar hacia el directorio raíz del proyecto
project_root = os.path.abspath(os.path.join(os.getcwd(), '../../..'))

# Agregar la ruta del proyecto al sys.path para traer librerías personalizadas
sys.path.append(project_root)

######################################### FUNCIONES #########################################

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

def ETL(df, file_path, cols_to_delete):
    """
    Procesa los datos, los limpia, y retorna un dataframe.
    """
    # se verifica si existen columnas a eliminar, si el valor es None, no se elimina ninguna
    if cols_to_delete is not None and len(df) != 0:
        # se eliminan las columnas innecesarias de df
        df = df.drop(cols_to_delete, axis=1)
        print(f"Eliminado en {file_path} completado exitosamente con {len(df)} registros.")

    # Se verifica que existan filas en el df y normaliza los datos
    if len(df) != 0 and df is not None:
        # se rellenan los valores nulos de las columnas de texto con una cadena vacía
        df['text'] = df['text'].fillna('')

        # se normalizan los datos de las columnas de texto, enteros y decimales
        df['rating'] = df['rating'].astype(int)

        # se definen las columnas con tipos de dato texto, entero y float
        text = ['name', 'text', 'gmap_id']
        for c in text:
            df[c] = df[c].str.lower()
            df[c] = df[c].str.strip()

        print(f"Normalizado en {file_path} completado exitosamente con {len(df)} registros.")

    return df

############################################ MAIN ############################################

def __main__():
    # se guarda el directorio con los datasets en una variable
    data_dir = os.path.join(project_root, 'data/raw/google_maps/reviews-estados/review-Florida')
    final_dir = os.path.join(project_root, 'data/processed/google_maps/reviews-estados/review-Florida')
    metadata_dir = os.path.join(project_root, 'data/processed/google_maps/metadata-sitios')

    #se importan los datos de los datasets en metadata-sitios procesados de forma unificada
    metadata = merge_files(metadata_dir)

    #Se definen las columnas a eliminar (None para no filtrar)
    cols_to_delete = ['pics', 'resp']

    counter = 0

    # Recorre todas las carpetas y archivos en el directorio raíz
    for dirpath, _, filenames in os.walk(data_dir):
        for file in filenames:
            if file.endswith('.parquet'):
                file_path = os.path.join(dirpath, file)
                final_path = os.path.join(final_dir, file)

                try:
                    print(f"Leyendo archivo: {file_path}")
                    df = pd.read_parquet(file_path)
                    print(f"Archivo {file_path} leído exitosamente con {len(df)} registros.")
                    
                    # Filtrar los datos de florida donde gmap_id también esté en metadata
                    df = df[df['gmap_id'].isin(metadata['gmap_id'])]
                    print(f"Filtrado exitoso con {len(df)} registros.")

                    if len(df) != 0:
                        # se intenta aplicar el ETL a cada archivo si es que tiene resultados
                        df = ETL(df, file, cols_to_delete)
                
                except Exception as e:
                    print(f"Error al leer {file_path}: {e}")

                # Se verifica que existan filas en el df antes de exportar
                if len(df) != 0 and df is not None:
                    # Se exporta el df final
                    df.to_parquet(final_path)
                    print(f"Exportado en {file_path} completado exitosamente con {len(df)} registros.")
                    counter += len(df)

    print(f'TOTAL DE ELEMENTOS PROCESADOS: {counter}')

if __name__ == '__main__':
    __main__()
