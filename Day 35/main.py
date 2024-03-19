import requests
from twilio.rest import Client

account_sid = 'ACb8124b75e1ae364b66cae008f1912442'
auth_token = 'cf3ed932f63d605bcf5c5ac065b3c619'


parameters = {"lat": 29.760427,
              "lon": -95.369804,
              "appid": "8065eb80a7416957b3c5380794a8b8ac"
              }

will_rain =False


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()
# print(data["list"][0]["weather"][0]["description"])
condition_data = data["list"][:5]
for weather_per_3hrs in condition_data:
    weather_data = weather_per_3hrs["weather"][0]["id"]
    if weather_data > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= "its gonna rain today ",
        from_='+12165323657',
        to='+918168713178'
    )

    print(message.status)
