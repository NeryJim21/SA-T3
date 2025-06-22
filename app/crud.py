from sqlalchemy.orm import Session
from . import models, schemas

def crear_ci(db: Session, ci: schemas.CICreate):
    db_ci = models.ConfigurationItem(**ci.dict())
    db.add(db_ci)
    db.commit()
    db.refresh(db_ci)
    return db_ci

def obtener_cis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ConfigurationItem).offset(skip).limit(limit).all()

def obtener_ci(db: Session, ci_id: int):
    return db.query(models.ConfigurationItem).filter(models.ConfigurationItem.id == ci_id).first()

def actualizar_ci(db: Session, ci_id: int, ci: schemas.CICreate):
    db_ci = obtener_ci(db, ci_id)
    if db_ci:
        for key, value in ci.dict().items():
            setattr(db_ci, key, value)
        db.commit()
        db.refresh(db_ci)
    return db_ci

def eliminar_ci(db: Session, ci_id: int):
    db_ci = obtener_ci(db, ci_id)
    if db_ci:
        db.delete(db_ci)
        db.commit()
    return db_ci

def crear_relacion(db: Session, relacion: schemas.RelacionCreate):
    db_rel = models.RelacionCI(**relacion.dict())
    db.add(db_rel)
    db.commit()
    db.refresh(db_rel)
    return db_rel

def obtener_relaciones(db: Session):
    return db.query(models.RelacionCI).all()
