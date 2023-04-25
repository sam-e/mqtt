"""
Class for sensor data
"""

class SensorDATA:

    def __init__(self):
        self.mqtt_msg = ''
        self.parsed_msg = ''
        self.temp = ''
        self.ph = ''
            
    def parse_temp(self, data):
       self.temp = data.decode()
    
    def parse_ph(self, data):
       self.ph = data.decode() 
    
    def get_temp(self):
        return self.temp
    
    def get_ph(self):
        return self.ph
    
    def get_light(self):
        return self.light