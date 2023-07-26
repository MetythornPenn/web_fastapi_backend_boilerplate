from fastapi import FastAPI, Depends
from starlette.staticfiles import StaticFiles

from routers import auth, todos
# import models.models
from models.models import Base
from db.database import engine

# --------------------------------------

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


# ------------- router -------------------

app.include_router(auth.router)
app.include_router(todos.router)

    

    
    