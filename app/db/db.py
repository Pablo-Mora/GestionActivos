from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from config import Config

# Aquí defines Base
Base = declarative_base()

def get_connection_string():
    cfg = Config.DB_CONFIG 
    if cfg["use_windows_auth"]:
        return (
            f"mssql+pyodbc://@{cfg['server']}/{cfg['database']}?"
            f"driver={cfg['driver'].replace(' ', '+')}&trusted_connection=yes"
        )
    else:
        return (
            f"mssql+pyodbc://{cfg['user']}:{cfg['password']}"
            f"@{cfg['server']}/{cfg['database']}?driver={cfg['driver'].replace(' ', '+')}"
        )

engine = create_engine(get_connection_string())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
