import urllib.parse

import sqlalchemy as sql
import sqlalchemy.orm as orm

db_path = r'D:\K\Desktop\DatabaseISSEP.accdb'
odbc_driver = "Microsoft Access Driver (*.mdb, *.accdb)"

connection_string = (
    f'DRIVER={{{odbc_driver}}};'
    f'DBQ={db_path};'
    'ReadOnly=0;'
    'ExtendedAnsiSQL=1;'
)

connection_url = sql.URL.create('access+pyodbc', query={
    'odbc_connect': urllib.parse.quote_plus(connection_string)
})

engine = sql.create_engine(url=connection_url)

session_factory = orm.sessionmaker(bind=engine)