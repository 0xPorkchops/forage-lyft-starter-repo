from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear_readings):
        self.tire_wear_readings = tire_wear_readings

    def needs_service(self):
        return sum(self.tire_wear_readings) >= 3.0