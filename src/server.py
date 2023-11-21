from fastapi import FastAPI

from views.password_manager import password_manager_router


app = FastAPI()

app.include_router(password_manager_router)
