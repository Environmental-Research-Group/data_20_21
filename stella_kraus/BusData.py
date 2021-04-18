import csv


station = input("Name of Station:")

with open('CTA_-_Ridership_-_Bus_Routes_-_Monthly_Day-Type_Averages___Totals.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if station in row:
            print(f'\tStation: {row[1]}, Month Start: {row[2]}, Monthly Total: {row[6]}.')
            
        
            

    