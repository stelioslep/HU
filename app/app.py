from flask import Flask, render_template, request
import ipinfo
import os

app = Flask(__name__)

access_token = [os.environ.get('IPINFO_TOKEN')]

@app.route('/')
def index():
    visitor_details=locate_ip(get_client_ip())
    return render_template('index.html', visitor_details=visitor_details)

def get_client_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        client_ip = request.environ['REMOTE_ADDR']
    else:
        client_ip = request.environ['HTTP_X_FORWARDED_FOR']
    return client_ip

def locate_ip(client_ip):
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(client_ip)
    return details.all

if __name__ == '__main__':
    app.run(debug=True)