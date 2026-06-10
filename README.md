# 🌍 Air Quality AI Prediction System

## Overview

Air Quality AI Prediction System is a Machine Learning and Web-based application that predicts Air Quality Index (AQI) using environmental pollutant data and real-time air pollution information from the OpenWeather API.

The project helps users monitor air quality, understand pollution levels, receive health recommendations, and explore sustainability practices that contribute to cleaner environments.

---

## Features

### 🤖 AI-Powered AQI Prediction

* Random Forest Regression model trained on air quality data.
* Predicts AQI using pollutant concentrations.

### 📍 Live Location Support

* Uses the user's GPS location.
* Retrieves local air pollution data automatically.

### 🌆 City-Based AQI Prediction

* Search any city.
* Get AQI prediction and air quality category.

### 📊 Analytics Dashboard

* Interactive pollutant charts.
* AQI visualization using Chart.js.
* Real-time pollutant concentration display.

### 🌱 Sustainability Dashboard

* Indoor Air Quality Tips.
* Green Score Calculator.
* Daily Eco Challenges.
* Sustainability Recommendations.

### 🔒 Privacy Focused

* User location is used temporarily to retrieve local air quality data.
* No personal information or location history is stored.

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Random Forest Regressor
* StandardScaler

### APIs

* OpenWeather Geocoding API
* OpenWeather Air Pollution API

### Data Processing

* Pandas
* NumPy
* Joblib

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Feature Selection
4. Feature Scaling
5. Model Training using Random Forest Regression
6. Model Evaluation
7. Deployment using Flask

### Features Used

* PM2.5
* PM10
* NO
* NO2
* NH3
* CO
* SO2
* O3

---

## Project Structure

```text
Air_Quality_AI/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── model/
│   ├── random_forest.pkl
│   └── scaler.pkl
│
├── dataset/
│   └── city_day.csv
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── prediction.html
│   ├── visualization.html
│   └── sustainability.html
│
├── static/
│   ├── css/style.css
│   └── js/chart.js/sustainability.js
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/air-quality-ai.git
cd air-quality-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Sustainability and Ethics

This project follows responsible AI principles:

### Fairness

The model uses environmental pollutant data without discrimination or bias toward any individual or group.

### Transparency

Users are informed about AQI predictions and sustainability recommendations.

### Privacy

Location data is used only to retrieve local air quality information and is not stored.

### Ethical AI

The system is designed solely for environmental awareness and public benefit.

---

## Future Enhancements


* Mobile Application
* Interactive Pollution Heat Maps
* Historical AQI Analysis
* Multi-City Comparison Dashboard
* Weather-Based AQI Insights

---

## Author

Developed as a Machine Learning and Web Development project focused on environmental sustainability and air quality awareness.

