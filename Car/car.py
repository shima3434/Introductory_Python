# Names(Me, Partner): Shima Abdulla, Varun Sharma
class Car:
    def __init__(self):
        """Initializes the x and Y coordinates and the direction on is heading in. """
        self.x = 0
        self.y = 0
        self.heading = "n"
        
    def turn(self, direction):
        """ Uses direction (right/left)  and initial heading to determine which way the car is heading
        Args: direction. direction helps determine if the car is heading left or right
        """
        if (self.heading == "n"  and direction == "r"):
            self.heading = "e"
        elif (self.heading == "n"  and direction == "l"):
            self.heading = "w"
        elif (self.heading == "s"  and direction == "r"):
            self.heading = "e"
        elif (self.heading == "s"  and direction == "l"):
            self.heading = "w"
        elif (self.heading == "e"  and direction == "l"):
            self.heading = "n"
        elif (self.heading == "e"  and direction == "r"):
            self.heading = "s"
        elif (self.heading == "w"  and direction == "l"):
            self.heading = "s"
        elif (self.heading == "w"  and direction == "r"):
            self.heading = "n"
                    
    def drive(self, distance = 1):
        """Determine the distance the car has travelled 
        Args: Distance: interger value which representsthe vale of the distance traveled
        """
        if self.heading == "e":
            self.x += distance
        elif self.heading == "w":
            self.x -= distance
        elif self.heading == "n":
            self.y += distance 
        elif self.heading == "s":
            self.y -= distance 
            
    def status(self):
        """ Displays the heading and the coordinate
        Returns: X,Y coordinate of where the car is and in which direction the car is heading.
        """
        print(f"Coordinate: ({self.x},{self.y})")
        print(f"Heading: {self.heading}")
    