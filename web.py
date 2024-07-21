import requests
def web_correct(url):
    res=requests.get(url)
    if res.status_code==200:
        print(url,"is working")
    else:
        print(url,"is down or not working")
web_correct('https://open-meteo.com/en/docs#current=temperature_2m&daily=weather_code&timezone=Europe%2FMoscow')