# This file takes CSV Annual/Seasonal Climate Normals and turns the last/first frost data into a readable table
# Data can be downloaded from https://www.ncei.noaa.gov/access/search/data-search/normals-annualseasonal-1991-2020

import csv, argparse, re

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="CSV Annual/Seasonal climate normal file from NOAA")
args = parser.parse_args()

print()

with open(args.filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print('Location:', row['NAME'])
        print()
        print('Last Frost Dates (Spring)')
        print('TEMP  90%   80%   70%   60%   50%   40%   30%   20%   10%')
        for temp in ['16','20','24','28','32','36']:
            print(temp+'°F', end =' ')
            for prob in ['90','80','70','60','50','40','30','20','10']:
                key = 'ANN-TMIN-PRBLST-T'+temp+'FP'+prob
                print(row[key].strip(), end =' ')
            print()
        print()
        print('First Frost Dates (Fall)')
        print('TEMP  10%   20%   30%   40%   50%   60%   70%   80%   90%')
        for temp in ['36','32','28','24','20','16']:
            print(temp+'°F', end =' ')
            for prob in ['10','20','30','40','50','60','70','80','90']:
                key = 'ANN-TMIN-PRBFST-T'+temp+'FP'+prob
                print(row[key].strip(), end =' ')
            print()
