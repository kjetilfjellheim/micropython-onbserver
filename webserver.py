import json
import network
from microdot import Microdot, Response, send_file
from sensor import Sensor
from props import Properties

app = Microdot()
sensor = Sensor()

class Webserver:

    properties = None

    def __init__(self, properties: Properties) -> None:
        self.properties = properties
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(properties.getSsid(), properties.getPassword())
        while wifi.isconnected() is False:
            pass
        print(wifi.ifconfig())
        app.run(port="80")

@app.route('/', methods=['GET'])
def indexRoute(request):
    return send_file("/index.html")

@app.route('/data', methods=['GET'])
def dataRoute(request):
    response = Response(json.dumps(sensor.getSensorValues()))
    return response

@app.route('/chart.js', methods=['GET'])
def staticChartjs(request):
    return send_file("/chart.js")
