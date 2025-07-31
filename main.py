import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

RAPIDAPI_KEY = "5077c3f5f4msh81956eb53a533aep1af1c7jsn4719cb429064"
RAPIDAPI_HOST = "instagram120.p.rapidapi.com"

@app.route("/check/instagram", methods=["GET"])
def check_instagram():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Kullanıcı adı gerekli"}), 400

    url = f"https://{RAPIDAPI_HOST}/api/instagram/profile"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    data = {"username": username}

    try:
        response = requests.post(url, headers=headers, json=data)
        raw = response.json()
        result = raw.get("result", {})

        simplified = {
            "username": result.get("username"),
            "full_name": result.get("full_name"),
            "biography": result.get("biography"),
            "followers": result.get("edge_followed_by", {}).get("count"),
            "following": result.get("edge_follow", {}).get("count"),
            "posts": result.get("edge_owner_to_timeline_media", {}).get("count"),
            "profile_picture": result.get("profile_pic_url_hd")
        }

        return jsonify(simplified)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
