from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

root = os.getenv("ROOT")

engine = create_engine(f"mysql+pymysql://root:{root}@localhost/laptops", echo=True)

TABLES = {
"laptop": """
    CREATE TABLE IF NOT EXISTS laptop (
    id INTEGER PRIMARY KEY auto_increment,
    title VARCHAR(400),
    image TEXT,
    price VARCHAR(50),
    property TEXT,

    UNIQUE (title)
f    )
"""
}


