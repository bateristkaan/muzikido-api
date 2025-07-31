from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Merhaba, muzikido-api çalışıyor!"

@app.route("/check/<username>")
def check(username):
    try:
        url = f"https://www.instagram.com/{username}/"
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

        res = requests.get(url, headers=headers)

        if res.status_code != 200:
            return jsonify({"error": "Kullanıcı bulunamadı"}), 404

        soup = BeautifulSoup(res.text, "html.parser")
        meta = soup.find("meta", property="og:description")

        if not meta:
            return jsonify({"error": "Profil açıklaması bulunamadı"}), 500

        description = meta["content"]
        return jsonify({
            "username": username,
            "info": description
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
