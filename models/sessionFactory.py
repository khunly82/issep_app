import os
import urllib.parse

import dotenv
import sqlalchemy as sql
import sqlalchemy.orm as orm

dotenv.load_dotenv()

odbc_driver = "Microsoft Access Driver (*.mdb, *.accdb)"
db_path = os.getenv('DB_PATH')
password = os.getenv('DB_PASSWORD')

connection_string = (
    f'DRIVER={{{odbc_driver}}};'
    f'DBQ={db_path};'
    f'PWD={password};'
    'ReadOnly=0;'
    'ExtendedAnsiSQL=1;'
)

connection_url = sql.URL.create('access+pyodbc', query={
    'odbc_connect': urllib.parse.quote_plus(connection_string)
})

engine = sql.create_engine(url=connection_url)

session_factory = orm.sessionmaker(bind=engine)