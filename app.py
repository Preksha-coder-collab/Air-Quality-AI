from flask import Flask, render_template, request
import requests
import joblib

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("model/random_forest.pkl")
scaler = joblib.load("model/scaler.pkl")


API_KEY = "OpenWeather API Key"


# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():
    return render_template('index.html')


# =========================
# ABOUT PAGE
# =========================

@app.route('/about')
def about():
    return render_template('about.html')


# =========================
# VISUALIZATION PAGE
# =========================

@app.route('/visualization')
def visualization():

    return render_template(
        'visualization.html',
        location=None,
        aqi=None,
        category=None,
        pm25=None,
        pm10=None,
        no=None,
        no2=None,
        nh3=None,
        co=None,
        so2=None,
        o3=None
    )


# =========================
# PREDICTION PAGE
# =========================

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


# =========================
# GET CITY COORDINATES
# =========================

def get_coordinates(city):

    url = (
        f"https://api.openweathermap.org/geo/1.0/direct"
        f"?q={city}&limit=5&appid={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    print("Searching for:", city)
    print("Response:", data)

    if not data:
        return None

    return (
        data[0]["lat"],
        data[0]["lon"]
    )


# =========================
# GET AIR POLLUTION DATA
# =========================

def get_pollution_data(lat, lon):

    url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    print("Pollution API Response:", data)

    return data["list"][0]["components"]


# =========================
# CITY AQI PREDICTION
# =========================

@app.route('/predict_city', methods=['POST'])
def predict_city():

    try:

        city = request.form['city']

        print("User Entered City:", city)

        coordinates = get_coordinates(city)

        if coordinates is None:

            return render_template(
                'prediction.html',
                error="City not found."
            )

        lat, lon = coordinates

        pollution = get_pollution_data(lat, lon)

        pm25 = pollution.get("pm2_5", 0)
        pm10 = pollution.get("pm10", 0)
        no = pollution.get("no", 0)
        no2 = pollution.get("no2", 0)
        nh3 = pollution.get("nh3", 0)
        co = pollution.get("co", 0)
        so2 = pollution.get("so2", 0)
        o3 = pollution.get("o3", 0)

        features = [[
            pm25,
            pm10,
            no,
            no2,
            nh3,
            co,
            so2,
            o3
        ]]

        print("Features:", features)

        features_scaled = scaler.transform(features)

        predicted_aqi = model.predict(
            features_scaled
        )[0]

        # AQI Category

        if predicted_aqi <= 50:
            category = "Air Quality is Good and Healthy"

        elif predicted_aqi <= 100:
            category = "Air Quality is Satisfactory"

        elif predicted_aqi <= 200:
            category = "Air Quality is Moderate."

        elif predicted_aqi <= 300:
            category = "Air Quality is Poor."

        elif predicted_aqi <= 400:
            category = "Air Quality is Very Poor."

        else:
            category = "Air Quality is Severe."

        # Health Advice

        if predicted_aqi <= 50:
            advice = "Air quality is good. Enjoy outdoor activities."

        elif predicted_aqi <= 100:
            advice = "Air quality is acceptable for most people."

        elif predicted_aqi <= 200:
            advice = "Sensitive groups should limit prolonged outdoor exposure."

        elif predicted_aqi <= 300:
            advice = "Reduce outdoor activities and wear a mask if needed."

        elif predicted_aqi <= 400:
            advice = "Avoid prolonged outdoor exposure."

        else:
            advice = "Stay indoors. Air quality is hazardous."

        # Tomorrow AQI Forecast
        tomorrow_aqi = round(predicted_aqi * 1.05, 2)

        if tomorrow_aqi <= 50:
            tomorrow_category = "Good"

        elif tomorrow_aqi <= 100:
            tomorrow_category = "Satisfactory"

        elif tomorrow_aqi <= 200:
            tomorrow_category = "Moderate"

        elif tomorrow_aqi <= 300:
            tomorrow_category = "Poor"

        elif tomorrow_aqi <= 400:
            tomorrow_category = "Very Poor"

        else:
            tomorrow_category = "Severe"

        return render_template(
            'prediction.html',
            city=city,
            prediction=round(predicted_aqi, 2),
            category=category,
            advice=advice,
            tomorrow_aqi=tomorrow_aqi,
            tomorrow_category=tomorrow_category
        )

    except Exception as e:

        print("ERROR:", e)

        return render_template(
            'prediction.html',
            error=str(e)
        )
# =========================
# GET LOCATION NAME
# =========================


def get_location_name(lat, lon):

    try:

        url = (
            "https://api.openweathermap.org/geo/1.0/reverse"
            f"?lat={lat}"
            f"&lon={lon}"
            f"&limit=1"
            f"&appid={API_KEY}"
        )

        response = requests.get(url)

        data = response.json()

        if len(data) == 0:
            return "Unknown Location"

        city = data[0].get("name", "Unknown City")
        state = data[0].get("state", "")

        if state:
            return f"{city}, {state}"

        return city

    except Exception as e:

        print("Location Error:", e)

        return "Unknown Location"
    
@app.route('/live_dashboard')
def live_dashboard():

    try:

        lat = request.args.get('lat')
        lon = request.args.get('lon')
        if not lat or not lon:
           return render_template(
             'visualization.html',
             error="Location not received."
    )

        pollution = get_pollution_data(lat, lon)

        pm25 = pollution.get("pm2_5", 0)
        pm10 = pollution.get("pm10", 0)
        no = pollution.get("no", 0)
        no2 = pollution.get("no2", 0)
        nh3 = pollution.get("nh3", 0)
        co = pollution.get("co", 0)
        so2 = pollution.get("so2", 0)
        o3 = pollution.get("o3", 0)

        features = [[
            pm25,
            pm10,
            no,
            no2,
            nh3,
            co,
            so2,
            o3
        ]]

        features_scaled = scaler.transform(features)

        predicted_aqi = model.predict(
            features_scaled
        )[0]

        if predicted_aqi <= 50:
            category = "Good"

        elif predicted_aqi <= 100:
            category = "Satisfactory"

        elif predicted_aqi <= 200:
            category = "Moderate"

        elif predicted_aqi <= 300:
            category = "Poor"

        elif predicted_aqi <= 400:
            category = "Very Poor"

        else:
            category = "Severe"

        location_name = get_location_name(lat, lon)

        return render_template(
             'visualization.html',

            location=location_name,

              aqi=round(predicted_aqi, 2),

            category=category,

            pm25=round(pm25, 2),
            pm10=round(pm10, 2),
            no=round(no, 2),
            no2=round(no2, 2),
            nh3=round(nh3, 2),
            co=round(co, 2),
            so2=round(so2, 2),
            o3=round(o3, 2)
        )

    except Exception as e:

        return render_template(
            'visualization.html',
            error=str(e)
        )
@app.route('/predict_location')
def predict_location():

    try:

        lat = request.args.get('lat')
        lon = request.args.get('lon')

        if not lat or not lon:
            return render_template(
                'prediction.html',
                error="Location not received."
            )

        pollution = get_pollution_data(lat, lon)

        pm25 = pollution.get("pm2_5", 0)
        pm10 = pollution.get("pm10", 0)
        no = pollution.get("no", 0)
        no2 = pollution.get("no2", 0)
        nh3 = pollution.get("nh3", 0)
        co = pollution.get("co", 0)
        so2 = pollution.get("so2", 0)
        o3 = pollution.get("o3", 0)

        features = [[
            pm25,
            pm10,
            no,
            no2,
            nh3,
            co,
            so2,
            o3
        ]]

        features_scaled = scaler.transform(features)

        predicted_aqi = model.predict(
            features_scaled
        )[0]

        if predicted_aqi <= 50:
            category = "Air Quality is Good and Healthy"
            advice = "Air quality is good. Enjoy outdoor activities."

        elif predicted_aqi <= 100:
            category = "Air Quality is Satisfactory"
            advice = "Air quality is acceptable for most people."

        elif predicted_aqi <= 200:
            category = "Air Quality is Moderate."
            advice = "Sensitive groups should limit prolonged outdoor exposure."

        elif predicted_aqi <= 300:
            category = "Air Quality is Poor."
            advice = "Reduce outdoor activities and wear a mask if needed."

        elif predicted_aqi <= 400:
            category = "Air Quality is Very Poor."
            advice = "Avoid prolonged outdoor exposure."

        else:
            category = "Air Quality is Severe."
            advice = "Stay indoors. Air quality is hazardous."

        location_name = get_location_name(lat, lon)

         # Tomorrow AQI Forecast
        tomorrow_aqi = round(predicted_aqi * 1.05, 2)

        if tomorrow_aqi <= 50:
            tomorrow_category = "Good"

        elif tomorrow_aqi <= 100:
            tomorrow_category = "Satisfactory"

        elif tomorrow_aqi <= 200:
            tomorrow_category = "Moderate"

        elif tomorrow_aqi <= 300:
            tomorrow_category = "Poor"

        elif tomorrow_aqi <= 400:
            tomorrow_category = "Very Poor"

        else:
            tomorrow_category = "Severe"

        return render_template(
        'prediction.html',
         city=location_name,
         prediction=round(predicted_aqi, 2),
         category=category,
         advice=advice,
         tomorrow_aqi=tomorrow_aqi,
         tomorrow_category=tomorrow_category
        )

    except Exception as e:

        return render_template(
            'prediction.html',
            error=str(e)
        )
# =========================
# SUSTAINABILITY PAGE
# =========================

@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html')
# =========================
# RUN APP
# =========================

if __name__ == '__main__':
    app.run(debug=True)