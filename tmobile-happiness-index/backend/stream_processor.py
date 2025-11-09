import sys
import os

# Add the project root directory to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.nemotron_analyzer import analyze_text_sentiment
from backend.voice_analyzer import analyze_voice_sentiment
from ml_models.camera_emotion import analyze_camera_emotion
from backend.happiness_calculator import calculate_happiness_score
from backend.prometheus_exporter import export_metrics
from backend.database import save_happiness_record

def process_stream_data(data):
    """
    Processes a single data point from the stream.
    """
    # 1. Analyze sentiment from different sources
    data['text_sentiment_score'] = analyze_text_sentiment(data['text_input'])
    data['voice_sentiment_score'] = analyze_voice_sentiment(data['voice_input_url'])
    data['camera_emotion_score'] = analyze_camera_emotion(data['camera_feed_url'])

    # 2. Calculate the overall happiness score
    happiness_score = calculate_happiness_score(data)
    data['happiness_score'] = happiness_score

    # 3. Export metrics to Prometheus
    export_metrics(data['store_id'], happiness_score)

    # 4. Save the results to the database
    save_happiness_record(data)

    return data
