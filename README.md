# 📰 AI-Powered News Classification System (DistilBERT + Flask)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![Transformers](https://img.shields.io/badge/Transformers-DistilBERT-yellow)
![Status](https://img.shields.io/badge/Project-Completed-green)

This project is an AI-based news classification web application built using HuggingFace Transformers (DistilBERT) and Flask.  
It classifies news articles into multiple categories with confidence scoring and handles uncertain inputs using threshold-based logic.

---

## 🚀 Features

- AI-based news classification using DistilBERT  
- Categories: World, Sports, Business, Sci/Tech  
- Confidence threshold for uncertain predictions  
- Rule-based enhancement for Sports detection  
- Keyword-based improvement for Business detection  
- Flask web interface (frontend + API)  
- Automatic model loading from external storage (Google Drive)  

---

## 📂 Project Structure

```text
news-classifier/
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
└── templates/
    └── index.html
```
## ⚙️ Installation & Setup

### 1. Clone Repository
git clone <repo-url>
cd news-classifier

---

### 2. Create Virtual Environment (optional)
python -m venv venv
venv\Scripts\activate   (Windows)

---

### 3. Install Dependencies
pip install -r requirements.txt

---

### 4. Run Application
python app.py

---

### 5. Open in Browser
http://127.0.0.1:5000

---

## 🧠 Model Information

- Model: DistilBERT (fine-tuned for news classification)
- Input: Raw news text
- Output: Predicted category + confidence score

---

## 📸 Screenshots

👉 Add your screenshots in the `screenshots/` folder and rename them like below:

- Home Page → `home.png`
- Prediction Page → `predict.png`
- World News → `world.png`
- Sports News → `sports.png`
- Business News → `business.png`
- Sci/Tech News → `science.png`
- Unclear Input → `unclear.png`

### 🖼️ Then use below format in README:

![Home Page](screenshots/home.png)

![Prediction Page](screenshots/predict.png)

![World News Result](screenshots/world.png)

![Sports News Result](screenshots/sports.png)

![Business News Result](screenshots/business.png)

![Sci/Tech News Result](screenshots/science.png)

![Unclear Input Result](screenshots/unclear.png)

---

## 🏗️ Tech Stack

- Python  
- Flask  
- HuggingFace Transformers  
- PyTorch  
- Google Drive (model storage)  

---

## 🚀 Future Improvements

- Improve model accuracy with fine-tuning  
- Add more categories  
- Deploy on cloud platform  
- Improve UI/UX design  

---

## 👨‍💻 Author

Laksh Kumar
