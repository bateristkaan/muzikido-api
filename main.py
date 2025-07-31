import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

RAPIDAPI_KEY = "5077c3f5f4msh81956eb53a533aep1af1c7jsn4719cb429064"  # kendi key'in
RAPIDAPI_HOST = "instagram120.p.rapidapi.com"

@app.route("/check/instagram")
def check_instagram():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Kullanıcı adı gerekli"}), 400

    url = f"https://{RAPIDAPI_HOST}/api/instagram/profile"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    params = {"username": username}

    try:
        response = requests.get(url, headers=headers, params=params)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

