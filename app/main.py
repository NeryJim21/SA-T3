from fastapi import FastAPI
from .routers import ci, relaciones
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CMDB API")

app.include_router(ci.router, prefix="/cis", tags=["Configuration Items"])
app.include_router(relaciones.router, prefix="/relaciones", tags=["Relaciones entre CIs"])
