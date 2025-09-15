# connect to db just like mongo connected

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

URL_DATABASE=os.getenv('URL_DATABASE')

if not URL_DATABASE:
    raise ValueError("DATABASE_URL is not set in the .env file")

engine=create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()