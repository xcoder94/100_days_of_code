from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from dependencies import get_db
from models import User
from schemas import UserOut, UserCreate, Token, CheckUser
from crud.users_crud import create_user, delete_user, get_user
from security import hash_password, get_current_user, verify_password, create_access_token

# Initialize the router 
router = APIRouter()

@router.post('/login', response_model=Token)
def login_user(user_data: CheckUser, db: Session = Depends(get_db)):
    user = get_user(db, user_id=None, username=user_data.username)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    if not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=400, detail='Invalid password')
    
    # Credentials are valid, create token
    access_token = create_access_token(data={'sub': str(user.id)})
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/me', response_model=UserOut)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.post('/', response_model=UserOut)
def create_user_endpoint(user_data: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user_data.password)
    user = create_user(db, user_data.username, user_data.email, hashed_password)
    if user:
        return user
    else:
        # Return response indicating user creation failed (e.g., unique constraint)
        # FastAPI Will convert the dictionary to json automaticly
        return {'Error': 'User not created'}

@router.get('/')
def get_users_endpoint(
    db: Session = Depends(get_db),
    page: int = 1,
    size: int = 10, 
    sort_by: str = 'id',
    sort_order: str = 'asc'
):
    # Start the query with the 'users' table
    query = db.query(User)

    # Sorting
    valid_sort_columns = {'id', 'username', 'created_at'}
    if sort_by not in valid_sort_columns:
        sort_by = 'id'
    
    if sort_order.lower() == 'desc':
        query = query.order_by(desc(getattr(User, sort_by)))
    else:
        query = query.order_by(asc(getattr(User, sort_by)))

    # Pagination
    total_records = query.count()
    items = query.offset((page - 1) * size).limit(size).all()

    return {
        'page': page,
        'size': size,
        'total_records': total_records,
        'items': items
    }


@router.delete('/{user_id}')
def delete_user_endpoint(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.id != user_id and current_user.role != 'admin':
        raise HTTPException(status_code=403, detail='Not enough permissions')
    
    success = delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail='User not found')
    return {'message': 'User deleted successfully'}

