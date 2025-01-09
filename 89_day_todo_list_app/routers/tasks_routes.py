from fastapi import Depends, APIRouter, HTTPException
from crud.tasks_crud import create_task, get_all_tasks, get_task, delete_task
from sqlalchemy.orm import Session
from schemas import TaskCreate, TaskOut
from dependencies import get_db

router = APIRouter()

@router.post('/task', response_model=TaskOut)
def create_task_endpoint(task_data: TaskCreate, db: Session = Depends(get_db)):
    task = create_task(db, task_data.todo_list_id, task_data.description, task_data.is_done)
    if task:
        return task
    else:
        return {'Error': 'Create Task'}
    

@router.get('/task', response_model=list[TaskOut])
def get_task_endpoint(db: Session = Depends(get_db)):
    tasks = get_all_tasks(db)
    return tasks


@router.put('/{task_id}', response_model=TaskOut)
def update_task_endpoint(
    task_id: int, 
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):
    existing_task = get_task(db,task_id)
    if not existing_task:
        raise HTTPException(status_code=404, detail='Task not found')
    
    existing_task.description = task_data.description
    existing_task.is_done = task_data.is_done
    db.commit()
    db.refresh(existing_task)
    return existing_task


@router.delete('/{task_id}')
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    success = delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail='Task is not found')
    return {'message': 'Task deleted succesfully'}

