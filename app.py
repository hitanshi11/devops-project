from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello. This app is deployed using DevOps pipeline. \n" \
    "Added docker.yml and now checking if image appears in dockerhub"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)