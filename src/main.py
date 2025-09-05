from fastapi import FastAPI
from src.core.config import settings
from sqlite3.dbapi2 import version
from src.db import base

app = FastAPI(tittle=settings.PROJEC_NAME,version=settings.PROJEC_VERSION)
