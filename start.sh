#!/bin/bash

echo "Starting Ollama server..."
# Start Ollama server in background
ollama serve &

# Wait for Ollama to start
sleep 10

echo "Pulling DeepSeek Coder model..."
# Pull DeepSeek Coder model (using 1.3B version for free tier)
ollama pull deepseek-coder:1.3b-base

echo "DeepSeek Coder model loaded!"

echo "Starting Flask API server..."
# Start Flask API
python3 app.py
 
