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

def filter_in_columns(df, col, elems):
    """
    Filtra las filas de un DataFrame en las que una columna que contiene listas tiene elementos que coinciden con
    al menos uno de los términos en `elems`. Retorna el DataFrame filtrado.
    """
    # Convertir valores de la columna `col` a listas si son `numpy.ndarray`
    df[col] = df[col].apply(lambda x: list(x) if isinstance(x, np.ndarray) else x) 

    # se explota la columna especificada
    df = df.explode(column=col)
    logging.info(f"Después de explotar '{col}', el DataFrame tiene {len(df)} filas.")

    # todos los elementos de la columna se convierten a minúscula
    df[col] = df[col].str.lower()

    # se reescribe elems como expresión regular
    elems = '|'.join(elems)

    # mantener solo las categorías que contengan las palabras claves de elems y que no me traiga la palabra public
    df = df[
        df[col].str.contains(elems, case=False, na=False) & 
        ~df[col].str.contains('public', case=False, na=False)
    ]
    logging.info(f"Después del filtro de palabras clave, el DataFrame tiene {len(df)} filas.")

    # Asegurarse de que todos los valores son strings
    df[col] = df[col].astype(str)

    # se crea una lista con los nombres de todas las columnas excepto la columna ingresada
    columns = [c for c in df.columns if c != col]
    for c in columns:
        df[c] = df[c].apply(lambda x: str(x) if isinstance(x, (list, np.ndarray, dict)) else x)
    print("Columns to group by:", columns)
    
    try:
        # Agrupar y agregar con `list`
        df = df.groupby(columns).agg({col: list}).reset_index()
        logging.info(f"Después de reagrupar, el DataFrame final tiene {len(df)} filas.")
    except Exception as e:
        logging.error(f"Error en la agregación: {e}")
        raise

    # retorna el dataframe
    return df


def filter_services(df, services=[], col=None):
    '''
    Recibe un dataframe, una lista con servicios y nombre de columna a filtrar.
    Filtra el dataframe para obtener aquellos que contengan alguna palabra que coincida con las de las categorías dadas.
    Retorna un arreglo filtrado, también filtra las categorías.
    Si sólo recibe el dataframe y no la lista o el nombre de la columna, retorna el dataframe original.
    '''
    logging.info(f"Filtrando servicios en la columna '{col}' con palabras clave: {services}")

    # si la lista services está vacía, retorna el df
    if services == [] or col is None:
        return df
    
    if col not in df.columns:
        logging.warning(f"Columna '{col}' no encontrada en el DataFrame")
        return df

    # Filtra filas que contengan algún servicio en la columna `col`, verificando que sea lista o tupla
    df = df[df[col].apply(lambda x: x is not None and any(
        any(service.lower() in category.lower() for service in services) for category in x
    ))]
    logging.info(f"Después del filtro de servicios, el DataFrame tiene {len(df)} filas.")

    # se filtran las palabras clave de negocios gastronómicos en la columna category y se convierten los resultados en una lista de listas ##########################################################
    data = filter_in_columns(df, col, services)

    logging.info(f"DataFrame resultante después de filter_in_columns tiene {len(data)} filas.")
    # se retorna el df resultante
    return data

def filter_ubication(df, col=None, filter=None):
    '''
    Recibe un dataframe, el nombre de la columna sobre la que se va a buscar el substrin de filter.
    Retorna el df con los datos que contengan la palabra en filter
    '''
    # Filtra filas que contengan algún servicio en la columna `col`, verificando que sea lista o tupla
    df = df[df[col].apply(lambda x: x is not None and filter in x)]
    logging.info(f"Filtrando ubicación en la columna '{col}' con palabra clave: {filter}")

    # se retorna el df final
    return df

def ETL(file_path, services, cols_to_delete, coor, filter_col):
    """
    Procesa un archivo Parquet aplicando los filtros de coordenadas, servicios y columnas, y lo guarda en el destino especificado.
    """
    # Intenta leer el archivo Parquet y lo procesa
    try:
        print(f"Leyendo archivo: {file_path}")
        df = pd.read_parquet(file_path)
        print(f"Archivo {file_path} leído exitosamente con {len(df)} registros.")
        
        # se verifica si existen coordenadas, si el valor es None, no se filtra ninguna
        if coor is not None:
            # se filtran las filas de df que no tengan coordenadas
            df = filter_ubication(df, coor[0], coor[1])
            print(f"Filtrado en {file_path} completado exitosamente con {len(df)} registros.")

        # si existe la columna state, se filtran los elementos que no estén permanentemente cerrados
        if 'state' in df.columns:
            # se filtran las filas de df que no estén permanentemente cerrados
            df = df[df['state'] != 'Permanently closed']

        # se verifica si existen filas a eliminar, si el valor es None, no se elimina ninguna
        if services is not None and len(df) != 0:
            # se filtran las filas de df que contengan alguna palabra clave de negocios gastronómicos en la columna category
            df = filter_services(df, services, filter_col)
            print(f"Filtrado en {file_path} completado exitosamente con {len(df)} registros.")

        # se verifica si existen columnas a eliminar, si el valor es None, no se elimina ninguna
        if cols_to_delete is not None and len(df) != 0:
            # se eliminan las columnas innecesarias de df
            df = df.drop(cols_to_delete, axis=1)
            print(f"Eliminado en {file_path} completado exitosamente con {len(df)} registros.")

        return df
        
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        return None

######################################### MAIN #########################################

def __main__():
    # se guarda el directorio con los datasets en una variable
    data_dir = os.path.join(project_root, 'data/raw/google_maps/metadata-sitios')
    final_dir = os.path.join(project_root, 'data/processed/google_maps/metadata-sitios')

    # se crea una lista con palabras clave de negocios gastronómicos para filtrar (None para no filtrar)
    services = ['restaurant', 'food', 'pub', 'ice cream', 'coffee', 'bakery', 'diner', 'buffet', 'bar', 'brewery']

    # se define la columna en la que se aplicará el filtro
    filter_col = 'category'

    #Se definen las columnas a eliminar (None para no filtrar)
    cols_to_delete = ['description', 'hours', 'state', 'relative_results', 'MISC', 'url']

    # Se definen las coordenadas de Tampa para filtrar en formato [columna, ciudad]. None para no filtrar por coordenadas
    coor = ['address', 'Tampa']

    counter = 0

    # Recorre todas las carpetas y archivos en el directorio raíz
    for dirpath, _, filenames in os.walk(data_dir):
        for file in filenames:
            if file.endswith('.parquet'):
                file_path = os.path.join(dirpath, file)
                final_path = os.path.join(final_dir, file)
                
                # se intenta aplicar el ETL a cada archivo
                df = ETL(file_path, services, cols_to_delete, coor, filter_col)

                # Se verifica que existan filas en el df y normaliza los datos
                if len(df) != 0 and df is not None:
                    # se normalizan los datos de las columnas de texto, enteros y decimales
                    df['latitude'] = df['latitude'].astype(float)
                    df['longitude'] = df['longitude'].astype(float)
                    df['avg_rating'] = df['avg_rating'].astype(float)
                    df['num_of_reviews'] = df['num_of_reviews'].astype(int)

                    # se definen las columnas con tipos de dato texto, entero y float
                    text = ['name', 'address', 'gmap_id']
                    for c in text:
                        df[c] = df[c].str.lower()
                        df[c] = df[c].str.strip()

                    print(f"Normalizado en {file} completado exitosamente con {len(df)} registros.")

                # Se verifica que existan filas en el df antes de exportar
                if len(df) != 0 and df is not None:
                    # Se exporta el df final
                    df.to_parquet(final_path)
                    print(f"Exportado en {file_path} completado exitosamente con {len(df)} registros.")
                    counter += len(df)

    print(f'TOTAL DE ELEMENTOS PROCESADOS: {counter}')

if __name__ == '__main__':
    __main__()