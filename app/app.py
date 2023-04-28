from flask import Flask, render_template, request
import ipinfo
import os

app = Flask(__name__)

access_token = os.environ['IPINFO_TOKEN']

@app.route('/')
def index():
    
    visitor_details=locate_ip(remove_port(get_client_ip()))

    if location_detail_validator(visitor_details):
        city, region, country, countryname, latitude, longitude = location_detail_extractor(visitor_details)
    else:
        city = 'Unknown city'
        region = 'Unknown region'
        country = 'Unknown country'
        countryname = 'Unknown country name'
        latitude = 'Unknown latitude'
        longitude = 'Unknown longitude'
    
    return render_template('index.html', city=city, region=region, country=country, countryname=countryname, latitude=latitude, longitude=longitude)

def get_client_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        client_ip = request.environ['REMOTE_ADDR']
    else:
        client_ip = request.environ['HTTP_X_FORWARDED_FOR']
    
    return client_ip

def remove_port(ip_address_with_port):
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
    if 'bogon' in detail_dict:
        return False
    else:
        return True

if __name__ == '__main__':
    app.run(debug=True)