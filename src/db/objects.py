from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

from db.utils import make_pg_url
from config import AppConfig


engine = create_engine(make_pg_url(
    host=AppConfig.DB_HOST,
    port=AppConfig.DB_PORT,
    username=AppConfig.DB_USERNAME,
    password=AppConfig.DB_PASSWORD,
    db_name=AppConfig.DB_NAME,
))
meta_data = MetaData()
BaseModel = declarative_base(metadata=meta_data)
Session = sessionmaker(bind=engine)
