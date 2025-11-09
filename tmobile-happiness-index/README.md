# T-Mobile Customer Happiness Index

This project is a proof-of-concept for a real-time customer happiness index dashboard for T-Mobile stores. It uses a combination of simulated data, machine learning models, and a web-based dashboard to provide a live view of customer sentiment.

## Project Structure

- `backend/`: FastAPI application that handles data processing, analysis, and API endpoints.
- `frontend/`: Dash application for the real-time dashboard.
- `ml-models/`: Placeholder Python scripts for machine learning models.
- `data/`: Directory for storing synthetic or real data.
- `infrastructure/`: Configuration files for Prometheus and Grafana.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for running Prometheus and Grafana)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd tmobile-happiness-index
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Copy the `.env.example` to `.env`.
   - Add your API keys for NVIDIA and ElevenLabs to the `.env` file.

### Running the Application

1. **Start the backend server:**
   ```bash
   uvicorn backend.main:app --reload
   ```

2. **Run the database migrations:**
   ```bash
   python backend/database.py
   ```

3. **Start the frontend dashboard:**
   ```bash
   python frontend/app.py
   ```

4. **(Optional) Run Prometheus and Grafana:**
   - Make sure you have Docker installed.
   - Navigate to the `infrastructure` directory.
   - Run `docker-compose up`.

## How it Works

1. **Data Simulation:** The `data_simulator.py` script generates synthetic data representing customer interactions in a T-Mobile store.
2. **Stream Processing:** The `stream_processor.py` orchestrates the analysis of the incoming data.
3. **Sentiment Analysis:**
   - Text sentiment is analyzed using a placeholder for the NVIDIA Nemotron model.
   - Voice sentiment is analyzed using a placeholder for the ElevenLabs API.
   - Emotion from camera feeds is analyzed using a placeholder computer vision model.
4. **Happiness Score Calculation:** A weighted average of the different sentiment scores is calculated to produce a single "happiness score."
5. **Metrics and Monitoring:** Key metrics are exported to Prometheus and can be visualized in a Grafana dashboard.
6. **Dashboard:** A Dash application provides a real-time view of the happiness index, including live metrics, a geographic map of store performance, and an alert panel.
