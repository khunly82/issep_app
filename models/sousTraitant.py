import typing

import sqlalchemy as sql
import sqlalchemy.orm as orm

from models.base import Base

if typing.TYPE_CHECKING:
    from models.operateur import Operateur


class SousTraitant(Base):
    __tablename__ = 'SousTraitants'
    Numero: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    NumOperateur: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey('Operateurs.Numero'))
    SousTraitant: orm.Mapped[str] = orm.mapped_column()
    Actif: orm.Mapped[int] = orm.mapped_column()

    operateur: orm.Mapped['Operateur'] = orm.relationship()