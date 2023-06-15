import math

# radius of the Earth
R = 6373.0

# coordinates
# rondo
lat1 = math.radians(50.26466564569832)
lon1 = math.radians(19.02344687766619)

# park
lat2 = math.radians(50.27435514231501)
lon2 = math.radians(18.98361692607257)

dlon = lon2 - lon1
# change in coordinates

dlat = lat2 - lat1

# Haversine formula
a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = R * c

print(distance)
