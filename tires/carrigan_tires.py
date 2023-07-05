from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear_readings):
        self.tire_wear_readings = tire_wear_readings

    def needs_service(self):
        return any(reading > 0.9 for reading in self.tire_wear_readings)