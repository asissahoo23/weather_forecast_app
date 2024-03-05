from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
api_key = "4cfe2c7d49f3bb997b0fdb4b6e5dd665"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city']
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        weather_data = None
        city = None
        if response.status_code == 200:
            x = response.json()
            city = city_name
            weather_data = {
                'temperature': x['main']['temp'],
                'pressure': x['main']['pressure'],
                'humidity': x['main']['humidity'],
                'description': x['weather'][0]['description']
            }
        else:
            city = "City Not Found"
        return render_template('index.html', weather_data=weather_data, city=city)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
