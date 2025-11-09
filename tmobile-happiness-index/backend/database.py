from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tmobile_happiness.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class HappinessRecord(Base):
    __tablename__ = "happiness_records"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    store_id = Column(Integer)
    customer_id = Column(String)
    text_input = Column(String)
    text_sentiment_score = Column(Float)
    voice_sentiment_score = Column(Float)
    camera_emotion_score = Column(Float)
    happiness_score = Column(Float)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def save_happiness_record(data):
    """Saves a happiness record to the database."""
    db = SessionLocal()
    db_record = HappinessRecord(
        store_id=data['store_id'],
        customer_id=data['customer_id'],
        text_input=data['text_input'],
        text_sentiment_score=data.get('text_sentiment_score', 0.0),
        voice_sentiment_score=data.get('voice_sentiment_score', 0.0),
        camera_emotion_score=data.get('camera_emotion_score', 0.0),
        happiness_score=data['happiness_score']
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    db.close()
    return db_record

if __name__ == "__main__":
    print("Creating database and tables...")
    create_db_and_tables()
    print("Done.")
