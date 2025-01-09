from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import List

DATABASE_URL = 'postgresql://xcoder:xxx7451155@localhost:5432/postgredb'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    todolists: Mapped[List['TodoList']] = relationship(
        'TodoList', back_populates='owner', cascade='all, delete-orphan'
    )
    role: Mapped[str] = mapped_column(String, default='user', nullable=False)

class TodoList(Base):
    __tablename__ = 'todo_lists'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    owner: Mapped['User'] = relationship(
        'User', back_populates='todolists'
    )
    tasks: Mapped[List['Task']] = relationship(
        'Task', back_populates='todo_list', cascade='all, delete-orphan'
    )


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    todo_list_id: Mapped[int] = mapped_column(
        ForeignKey('todo_lists.id', ondelete='CASCADE')
    )
    description: Mapped[str] = mapped_column(String, nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    todo_list: Mapped['TodoList'] = relationship(
        'TodoList', back_populates='tasks'
    )



# db = SessionLocal()

# new_user = User(username='testuser', email='test@example.com', password='1234')
# db.add(new_user)
# db.commit()
# db.refresh(new_user)
# print(new_user.id, new_user.created_at)

# users = db.query(User).all()
# print(users)
