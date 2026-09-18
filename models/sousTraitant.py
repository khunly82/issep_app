import sqlalchemy as sql
import sqlalchemy.orm as orm

from models.base import Base


class SousTraitant(Base):
    __tablename__ = 'SousTraitants'
    Numero: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    NumeroOperateur: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey('Operateurs.Numero'))
    SoutTraitant: orm.Mapped[str] = orm.mapped_column()
    Actif: orm.Mapped[int] = orm.mapped_column()