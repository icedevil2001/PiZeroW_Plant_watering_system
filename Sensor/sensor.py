
import threading
from time import sleep
running = False # to control loop in thread
value = 0

GPIO = ''

class Sensor:
    def __init__(self, pin_moisture, pin_reply):
        self.p_moisture = pin_moisture
        self.p_relay = pin_reply

    def moisture(self):
        reading = 'moisture reads'
        return reading
    
    def relay_on(self):
        relay_start = 'relay pin on HIGH'
        return 

    def relay_off(self):
        relay_start = 'relay pin on LOW'
        return 

def autofeeder(sensor, duration_sec, delay_hr, min_soil_moisture):
    global running
    
    def feed(duration_sec):
        sensor.relay_on()
        for _ in range(duration_sec):
            pass
        sensor.relay_off()
        return 
    print("Started autofeeding")  
    while running:
        if sensor <= min_soil_moisture:
            feed(duration_sec)
            sleep(10 * 60) ## sleep for 10mins 
        else:
            sleep(delay_hr * 60 * 60)
    print('Ended autofeeding')

        


def rpi_function():
    global value

    print('start of thread')
    while running: # global variable to stop loop  
        value += 1
        time.sleep(1)
    print('stop of thread')


# @app.route('/')
# @app.route('/<device>/<action>')
# def index(device=None, action=None):
#     global running
#     global value

#     if device:
#         if action == 'on':
#             if not running:
#                 print('start')
#                 running = True
#                 threading.Thread(target=rpi_function).start()
#             else:
#                 print('already running')
#         elif action == 'off':
#             if running:
#                 print('stop')
#                 running = False  # it should stop thread
#             else:
#                 print('not running')

#     return render_template_string('''<!DOCTYPE html>