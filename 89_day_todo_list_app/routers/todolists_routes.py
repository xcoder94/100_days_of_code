from crud.todolists_crud import create_todo_list, get_all_todo_lists, delete_todo_list
from schemas import TodoListCreate, TodoListOut
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db

router = APIRouter()

@router.post('/', response_model=TodoListOut)
def create_todo_list_endpoint(todo_list_data: TodoListCreate, db: Session = Depends(get_db)):
    todo_list = create_todo_list(db, todo_list_data.user_id, todo_list_data.name)
    if todo_list:
        return todo_list
    else:
        return {'Error': 'TodoList not created'}
    

@router.get('/', response_model=list[TodoListOut])
def get_todo_list_endpoint(db: Session = Depends(get_db)):
    todo_lists = get_all_todo_lists(db)
    return todo_lists


@router.put('/{todolist_id}', response_model=TodoListOut)
def update_todolist_endpoint(
    todolist_id: int,
    data: TodoListCreate,
    db: Session = Depends(get_db)
):
    existing_todolist = get_db, todolist_id
    if not existing_todolist:
        raise HTTPException(status_code=404, detail='Todo list not found')
    existing_todolist.name = data.name
    db.commit()
    db.refresh(existing_todolist)
    return existing_todolist


@router.delete('/{todolist_id}')
def delete_todolist_endpoint(todolist_id: int, db: Session = Depends(get_db)):
    success = delete_todo_list(db, todolist_id)
    if not success:
        raise HTTPException(status_code=404, detail='Todolist not found')
    return {'message': 'Todolist deleted successfuly'}
