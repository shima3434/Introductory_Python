# Names(Me, Partner): Shima Abdulla, Varun Sharma

""" Find cities near a specified location. """


from argparse import ArgumentParser
import sys

from haversine import haversine

class Cities:
    """ A class to represent the cities this should ideally include the city state and logitude and latitude and determines the closests cities to a point and eventually returns the five closest ones."""
    def __init__(self,filename):
        """ Uses the information from the file to create a dictionary of the cities and their location in terms of longitude, latitude, and the city and state (found by position in line of file). As well as initializes needed variables"""
        self.cities = {}
        
        with open(filename, "r", encoding = "utf-8") as f:
            for line in f:
                line = line.split(",")
                key = tuple(line[0:2])
                lat = float(line[2])
                lon = float(line[3])
                self.cities[key] = lat,lon
                
    def nearest(self, point):
        """ Determined the closest cities from the point uing a lambda and haversine function and the cities dictionary. Returns the five closest cities"""
        city = sorted(self.cities, key = lambda x : haversine(point, self.cities[x]))
        return city[:5]
        

def main(filename, arg1, arg2):
    """ Read city data from a file and find the closest cities to a
    specified location (either an area and city from filename or a
    latitude and longitude which may or may not be in the file).
    
    Args:
        filename (str): path to a file containing city data. Each line
            in the file should consist of four values, separated by
            commas: area (e.g., state or country), city, latitude in
            decimal degrees, longitude in decimal degrees.
        arg1 (str): either the name of an area in the file, or a string
            representation of a latitude.
        arg2 (str): either the name of a city in the file, or a string
            representation of a longitude.
    
    Side effects:
        Writes to stdout.
    """
    cities = Cities(filename)
    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
    except ValueError:
        try:
            point = cities.cities[arg1, arg2]
        except KeyError:
            sys.exit(f"Error: could not look up {arg1}, {arg2}")
    print(f"For {arg1}, {arg2}, the nearest cities from the file are")
    for result in cities.nearest(point):
        print("    " + ", ".join(result))


def parse_args(arglist):
    """ Process command-line arguments and return the parsed values as a
    namespace. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing city data")
    parser.add_argument("arg1",
                        help="a latitude expressed in decimal degrees"
                             " or an area (state, country) from the"
                             " file")
    parser.add_argument("arg2",
                        help="a longitude expressed in decimal degrees"
                             " or a city name from the file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.arg1, args.arg2)
