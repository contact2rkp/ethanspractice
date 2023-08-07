import csv
from datetime import datetime as dt
year_close = dict()

try:
    with open("C:\\Users\\Raj Kumar\\Documents\\Raj\\python\\ethans\\BSE-BOM504067.csv", 'r') as zensar:
        reader = csv.DictReader(zensar)
        for row in reader:
            year = dt.strptime(row['Date'], '%Y-%m-%d').year

            if year in year_close:
                year_close[year].append(float(row['Close']))
            else:
                year_close[year] = [float(row['Close'])]
except FileNotFoundError as F:
    print('Unable to open the file: ', F)
    exit(1)
except Exception as E:
    print('Exception: ', E)
    exit(2)

for year, close in year_close.items():
    print(year, sum(close) / len(close))