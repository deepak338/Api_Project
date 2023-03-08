import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"  # end point
app_key = 'b35d5b022bffa533d164e188fc9292af'

weather_parameter = {
    "lat": 20.593683,
    "lon": 78.962883,
    "appid": app_key,
    "exculde": "current,minutely,daily",
}

reponse = requests.get(OWM_Endpoint, params=weather_parameter)
reponse.raise_for_status()
weather_data = reponse.json()
weather_condition =(weather_data["weather"][0]['id'])
print(weather_condition)

if id<700:
    print("take your umbrella with you")
