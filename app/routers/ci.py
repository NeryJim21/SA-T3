from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.CI)
def crear_ci(ci: schemas.CICreate, db: Session = Depends(database.get_db)):
    return crud.crear_ci(db, ci)

@router.get("/", response_model=list[schemas.CI])
def leer_cis(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.obtener_cis(db, skip, limit)

@router.get("/{ci_id}", response_model=schemas.CI)
def leer_ci(ci_id: int, db: Session = Depends(database.get_db)):
    db_ci = crud.obtener_ci(db, ci_id)
    if db_ci is None:
        raise HTTPException(status_code=404, detail="CI no encontrado")
    return db_ci

@router.put("/{ci_id}", response_model=schemas.CI)
def actualizar_ci(ci_id: int, ci: schemas.CICreate, db: Session = Depends(database.get_db)):
    return crud.actualizar_ci(db, ci_id, ci)

@router.delete("/{ci_id}")
def eliminar_ci(ci_id: int, db: Session = Depends(database.get_db)):
    return crud.eliminar_ci(db, ci_id)
