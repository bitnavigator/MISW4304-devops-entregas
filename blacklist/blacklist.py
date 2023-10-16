from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from datetime import datetime

# Configura la conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/blacklist"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Blacklist(Base): 
    __tablename__ = 'blacklist'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    app_uuid = Column(String, nullable=False)
    blocked_reason = Column(String, nullable=False)
    dir_ip = Column(String, nullable=False)
    createdat = Column(DateTime, default=datetime.now, nullable=False)