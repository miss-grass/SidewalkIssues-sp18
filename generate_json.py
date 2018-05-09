import json
import numpy as np
from numpy import math

mode = 'campus'
delta = 500
distance_threshold = 700


final_lat = 0
final_long = 0

uw_lat = 47.6498128
uw_long = -122.3037817

downtown_lat = 47.611203
downtown_long = -122.338754

if mode == 'dt':
    final_lat = downtown_lat
    final_long = downtown_long
elif mode == 'campus':
    final_lat = uw_lat
    final_long = uw_long


def m_to_lat(m):
    return 1.0 / 110540 * m


def m_to_long(m, lat):
    return -1.0 / (111320 * math.cos(lat)) * m


def color_index(s, n):
    # exist severe --> 4
    if s > 0:
        return 4
    # 0 --> 0
    if n == 0:
        return 0
    # 0-3 --> 1
    elif n <= 3:
        return 1
    # 3-5 --> 2
    elif n <= 5:
        return 2
    # 5-8 --> 3
    elif n <= 8:
        return 3
    # >8 --> 4
    else:
        return 4


data = np.load('google_final_output/output_0-4800.npy')
# data = np.load('acc_final_output/output_0-4800.npy')
bfX = m_to_lat(delta)
bfY = m_to_long(delta, final_lat)
x1 = final_lat - bfX
x2 = final_lat + bfX
y1 = final_long - bfY
y2 = final_long + bfY

# all routes found in the area and indicator to tell the situation of the route
routes = []
inds = []
for route in data:
    if float(route[6]) <= distance_threshold:
        x = float(route[0].split(',')[0])
        y = float(route[0].split(',')[1])
        xE = float(route[1].split(',')[0])
        yE = float(route[1].split(',')[1])
        # we want this route
        if x1 <= x <= x2 and y1 <= y <= y2 and x1 <= xE <= x2 and y1 <= yE <= y2:
            ind = color_index(route[4], route[5])
            routes.append(route[2])
            inds.append(ind)

# construct the basic structure of json object
output = {
    'id': 'lines',
    'type': 'line',
    'source': {
        'type': 'geojson',
        'data': {
            'type': 'FeatureCollection',
            'features': []
        }
    },
    'paint': {
        'line-width': 3,
        # Use a get expression (https://www.mapbox.com/mapbox-gl-js/style-spec/#expressions-get)
        # to set the line-color to a feature property value.
        'line-color': ['get', 'color']
    }
}

# write the data into json
for i in range(0, len(routes)):
    line = {
        'type': 'Feature',
        'properties': {},
        'geometry': {
            'type': 'LineString',
            'coordinates': []
        }
    }
    # set the color
    if inds[i] == 0:
        line['properties']['color'] = '#00cc44'
    elif inds[i] == 1:
        line['properties']['color'] = '#ffcc00'
    elif inds[i] == 2:
        line['properties']['color'] = '#e63900'
    elif inds[i] == 3:
        line['properties']['color'] = '#ff0066'
    else:
        line['properties']['color'] = '#4d0026'
    # add the coords
    coords = line['geometry']['coordinates']
    for coord in routes[i]:
        coords.append([coord[1], coord[0]])

    # add the line
    output['source']['data']['features'].append(line)
    i += 1

with open('graph_json/data_uw_google.json', 'w') as outfile:
    json.dump(output, outfile)

