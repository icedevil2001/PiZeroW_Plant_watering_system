
## https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc
##  https://gist.github.com/benrules2/6f490f3a0e082ae6592a630bd7abe588

## https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d

# https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/

# http://mattrichardson.com/Raspberry-Pi-Flask/

## Refresh auto page
## https://stackoverflow.com/questions/40963401/flask-dynamic-data-update-without-reload-page 

####
###  Reading live sensor
### https://stackoverflow.com/questions/62333250/trying-to-get-realtime-sensor-data-from-python-into-html-using-flask-and-jquery 
####

### loggin ###
## https://www.raspberrypi.org/forums/viewtopic.php?t=289151 
########


from flask import Flask, render_template, redirect, url_for, request, jsonify
from datetime import datetime
import json
from pkg_resources import yield_lines

from plotly.subplots import _subplot_type_for_trace_type
from plotting import dash_application
from time import sleep

from Sensor import sensor, autofeeder

# import RPi.GPIO as GPIO
GPIO = 21

from flask.signals import template_rendered 
print(datetime.now().strftime("%Y-%m-%d %H:%M:%s"))

## Measure sensor
## Water 
    # for X sec
## Calibration

################
#   database   #
################
## Soil moisture
    # date, soil moisture 
## Feeding db
    # date, soil moisture before, after, water duration

app  = Flask(__name__)
dash_application(app)

def load_config():
    with open("config/config.json", "r") as js:
        return json.load(js)

def write_config(data):
    with open("config/config.json", "w") as js:
        return json.dump(data,js)

@app.route('/')
def index():
    #return 'Hello World!'
    config_values =  load_config()
    print(config_values)
    return render_template('index.html', title='main page', today=str(datetime.today()), **config_values)


@app.route('/config', methods=['POST'])
def configuration():
    ## Update config file 
    write_config(request.form.to_dict())
    return redirect(url_for("index"))

@app.route('/calibration/<state>')
def calibration(state):
    pass

@app.route('/sensor_calibartion', methods=['GET', 'POST'])
def sensor_calibration(sensor, duration ):
    return jsonify({
        'sensor': sensor
    })


@app.route('/calibration/dry')
def calibration_dry_page():
    sensor_calibration(GPIO)
    pass


@app.route('/calibration/wet')
def calibration_wet_page():
    pass

 

###################################
##     -- dynamic update --      ##
###################################
@app.route('/update2')
def update2():
    return render_template('update.html')

@app.route("/update", methods=["GET", "POST"])
def update():
    now = datetime.now()
    return jsonify({
        "time": datetime.now().strftime("%H:%M:%S")
    })
######################################

# app.route('/sensor')
# def read_sensor():
#     pass

# app.route('/water/<toggle>')
# def water():
#     pass

# app.route('/calibration')
# def calibrate():
#     pass 
#     ## calibrated dry
#     ## calibrated wet 


if __name__ == '__main__':
   app.run(debug=True)




