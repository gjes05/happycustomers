# --- data_listener.py ---
# (Run this in a *separate* terminal from your simulator)

import requests
import json
import time

# The address of your simulator's web server
SIMULATOR_URL = "http://localhost:8000"

def fetch_latest_data():
    """Fetches the latest batch of events from the simulator."""
    try:
        # Make a request to the server
        response = requests.get(SIMULATOR_URL)
        
        # If the request was successful (status code 200)
        if response.status_code == 200:
            events = response.json() # Parse the JSON response
            return events
        else:
            print(f"Error: Server returned status code {response.status_code}")
            return None

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the simulator.")
        print("Is simulator.py running?")
        return None
    except json.JSONDecodeError:
        print("Error: Received invalid JSON from the server.")
        return None

def main():
    print("--- 🚀 Real-Time Data Listener START ---")
    print(f"Polling {SIMULATOR_URL} every 5 seconds...")
    print("Press Ctrl+C to stop.\n")
    
    try:
        while True:
            events = fetch_latest_data()
            
            if events:
                print(f"--- Received {len(events)} new events at {time.strftime('%H:%M:%S')} ---")
                
                # Now you can do anything you want with the data.
                # For this example, we'll just print them.
                for event in events:
                    print(json.dumps(event, indent=2))
                print("-" * 30 + "\n")

            # Wait for the next tick
            time.sleep(5) 
            
    except KeyboardInterrupt:
        print("\n--- 🛑 Listener Stopped ---")

if __name__ == "__main__":
    main()