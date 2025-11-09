import json
import random
from datetime import datetime

def generate_synthetic_data(store_id: int):
    """Generates a single synthetic data point."""
    return {
        "timestamp": datetime.now().isoformat(),
        "store_id": store_id,
        "customer_id": f"cust_{random.randint(1000, 9999)}",
        "text_input": random.choice([
            "I'm really happy with the service!",
            "This is frustrating, my phone isn't working.",
            "Can you help me with my bill?",
            "Just browsing, thanks.",
            "The new store layout is great."
        ]),
        "voice_input_url": f"https://example.com/voice/{random.randint(1, 100)}.wav",
        "camera_feed_url": f"https://example.com/camera/{random.randint(1, 100)}.jpg"
    }

if __name__ == "__main__":
    # Example of generating and printing a few data points
    for i in range(5):
        print(json.dumps(generate_synthetic_data(store_id=101), indent=2))
