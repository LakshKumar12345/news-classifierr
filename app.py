from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import os
import zipfile
import gdown

app = Flask(__name__)

MODEL_DIR = "best_distilbert_news_model"
ZIP_FILE = "best_distilbert_news_model.zip"

classifier = None

THRESHOLD = 0.65

sports_keywords = ["cricket", "football", "match", "world cup", "t20", "ipl", "goal"]


# 🔥 download + extract model (first run only)
def download_model():
    if not os.path.exists(MODEL_DIR):

        url = "https://drive.google.com/uc?id=1Sw7BN2o00jXqyuVzEYWVwUc3kLW8gLHz"


        gdown.download(url, ZIP_FILE, quiet=False)

        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(".")


# 🔥 lazy load model (IMPORTANT for Railway)
def load_model():
    global classifier
    if classifier is None:
        classifier = pipeline(
            "text-classification",
            model=f"./{MODEL_DIR}",
            tokenizer=f"./{MODEL_DIR}"
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    download_model()
    load_model()

    data = request.get_json()
    text = data["text"].lower()

    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    # 🏏 rule-based override
    if any(k in text for k in sports_keywords):
        label = "Sports"
        score = max(score, 0.80)

    # 🧠 confidence check
    if score < THRESHOLD:
        return jsonify({
            "label": "Unclear News",
            "message": "This input does not strongly match any category (World, Sports, Business, Sci/Tech).",
            "confidence": float(score)
        })

    return jsonify({
        "label": label,
        "message": "Prediction based on AG News model (World, Sports, Business, Sci/Tech)",
        "confidence": float(score)
    })


if __name__ == "__main__":
    app.run(debug=True)