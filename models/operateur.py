import typing

from sqlalchemy import orm

from models.base import Base

if typing.TYPE_CHECKING:
    from models.sousTraitant import SousTraitant


class Operateur(Base):
    __tablename__ = 'Operateurs'
    Numero: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    Operateur: orm.Mapped[str] = orm.mapped_column()
    OperateurActif: orm.Mapped[int] = orm.mapped_column()
    OperateurPublic: orm.Mapped[int] = orm.mapped_column()
    AbrevQGISOp: orm.Mapped[str] = orm.mapped_column()

    SousTraitants: orm.Mapped[list['SousTraitant']] = orm.relationship()