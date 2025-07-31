from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/check/instagram", methods=["GET"])
def check_instagram():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Kullanıcı adı gerekli"}), 400

    url = "https://instagram120.p.rapidapi.com/api/instagram/profile"
    headers = {
        "X-RapidAPI-Key": "5077c3f5f4msh81956eb53a533aep1af1c7jsn4719cb429064",
        "X-RapidAPI-Host": "instagram120.p.rapidapi.com"
    }
    params = {"username": username}

    response = requests.get(url, headers=headers, params=params)

    try:
        return response.json()
    except Exception:
        return {"error": "Yanıt işlenemedi"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
