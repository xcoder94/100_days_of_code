from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers import user_routes, todolists_routes, tasks_routes


app = FastAPI()
# Include the user router
app.include_router(user_routes.router, prefix='/users', tags=['Users'])
app.include_router(todolists_routes.router, prefix='/todolists', tags=['Todolists'])
app.include_router(tasks_routes.router, prefix='/tasks', tags=['Tasks'])


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')




    
