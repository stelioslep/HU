# Flask Weather App

This is a simple Flask web application that provides weather information for the user's location. The app uses the OpenWeatherMap API to fetch the current weather data and display it to the user, as well as the IPInfo API to locate users based on their public IP.

## Installation

There is no need to do this unless you intend to modify this project in order to repurpose it for one of your own. You can find a live version of it at `https://lepweather.com`.
The version found there is a deployed version of this repository in an Azure Web App. 

1. Clone the repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`. Probably best if this is done in a virtual environment.
3. Replace the `OWM_TOKEN` and `IPINFO_TOKEN` values with your own API keys for OpenWeatherMap and IPInfo respectively. The app will work under the free pricing tiers of both.

## Usage

### Local Version

1. Start the app by running `python app.py`.
2. Navigate to `http://localhost:5000/` in your web browser.
3. The current weather data for Munich, Germany will be displayed on the page. Information regarding your location based on your public IP would require additional logic and
additional IPINfo API calls during testing which are not desired. To get information on your current location (or any other), you would have to swap the values for `region`, 
`city`, and `country` in the "else" under the index function in `app.py`


### Web Version

1. Simply visit `https://lepweather.com` from a desktop web browser of choice. 

As a lot of the styling of the website is a based on a blend of [borrowed](https://codepen.io/antoniasymeonidou/pen/BawKMqg "Thank you for the beautiful clouds!") or simply extremely basic code, just there to make the information the APIs give prettier, it has **not** been optimised.

There may be issues when the page is visited from devices with a low screen resolution, as well as most mobile aspect ratios. As of right now, further refinements on the site
may happen when I feel like it, but are not planned or a priority.

## Credits

This app was created by Stelios Lepouras as a personal project.

The app uses the following packages:

- Flask
- pyOWM
- IPInfo
- All packages the above depend on, as shown on the project's requirements.txt

The weather data is provided by the OpenWeatherMap API.
The user is located via the IPInfo API, based on their IP.

## Skills showcased

This project intends to demonstrate my skills in python development, API consumption, as well as some basic user interface design. I used Flask to create a dynamic web app that
displays real-time weather data from the OpenWeatherMap API, while also locating the user with the IPInfo API. I learned how to make HTTP requests, parse JSON responses, and
handle errors. Additionally, I was introduced to designing a basic interface using HTML, CSS, and JavaScript. Once everything was set up, I hosted my app on Azure, making it
available for anyone on the internet to view.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
