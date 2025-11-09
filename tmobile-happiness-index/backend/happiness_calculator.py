from typing import Dict, Any

def calculate_happiness_score(data: Dict[str, Any]) -> float:
    """
    Calculates the overall happiness score based on various inputs.
    Weights can be adjusted based on business priorities.
    """
    weights = {
        "text_sentiment": 0.5,
        "voice_sentiment": 0.3,
        "camera_emotion": 0.2
    }

    text_score = data.get("text_sentiment_score", 0.0) * weights["text_sentiment"]
    voice_score = data.get("voice_sentiment_score", 0.0) * weights["voice_sentiment"]
    camera_score = data.get("camera_emotion_score", 0.0) * weights["camera_emotion"]

    # The combined score is normalized to a 0-100 scale
    # Raw scores are between -1 and 1, so we shift them to 0-2 and then scale by 50
    total_score = (text_score + voice_score + camera_score + 1) * 50

    return max(0, min(100, total_score))  # Ensure the score is within the 0-100 range

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "text_sentiment_score": 0.8,   # Positive text
        "voice_sentiment_score": -0.2, # Slightly negative tone
        "camera_emotion_score": 0.6    # Happy face detected
    }
    score = calculate_happiness_score(sample_data)
    print(f"Calculated Happiness Score: {score:.2f}")
