from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class ConfigurationItem(Base):
    __tablename__ = "configuration_items"

    id = Column(Integer, primary_key=True, index=True)
    nombre_ci = Column(String, nullable=False)
    tipo_ci = Column(String, nullable=False)
    descripcion = Column(Text)
    numero_serie = Column(String)
    version = Column(String)
    fecha_adquisicion = Column(Date)
    estado_actual = Column(String)
    ubicacion_fisica = Column(String)
    propietario = Column(String)
    fecha_cambio = Column(Date)
    descripcion_cambio = Column(Text)
    doc_relacionada = Column(Text)
    enlaces_incidentes = Column(Text)
    nivel_seguridad = Column(String)
    cumplimiento = Column(String)
    estado_configuracion = Column(String)
    numero_licencia = Column(String)
    fecha_vencimiento = Column(Date)
    ambiente = Column(String)

    relaciones_padre = relationship("RelacionCI", foreign_keys="[RelacionCI.padre_id]", back_populates="padre")
    relaciones_hijo = relationship("RelacionCI", foreign_keys="[RelacionCI.hijo_id]", back_populates="hijo")

class RelacionCI(Base):
    __tablename__ = "relaciones_ci"

    id = Column(Integer, primary_key=True)
    padre_id = Column(Integer, ForeignKey("configuration_items.id"))
    hijo_id = Column(Integer, ForeignKey("configuration_items.id"))
    tipo_relacion = Column(String)

    padre = relationship("ConfigurationItem", foreign_keys=[padre_id], back_populates="relaciones_padre")
    hijo = relationship("ConfigurationItem", foreign_keys=[hijo_id], back_populates="relaciones_hijo")
