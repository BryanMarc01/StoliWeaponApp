from pymongo import MongoClient
from datetime import datetime

# Conexión a la base de datos
client = MongoClient('mongodb://tu_mongodb_uri')
db = client['tu_db']
backups_collection = db['backups']

# Registro del backup en la base de datos
backup_record = {
    'file_path': '/backups/backup.xlsx',
    'created_at': datetime.now()
}
backups_collection.insert_one(backup_record)
print('Backup registrado exitosamente')
