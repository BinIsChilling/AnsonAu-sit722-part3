from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://books_inventory_user:9hNFJrnxrxlTVYcGkiVFuBEhvu5hFNoh@dpg-criiimm8ii6s73f45to0-a.oregon-postgres.render.com/books_inventory" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
