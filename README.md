
# 📈 Stock Price Predictor Web App

This is a simple web application built using **Flask** and a **Machine Learning model** to predict stock closing prices based on user input features like Open, High, Low, and Volume.

<p align="center">
  <img src="https://dummyimage.com/720x600" alt="Demo Screenshot" width="500"/>
</p>

## 🔍 Project Overview

This web app takes user input for stock market values and returns a predicted closing price. It uses a trained machine learning model (`model.pkl`) built during learning exercises and serves predictions through a Flask web server.

### 🧠 Tech Stack
- **Frontend:** HTML, Tailwind CSS
- **Backend:** Python, Flask
- **Model Training:** scikit-learn
- **Deployment Ready:** Yes (Localhost)

---

## 🚀 How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/stock-price-predictor.git
cd stock-price-predictor
````

### 2. Install Required Packages

```bash
pip install flask joblib numpy scikit-learn
```

### 3. Run the Flask App

```bash
python app.py
```

### 4. Open in Browser

Navigate to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📁 Project Structure

```
├── app.py              # Main Flask application
├── utils.py            # Prediction utility using trained ML model
├── model.pkl           # Pre-trained stock prediction model
├── templates/
│   ├── index.html      # Main form page (with Tailblocks design)
│   └── prediction.html # Result display page
├── static/             # (Optional) For images, CSS, JS
└── README.md           # Project documentation
```

---

## 📸 Screenshots

### 📥 Input Page:

![Form Screenshot](https://dummyimage.com/720x600)

### 📤 Prediction Output:

![Prediction Screenshot](https://dummyimage.com/720x200)

---

## 📚 Acknowledgments

This project was inspired by the [**Machine Learning Course for Beginners**](https://www.youtube.com/watch?v=GxZrEKZfW2o) by **Ayush Singh (FreeCodeCamp)**. A big thanks for making ML simple and practical to learn!

---

## 🌟 Features

* Simple and responsive UI (TailwindCSS via Tailblocks)
* Real-time prediction on user input
* Modular code with Flask routes and utils
* Easy to expand for other features (charts, graphs, etc.)

---

## 🙌 Contribute

Have ideas to improve? Fork this repo, make changes, and submit a pull request!

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

> Made with ❤️ by Rosu | Computer Science Student @ VAST

```

---

Would you like me to generate a `requirements.txt` file too for GitHub or help you deploy this app on **Render**, **Vercel**, or **Railway**?
```
