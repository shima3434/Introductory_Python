""" Convert times from 24-hour format to 12-hour format with times of day. """
#Names(Me, Partner): Shima Abdulla, Varun Sharma

from argparse import ArgumentParser
import sys


def convert_times(hours):
    """Function takes in a list of hours in 24hr formate and converts it into 12hr format. It them returns the 12hr format with the time of day"""
    result =[]
    for x in hours:
        if x == 0:
            result.append(f"{x+12} midnight")
        elif (x >=1 and x <= 11):
            result.append(f"{x} in the morning")    
        elif x == 12:
            result.append( f"{x} noon")
        elif (x >=13 and x <= 16):
            result.append(f"{x-12} in the afternoon")
        elif (x >= 17 and x <= 20):
            result.append(f"{x-12} in the evening") 
        elif (x >= 21 and x <= 24):
            result.append(f"{x-12} at night")
    return result

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("hours", nargs="+", type=int, choices=range(0, 24),
                        help="hours to convert")
    args = parser.parse_args(sys.argv[1:])
    converted = convert_times(args.hours)
    assert len(converted) == len(args.hours), \
        "return value of convert_times() contains the wrong number of items"
    for original, conv in zip(args.hours, converted):
        print(f"{original} in 24-hour time is {conv}")