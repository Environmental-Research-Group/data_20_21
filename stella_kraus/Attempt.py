import csv
import re
import matplotlib.pyplot as plt
from csv import writer
from csv import reader

#station = input("Name of Station:")
#monthinput = input("Month #:")

with open('CTA_-_Ridership_-_Bus_Routes_-_Monthly_Day-Type_Averages___Totals.csv', 'r') as read_obj, \
    open('CTA_-_Ridership_-_Bus_Routes_-_Monthly_Day-Type_Averages___Totals.csv', 'w', newline='') as write_obj:
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    
    csv_reader = csv.reader(read_obj, delimiter=',')
    line_count = 1
    f_csv = csv.reader(read_obj) 
    headers = next(f_csv)
    for row in csv_reader:
        x=[]
        y=[]
        DL= row[2].split("/")
        month,day,year = str(DL).split()
        month = re.findall(r"'(.*?)'", month)[0]
        year = re.findall(r"'(.*?)'", year)[0]
        if int(year) == 2020:
            x.append(int(month))
            y.append(float(row[6]))
        diff=y[2]-y[3]
        print(diff)
        # Append the default text in the row / list
        row.append(diff)
        # Add the updated row / list to the output file
        csv_writer.writerow(row) 

        #print(month, day, year)
        #print(row)
        #if station in row and int(year) == 2020:
           # x.append(int(month))
          #  y.append(float(row[6]))
    
            
           # plt.plot(x,y)
           # plt.xlabel('Month')
           # plt.ylabel('Ridership')
           # plt.title('Title')
#with open('CTA_-_Ridership_-_Bus_Routes_-_Monthly_Day-Type_Averages___Totals.csv', 'r') as read_obj, \
        #open('output_1.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    


#plt.show()
                
                
            
        
            

    