import pandas as pd
from pymongo import MongoClient

# Conexión a la base de datos
client = MongoClient('mongodb://tu_mongodb_uri')
db = client['tu_db']
collection = db['tu_coleccion']

# Realiza la consulta y guarda los datos en un DataFrame
data = pd.DataFrame(list(collection.find()))

# Genera el archivo .xlsx
data.to_excel('/backups/backup.xlsx', index=False)
print('Backup generado exitosamente')
