import csv

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
    a = readfile('1000-largest-us-cities.csv')
    print(a)

    with open('final_weather_data.csv') as csvfile:
        weatherreader = csv.reader(csvfile, delimiter=',')
        for row in weatherreader:
            parsed_data = ', '.join(row)
            item = row[2]

if __name__ == "__main__":
    main()