# Names(Me, Partner): Shima Abdulla, Sean Delaney
class Appointment:
    def __init__(self, name, start, end):
        """Initializes the name, end,and start. """
        self.name = name
        self.end =  end
        self.start = start
        
    def overlaps(self, other):
        """ Checks for overlaps by using the start and end times using another appointment onject named other. Returns a boolean of true or false depending on the overlap."""
        if self.start <= other.start < self.end:
            return True
        elif self.start <= other.end < self.end:
            return True
        else:
            return False

    
 
    
    
