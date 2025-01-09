from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound
from models import SessionLocal, Task
from crud.users_crud import create_user, get_all_users, update_user_email, delete_user
from crud.todolists_crud import *

# CRUD for Task
def create_task(db: Session, todo_list_id: int, description: str, is_done: bool=False):
    new_task = Task(todo_list_id=todo_list_id, description=description, is_done=is_done)
    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except IntegrityError as e:
        db.rollback()
        return None
    

def get_task(db: Session, task_id: int):
    try:
        task = db.query(Task).filter(Task.id == task_id).one()
        return task
    except NoResultFound:
        return None
    
def get_all_tasks(db: Session):
    tasks = db.query(Task).all()
    return tasks


def get_all_task_status(db: Session, task_id: int, is_done: bool):
    task = get_task(db, task_id)
    if task:
        task.is_done = is_done
        db.commit()
        db.refresh(task)
        status = 'Complated' if is_done else 'Incomplate'
        print(f'Task ID {task_id} marked as {status}.')
        return task
    else: 
        print(f'Cannot update; Task ID {task_id} does not exist.')
        return None
    

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
        print(f'Task ID {task_id} deleted.')
        return True
    else:
        print(f'Cannot delete; Task ID {task_id} does not exist.')
        return False


if __name__ == '__main__':
    # Creating a new Session
    db = SessionLocal()

    try:
        # Creating new User
        user = create_user(db, "balice", "balice@example.com", "password123")
        if user:
            print(f'Created User: ID={user.id}, Username={user.username}')

        # Read all users
        users = get_all_users(db)
        print('\nAll Users: ')
        for u in users:
            print(f'ID: {u.id}, Username: {u.username}, Email: {u.email}')

        # Updating user's email
        if user:
            updated_user = update_user_email(db, user.id, 'alice_new@exapmle.com')
            if updated_user:
                print(f'\nUpdated User Email: ID={updated_user.id}, New Email={updated_user.email}')

        # Create a new TodoList for the User 
        if user:
            todo = create_todo_list(db,  user.id, 'Alice\'s First todo List')
            if todo:
                print(f'\nCreated TodoList: ID={todo.id}, Name={todo.name}')
        # Read all TodoLists
        todos = get_all_todo_lists(db)
        print('\nAll TodoLists:')
        for t in todos:
            print(f'ID: {t.id}, Name: {t.name}, User ID: {t.user_id}')

        # create new task in the TodoList
        if todo:
            task = create_task(db, todo.id, 'Buy groceries')
            if task:
                print(f'\nCreated Task: ID={task.id}, Description={task.description}')
        
        # Read all Tasks
        tasks = get_all_tasks(db)
        print('nAll Tasks')
        for ta in tasks:
            status = 'Done' if ta.is_done else 'Not Done'
            print(f'ID: {ta.id}, Description: {ta.description}, Status: {status}')

        # Update Task status to Done
        if task:
            updated_task = get_all_task_status(db, task.id, True)
            if updated_task:
                print(f'\nUpdated Task Status: ID={updated_task.id}, Status={'Done' if updated_task.is_done else 'Not Done'}')
        
        # Delete Task
        if task:
            if delete_task(db, task.id):
                print(f"\nDeleted Task ID: {task.id}")

        # Delete TodoList
        if todo:
            if delete_todo_list(db, todo.id):
                print(f'Deleted TodoList ID: {todo.id}')
        
        # Delete user
        if user:
            if delete_user(db, user.id):
                print(f'Deleted User ID: {user.id}')

    except Exception as e:
        print(f'An error occurred during CRUD operations: {e}')
        db.rollback()
    finally:
        db.close()