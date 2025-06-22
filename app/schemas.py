from pydantic import BaseModel
from datetime import date
from typing import Optional

class CIBase(BaseModel):
    nombre_ci: str
    tipo_ci: str
    descripcion: Optional[str] = None
    numero_serie: Optional[str] = None
    version: Optional[str] = None
    fecha_adquisicion: Optional[date] = None
    estado_actual: Optional[str] = None
    ubicacion_fisica: Optional[str] = None
    propietario: Optional[str] = None
    fecha_cambio: Optional[date] = None
    descripcion_cambio: Optional[str] = None
    doc_relacionada: Optional[str] = None
    enlaces_incidentes: Optional[str] = None
    nivel_seguridad: Optional[str] = None
    cumplimiento: Optional[str] = None
    estado_configuracion: Optional[str] = None
    numero_licencia: Optional[str] = None
    fecha_vencimiento: Optional[date] = None
    ambiente: Optional[str] = None

class CICreate(CIBase):
    pass

class CI(CIBase):
    id: int
    class Config:
        orm_mode = True

class RelacionCreate(BaseModel):
    padre_id: int
    hijo_id: int
    tipo_relacion: str

class Relacion(BaseModel):
    id: int
    padre_id: int
    hijo_id: int
    tipo_relacion: str
    class Config:
        orm_mode = True
