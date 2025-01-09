from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound
from models import SessionLocal, User, TodoList, Task

# CRUD for TodoList
def create_todo_list(db: Session, user_id: int, name: str):
    new_todo = TodoList(user_id=user_id, name=name)
    try:
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        print(f"TodoList created with ID: {new_todo.id}")
        return new_todo
    except IntegrityError as e:
        db.rollback()
        print(f"Error creating TodoList: {e}")
        return None


def get_todo_list(db: Session, todo_list_id: int):
    try:
        todo = db.query(TodoList).filter(TodoList.id == todo_list_id).one()
        return todo
    except NoResultFound:
        print(f"TodoList with ID {todo_list_id} not found.")
        return None


def get_all_todo_lists(db: Session):
    todos = db.query(TodoList).all()
    return todos


def update_todo_list_name(db: Session, todo_list_id: int, new_name: str):
    todo = get_todo_list(db, todo_list_id)
    if todo:
        todo.name = new_name
        db.commit()
        db.refresh(todo)
        print(f"TodoList ID {todo_list_id} name updated to {new_name}")
        return todo
    else:
        print(f"Cannot update name; TodoList ID {todo_list_id} does not exist.")
        return None


def delete_todo_list(db: Session, todo_list_id: int):
    todo = get_todo_list(db, todo_list_id)
    if todo:
        db.delete(todo)
        db.commit()
        print(f"TodoList ID {todo_list_id} deleted.")
        return True
    else:
        print(f"Cannot delete; TodoList ID {todo_list_id} does not exist.")
        return False