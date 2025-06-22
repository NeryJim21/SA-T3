from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Relacion)
def crear_relacion(relacion: schemas.RelacionCreate, db: Session = Depends(database.get_db)):
    return crud.crear_relacion(db, relacion)

@router.get("/", response_model=list[schemas.Relacion])
def listar_relaciones(db: Session = Depends(database.get_db)):
    return crud.obtener_relaciones(db)
