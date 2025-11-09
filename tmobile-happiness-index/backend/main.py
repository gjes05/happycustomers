from fastapi import FastAPI
from backend.data_simulator import generate_synthetic_data
from backend.stream_processor import process_stream_data
from backend.database import SessionLocal, HappinessRecord
from sqlalchemy import desc

app = FastAPI()

# In-memory storage for the latest processed data point for simplicity
latest_data = {}

@app.get("/")
def read_root():
    return {"message": "T-Mobile Happiness Index API"}

@app.post("/api/data")
def trigger_data_processing():
    """
    Generates a new synthetic data point, processes it, and stores it.
    This simulates a new event coming into the system.
    """
    global latest_data
    # In a real app, store_id might come from the request
    raw_data = generate_synthetic_data(store_id=101)
    processed_data = process_stream_data(raw_data)
    latest_data = processed_data
    return processed_data

@app.get("/api/dashboard-data")
def get_dashboard_data():
    """
    Returns the latest processed data and a summary of recent events
    for the frontend dashboard.
    """
    db = SessionLocal()
    try:
        # Get the most recent record
        latest_record = db.query(HappinessRecord).order_by(desc(HappinessRecord.timestamp)).first()

        # Get the last 10 records for some trend analysis (placeholder)
        recent_records = db.query(HappinessRecord).order_by(desc(HappinessRecord.timestamp)).limit(10).all()

        # In a real dashboard, you'd aggregate this data meaningfully
        # Here, we'll just pass the latest record's score and some alerts

        alerts = []
        if latest_record and latest_record.happiness_score < 60:
            alerts.append(f"Low happiness score detected at store {latest_record.store_id}: {latest_record.happiness_score:.2f}")

        return {
            "latest_score": latest_record.happiness_score if latest_record else 85,
            "alerts": alerts,
            "recent_events_count": len(recent_records)
        }
    finally:
        db.close()
