from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column


Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
