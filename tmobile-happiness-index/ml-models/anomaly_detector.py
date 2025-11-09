from typing import List
import numpy as np

def detect_anomalies(scores: List[float]) -> List[int]:
    """
    Placeholder for an anomaly detection model.
    Detects significant spikes or drops in a time series of happiness scores.
    Returns a list of indices where anomalies were detected.
    """
    # A simple statistical approach: identify points that are more than
    # two standard deviations away from the mean.
    if len(scores) < 10:  # Need enough data to be meaningful
        return []

    mean = np.mean(scores)
    std_dev = np.std(scores)
    anomalies = [
        i for i, score in enumerate(scores)
        if abs(score - mean) > 2 * std_dev
    ]
    return anomalies

if __name__ == "__main__":
    # Example usage
    sample_scores = [85, 88, 86, 90, 87, 89, 52, 91, 88, 86]
    anomalies = detect_anomalies(sample_scores)
    if anomalies:
        print(f"Anomalies detected at indices: {anomalies}")
        for i in anomalies:
            print(f"  - Score: {sample_scores[i]}")
    else:
        print("No anomalies detected.")
