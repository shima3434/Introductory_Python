# Shima Abdulla, Joseph Sanchez, Sydney Small

""" Build a database of energy sources in the US. """

from argparse import ArgumentParser
import sqlite3
import sys


class EnergyDB:
    """
    Creates an sqlite database and reads data from a CSV file 
    
    Attributes:
        conn(str): connection to an in-memory sqlite database
    """
    
    def __init__(self, filename):
        """
        Paramters:
            filename(str): string containing path to a file
            
        Attributes: 
            conn(str): connection to an in-memory sqlite database
        """
        self.conn = sqlite3.connect(':memory:')
        self.read(filename)
        
   
    def __del__(self):
        """ Clean up the database connection. """
        try:
            self.conn.close()
        except:
            pass
        
    def read(self, filename):
        """ Reads and ignores the first line in the file, which contains column headers. 
            Read the other lines in the file; for each of those lines, 
            Converts the year to an integer and the megawatt-hours into a float. 
            Inserts the data from the file into the sql database. 
        
            Parameters:
                        filename(str): string containing path to a file
        """
        cursor = self.conn.cursor()
        production_table = '''CREATE TABLE production
                        (year integer, state text, source text, mwh real)
                            '''
        cursor.execute(production_table)
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f.readlines()[1:]:
                energy_list = line.split(",")
                energy_list[0] = int(energy_list[0])
                energy_list[3] = float(energy_list[3])
                electricity = ''' INSERT INTO production VALUES (?, ?, ?, ?)'''
                cursor.execute(electricity, energy_list)
            self.conn.commit()
    
    def production_by_source(self, source, year):
        """ Creates a Cursor object to the database connection. 
            Gets the value of the mwh column for each row that matches the source and year.
            "Fetches" all the values returned, adds them together, and returns the total.
        
            Parameters:
                        source(string): string from the Source column of energy.csv
            
                        year(int): integer representing a year from energy.csv
        
            Return: 
                    Returns the total of all values of the mwh column for each row that matches the source and year.
        """
        cursor_1 = self.conn.cursor()
        get_mwh = cursor_1.execute('''SELECT mwh FROM production WHERE source=? AND year=?''', (source, year)).fetchall()
        total_values = 0
        for i in get_mwh:
            total_values = total_values + i[0]
        return total_values
        
def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.
    
    Args:
        filename (str): path to a CSV file containing four columns:
            Year, State, Energy Source, Megawatthours.
    
    Side effects:
        Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
       print(f"Total {source_lbl} production in 2017: ",
             e.production_by_source(source_str, 2017))


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
