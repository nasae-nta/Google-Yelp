import pandas as pd
import warnings
import os
import sys
from datetime import datetime, timedelta

# Ignorar advertencias
warnings.filterwarnings('ignore')

# Navegar hacia el directorio raíz del proyecto
project_root = os.path.abspath(os.path.join(os.getcwd(), '../../..'))

# Agregar la ruta del proyecto al sys.path para traer librerías personalizadas
sys.path.append(project_root)

# se guarda el directorio con el datasets de metadata procesado en una variable
data_dir = os.path.join(project_root, 'data/processed/google_maps/metadata_final.parquet')

# leer parquet y visualizar los primeros elementos
metadata = pd.read_parquet(data_dir)