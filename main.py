import sqlalchemy as sql

from models.sessionFactory import session_factory
from models.operateur import Operateur

with session_factory() as session:
    query = sql.select(Operateur)
    operateurs = session.scalars(query).all()
    for o in operateurs:
        print(o.Operateur)
        for st in o.SousTraitants:
            print('\t' + st.SousTraitant)
