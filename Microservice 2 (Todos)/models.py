from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column


Base = declarative_base()


class Todo(Base):

    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    todo: Mapped[str]
    is_completed: Mapped[bool]
