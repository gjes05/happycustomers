from prometheus_client import Counter, Gauge, start_http_server
import time

# Define Prometheus metrics
HAPPINESS_EVENTS = Counter('happiness_events_total', 'Total number of happiness events processed')
AVERAGE_HAPPINESS_SCORE = Gauge('average_happiness_score', 'Average happiness score across all stores')

def export_metrics(store_id: int, happiness_score: float):
    """Exports metrics to Prometheus."""
    HAPPINESS_EVENTS.inc()
    # In a real application, you'd have a more sophisticated way of calculating the average
    # This is a simplified example
    AVERAGE_HAPPINESS_SCORE.set(happiness_score)

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some random metrics for demonstration
    import random
    while True:
        export_metrics(store_id=101, happiness_score=random.uniform(60, 95))
        time.sleep(5)
