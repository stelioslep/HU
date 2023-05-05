from flask import Flask, render_template, request
import ipinfo
import os
from pyowm import OWM

app = Flask(__name__)

access_token = os.environ['IPINFO_TOKEN']
owm = OWM(os.environ['OWM_TOKEN'])
mgr = owm.weather_manager()

@app.route('/')
def index():
    
    visitor_details=locate_ip(remove_port(get_client_ip()))

    # See location_detail_validator() for more details.
    
    if location_detail_validator(visitor_details):
        city, region, country, countryname, latitude, longitude = location_detail_extractor(visitor_details)
    else:
        city = 'Munich'
        region = 'Bavaria'
        country = 'DE'
        countryname = 'Germany'
        latitude = 'Unknown latitude'
        longitude = 'Unknown longitude'
    
    # Check if we can find the weather for the city. If not, try the region.
    
    try:
        weather_status, humidity, now_temperature, max_temperature, min_temperature  = weather_search(city, countryname)
        location = city
    except:
        weather_status, humidity, now_temperature, max_temperature, min_temperature = weather_search(region, countryname)
        location = region

    now_temperature = round(now_temperature)
    max_temperature = round(max_temperature)
    min_temperature = round(min_temperature)
    
    return render_template('index.html', location=location, country=countryname,  weather_status=weather_status, humidity=humidity, now_temperature=now_temperature, max_temperature=max_temperature, min_temperature=min_temperature, latitude=latitude, longitude=longitude)

def get_client_ip():
    # Get the client ip address even if the app is behind a proxy
    
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        client_ip = request.environ['REMOTE_ADDR']
    else:
        client_ip = request.environ['HTTP_X_FORWARDED_FOR']
    
    return client_ip

def remove_port(ip_address_with_port):
    # get_client_ip() returns the ip address with the port number. We need to remove the port number to use the ipinfo library
    
    parts = ip_address_with_port.split(':')
    ip_address = parts[0]
    return ip_address

def locate_ip(client_ip):
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(client_ip)
    return details.all

def location_detail_extractor(detail_dict):
    city = detail_dict['city']
    region = detail_dict['region']
    country = detail_dict['country']
    countryname = detail_dict['country_name']
    latitude = detail_dict['latitude']
    longitude = detail_dict['longitude']
    return city, region, country, countryname, latitude, longitude

def location_detail_validator(detail_dict):
    # Local & other invalid ip addresses return a 'bogon' key in the dictionary. If the location is invalid, we will use Munich as the default location.
    
    if 'bogon' in detail_dict:
        return False
    else:
        return True

def weather_search(location, country):
    observation = mgr.weather_at_place(f'{location},{country}')
    w = observation.weather

    weather_status = w.detailed_status         # 'clouds'
    wind_dict = w.wind()                  # {'speed': 4.6, 'deg': 330}
    humidity = w.humidity                # 87
    temperature = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    rain = w.rain                    # {}
    #w.heat_index              # None
    #w.clouds                  # 75
    humidity = humidity
    now_temperature = temperature['temp'] 
    max_temperature = temperature['temp_max']
    min_temperature = temperature['temp_min']

    return weather_status, humidity, now_temperature, max_temperature, min_temperature

if __name__ == '__main__':
    app.run()