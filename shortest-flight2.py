import csv 
import math

# NR_fly = 0

# f = 999999
# s = 0

# top_5_flights = []
# top_5_distance = []

# flight_name = ''


# function definition
def haversine(dep_lat,dep_lng,arr_lat,arr_lng):
    # radius of the Earth
    R = 6373.0

    lat1 = math.radians(float(dep_lat))
    lon1 = math.radians(float(dep_lng))
    lat2 = math.radians(float(arr_lat))
    lon2 = math.radians(float(arr_lng))
    
    dlon = lon2 - lon1
    # change in coordinates

    dlat = lat2 - lat1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Function returns the value 
    return R * c


with open('flights-short.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:

        # decomposition variable into tuple so we can access all data fields from the line:
        (city_pair,dep_code,arr_code,dep_lat,dep_lng,arr_lat,arr_lng) = line

        print('flight: '+ city_pair + ' distance: ' + str(haversine(dep_lat,dep_lng,arr_lat,arr_lng)))


    
    
    




#         if f > distance:
#             f = distance
#             flight_name = line[0]
#             top_5_flights.append(flight_name)
#             top_5_distance.append(distance)
#             print(f)
#             print(flight_name)

    
# print(f)
# print(flight_name)

    

# find distances

# find shortest distance 

# print flight airports