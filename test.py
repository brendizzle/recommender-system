import csv
import pandas as pd
import numpy as np

def readfile(filepath):
    cities = []
    with open(filepath) as newfile:
        csvreader = csv.reader(newfile, delimiter=',')
        for city in csvreader:
            parsed_data = ';'.join(city)
            s = parsed_data.split(";")
            #print(s)
            cities.append(s)

    arr = [row[0:3] for row in cities]
    return arr


def main():
    #a = readfile('1000-largest-us-cities.csv')
    #print(a)

    weather = pd.read_csv("final_weather_data.csv")
    num_rows = weather.shape[0]
    num_cols = weather.shape[1]
    k = 5
    print(weather.values[:,4:num_cols])
    print(weather.min(axis=0).values[5:num_cols])
    print(weather.max(axis=0).values[5:num_cols])
    rnge = weather.max(axis=0).values[5:num_cols] - weather.min(axis=0).values[5:num_cols]
    print(rnge)
    s = []
    for i in range(num_cols-5):
        tmp = np.random.uniform(0,rnge[i],k)
        print(tmp)


    print(s)
    #with open('final_weather_data.csv') as csvfile:
        #weatherreader = csv.reader(csvfile, delimiter=',')
        #for row in weatherreader:
            #parsed_data = ', '.join(row)
            #item = row[2]

if __name__ == "__main__":
    main()