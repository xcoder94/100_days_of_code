from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound
from models import User

# CRUD for User
def create_user(db: Session, username: str, email: str, password: str, role: str = 'user'):
    new_user = User(username=username, email=email, password=password, role=role)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(f"User created with ID: {new_user.id}")
        return new_user
    except IntegrityError as e:
        db.rollback()
        print(f"Error creating user: {e}")
        return None
    

def get_user(db: Session, user_id: int, username: str):
    try:
        query = db.query(User)
        if user_id is not None:
            query = query.filter(User.id == user_id)
        if username is not None:
            query = query.filter(User.username == username)
        user = query.one()
        return user
    except NoResultFound:
        print(f"User with ID {user_id} not found.")
        return None
    

def get_all_users(db: Session):
    users = db.query(User).all()
    return users


def update_user_email(db: Session, user_id: int, new_email: str):
    user = get_user(db, user_id)
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
        print(f'User ID {user_id} email updated to {new_email}')
        return user
    else:
        print(f'Cannot update email; user ID {user_id} does not exist.')
        return None


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        print(f'User ID {user_id} deleted')
        return True
    else:
        print(f'Cannot delete; user ID {user_id} does not exist.')
        return False