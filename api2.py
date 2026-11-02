import requests
import os
from datetime import datetime
#What is environment file , why it is used , how it is used.
#install dotenv to fecth the secrets /keys from .env :-pip install python-dotenv
#donot push the .env (environment variable) as it has secret key passwords otherwise the other person can take it .
#we can automatically push the (.env) using (.gitignore).
#there is a tool that is specifically used to store the secret  "Vault".
from dotenv import load_dotenv
load_dotenv()
# base_url = "https://api.openweathermap.org/data/2.5/weather"
# city="Delhi"
# api_key=os.getenv("OPENWEATHER_API_KEY")

# params={
#     "q":city,
#     "appid":api_key,
#     "units":"metric"
# }
# response=requests.get(base_url,params=params)
# # print(response.json())




#WAP a program for openweather API write a function city as a argument return temp(in celcius),humidity,sunset_time.


def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key=os.getenv("OPENWEATHER_API_KEY")

    params={
        "q":city,
        "appid":api_key,
        "units":"metric"
    }
    response=requests.get(base_url,params=params)
    data=response.json()
    status_code=response.status_code
    if status_code==200:
      temp=data["main"]["temp"]
      temp=data["main"]["temp"]
      hum=data["main"]["humidity"]
      sun_set=data["sys"]["sunset"]
      sun_set_f=datetime.fromtimestamp(sun_set).strftime("%I: %M %p")
      return f" Temp of city {data["name"]} is {temp} and humdity:{hum} and sun set time : {sun_set_f}"
    elif status_code==401:
       return "Unauthorized"
    else:
       return "Unknown error"

       
print(get_weather("Mumbai"))


#WAP a function it take 2 inputs  1 is source currency and another one is target currency return converted currency and  be the API used is free.

def convert(amoount,source,target):
   api_key=os.getenv("EXCHANGE_RATE_API_KEY")
   if not api_key:
      raise RuntimeError("EXCHANGE_RATE_API_KEY is not set")
   base_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
   response=requests.get(base_url)
   data=response.json()
   print(data)
   rate = data["conversion_rates"][target.upper()]
   return amount * rate

amount=int(input("The amount"))
source=input("Enter the source currency")
target=input("Enter the target currency")
print(convert(amount,source,target)) 
