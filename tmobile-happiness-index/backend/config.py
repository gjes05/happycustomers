import os

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./test.db")

# ElevenLabs API Key
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# NVIDIA API Key
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY")
