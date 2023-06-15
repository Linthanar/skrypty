import csv 
import math
# radius of the Earth
R = 6373.0

NR_fly = 0

f = 999999
s = 0

top_5_flights = []
top_5_distance = []

lat1=0
lon1=0
lat2=0
lon2=0
flight_name = ''

with open('flights.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:

        lat1 = math.radians(float(line[3]))
        lon1 = math.radians(float(line[4]))
        lat2 = math.radians(float(line[5]))
        lon2 = math.radians(float(line[6]))
        
        dlon = lon2 - lon1
        # change in coordinates

        dlat = lat2 - lat1

        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        if f > distance:
            f = distance
            flight_name = line[0]
            top_5_flights.append(flight_name)
            top_5_distance.append(distance)
            print(f)
            print(flight_name)

    
print(f)
print(flight_name)

    

# find distances

# find shortest distance 

# print flight airports