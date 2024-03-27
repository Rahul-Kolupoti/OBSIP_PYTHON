import requests

API_KEY = "0e557cd1c9f7e8c40a2bf3f3fd5a0a83"

def get_weather(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    data=response.json()
    return data

city=input("Enter City Name: ")
weather=get_weather(city)
if weather["cod"]==200:
    print("City Name: ",weather["name"])
    print("Temperature: ",weather["main"]["temp"],"°C")
    print("Humidity: ",weather["main"]["humidity"],"%")
    print("Weather Condition: ",weather["weather"][0]["description"])