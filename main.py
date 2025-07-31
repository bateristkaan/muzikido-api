import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST", "instagram120.p.rapidapi.com")

@app.route("/")
def home():
    return "Merhaba, muzikido-api çalışıyor!"

@app.route("/check/instagram", methods=["GET"])
def check_instagram():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "username parametresi gerekli"}), 400

    url = f"https://{RAPIDAPI_HOST}/api/instagram/profile"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    payload = {"username": username}

    try:
        response = requests.post(url, json=payload, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
