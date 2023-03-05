from sqlalchemy import String, Column, Float, Integer, Text
from config.db import Base

class DespachoDTO(Base):
    __tablename__ = "despachos"

    order_id = Column(String(36), primary_key=True, index=True)
    customer_id = Column(String(36), index=True)
    order_date = Column(String(100), index=True)
    order_status = Column(String(100), index=True)
    order_items = Column(Text(1000000), index=True)
    order_total = Column(Float, index=True)
    pod_id = Column(String(100), index=True)
    date_despacho = Column(String(100), index=True)
    vehiculo_minimo_code = Column(String(100), index=True)
    order_version = Column(Integer, index=True)

    
