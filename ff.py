class Vehicle(object):
    """docstring"""
 
    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
    
    def brake(self):
        """
        Stop the car
        """
        return "Braking"
    
    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"
 