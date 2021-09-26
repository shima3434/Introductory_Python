#Names (Me, Partner): Shima Abdulla, Chika Chuka
""" Calculate the price of an order of magnets according to a bulk
pricing scheme. Price is determined by amount of quantity of magnents ordered. If quantity is less than 0 raise a value error. Ultimately this is return an number that represents the final price for the product"""

import sys

def get_cost(quantity):
    if quantity < 0:
        raise ValueError("You must have 0 or more magnents ")
    elif (quantity >= 0 and quantity <= 49):
        price = 0.75 
    elif (quantity >= 50 and quantity <= 99):
        price = 0.72
    elif (quantity >= 100 and quantity <= 999):
        price = 0.70
    else:
        price = 0.67
    return float(price * quantity)


if __name__ == "__main__":
    try:
        magnets = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a number of magnets as a command-line"
                 " argument")
    except ValueError:
        sys.exit("could not convert " + sys.argv[1] + " into an integer")
    print(get_cost(magnets))