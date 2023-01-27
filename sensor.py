import esp32
from machine import Timer

class Sensor:

    data = []
    timer: Timer = Timer(0)

    def __init__(self):
        self.timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:self.getNewSensorValue() )

    def getSensorValues(self):
        return self.data

    def getNewSensorValue(self):
        val = esp32.hall_sensor()
        self.data.append(val)
        if len(self.data) > 300:
            self.data.pop(0)
