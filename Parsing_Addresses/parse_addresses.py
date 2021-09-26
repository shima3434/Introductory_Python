# Names: Shima Abdulla, Luis Alfaro, Samson Joseph

from argparse import ArgumentParser
import re
import sys


def parse_address(text):
    """ This function using a line of text to make a dictionary of the parts of an address in the line. 
    Your only paramenter is a line of text which houses the whole address.
    It would return the dictionary of the parts of the address if the search being successful in finding a match. It it was unsuccessful it would return None"""
    
    expr = re.search(r"^(\S+)\s(.*),\s(.*)\s([A-Z]{2})\s(\d{5})$", text)
    address_dict = {"house_number":expr.group(1), "street":expr.group(2), "city":expr.group(3), "state":expr.group(4), "zip":expr.group(5)}
    return address_dict if expr else None

def parse_addresses(file):
    """ This part almost connects the code to the file and convert each address to the dictionary coded in the previous function.
    Your only paramenter is the file itself. 
    In the end it would return a list of dictionaries """
    
    with open(file, 'r', encoding='utf-8') as f:
        return [parse_address(key) for key in f]
         

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file",
                        help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file):
        print(address)
