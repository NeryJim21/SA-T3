from .database import SessionLocal
from .models import ConfigurationItem
from datetime import date

db = SessionLocal()
ci = ConfigurationItem(
    nombre_ci="Servidor1",
    tipo_ci="Hardware",
    descripcion="Servidor de Aplicaciones",
    numero_serie="SN123456",
    version="v1.0",
    fecha_adquisicion=date(2022, 1, 1),
    estado_actual="Activo",
    ubicacion_fisica="Sala de Servidores 1",
    propietario="Equipo de Infraestructura",
    fecha_cambio=date(2022, 2, 1),
    descripcion_cambio="Actualización de Software",
    ambiente="PROD"
)
db.add(ci)
db.commit()
db.close()
