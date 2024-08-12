from flask import Flask, jsonify
from utility import SocialMediaUtil

app = Flask(__name__)


@app.route("/")
def social_network_activity():
    social_media = SocialMediaUtil()
    res = social_media.social_media_thread()
    json_response = jsonify(res)
    return json_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
