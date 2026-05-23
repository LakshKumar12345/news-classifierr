from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import os
import zipfile
import gdown

app = Flask(__name__)

MODEL_DIR = "best_distilbert_news_model"
ZIP_FILE = "model.zip"

classifier = None
THRESHOLD = 0.65

sports_keywords = ["cricket", "football", "match", "world cup", "t20", "ipl", "goal"]


# 🔥 Download + extract model (ONLY ONCE at startup)
def download_model():
    if not os.path.exists(MODEL_DIR):

        url = "https://drive.google.com/uc?id=1Sw7BN2o00jXqyuVzEYWVwUc3kLW8gLHz"

        print("Downloading model from Drive...")

        gdown.download(url, ZIP_FILE, quiet=False)

        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(".")

        print("Model downloaded and extracted successfully.")


# 🔥 Load model (ONLY ONCE)
def load_model():
    global classifier
    if classifier is None:
        print("Loading model...")
        classifier = pipeline(
            "text-classification",
            model=f"./{MODEL_DIR}",
            tokenizer=f"./{MODEL_DIR}"
        )
        print("Model loaded.")


# ✅ INIT ON START (IMPORTANT FOR RAILWAY)
download_model()
load_model()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

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
            "message": "Input does not strongly match any category (World, Sports, Business, Sci/Tech).",
            "confidence": float(score)
        })

    return jsonify({
        "label": label,
        "message": "Prediction based on AG News model",
        "confidence": float(score)
    })


# 🚀 RAILWAY ENTRY POINT
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
