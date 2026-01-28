from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

OLLAMA_URL = "http://localhost:11434"

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "model": "deepseek-coder"}), 200

@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    """Analyze code for security vulnerabilities"""
    try:
        data = request.json
        code = data.get('code', '')
        
        if not code:
            return jsonify({"error": "No code provided"}), 400
        
        # Prompt for security analysis
        prompt = f"""You are a cybersecurity expert. Analyze the following code for security vulnerabilities, potential exploits, and provide recommendations for improvement.

Code:
```
{code}
```

Provide a detailed security analysis including:
1. Identified vulnerabilities
2. Severity level (Critical/High/Medium/Low)
3. Recommended fixes
4. Best practices to follow
"""
        
        # Call Ollama API
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "deepseek-coder:1.3b-base",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                "analysis": result.get('response', ''),
                "model": "deepseek-coder:1.3b-base"
            }), 200
        else:
            return jsonify({"error": "Model unavailable"}), 503
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timeout - model is processing"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """General chat endpoint for security questions"""
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({"error": "No message provided"}), 400
        
        # Call Ollama API
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "deepseek-coder:1.3b-base",
                "prompt": f"You are a cybersecurity AI assistant. Answer the following question:\n\n{message}",
                "stream": False
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                "response": result.get('response', ''),
                "model": "deepseek-coder:1.3b-base"
            }), 200
        else:
            return jsonify({"error": "Model unavailable"}), 503
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timeout"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/threat-detect', methods=['POST'])
def threat_detect():
    """Detect threats in logs or network traffic"""
    try:
        data = request.json
        logs = data.get('logs', '')
        
        if not logs:
            return jsonify({"error": "No logs provided"}), 400
        
        prompt = f"""You are a threat detection AI. Analyze the following logs for potential security threats, anomalies, or suspicious activities.

Logs:
{logs}

Provide:
1. Detected threats or anomalies
2. Risk level
3. Recommended actions
"""
        
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "deepseek-coder:1.3b-base",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                "analysis": result.get('response', ''),
                "model": "deepseek-coder:1.3b-base"
            }), 200
        else:
            return jsonify({"error": "Model unavailable"}), 503
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
