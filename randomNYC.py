import json
import geojson
import random
import numpy as np
from shapely.geometry import shape, Point

def generate_random(number, polygon):
    list_of_points = []
    minx, miny, maxx, maxy = polygon.bounds
    counter = 0
    while counter < number:
        point = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(point):
            list_of_points.append([point.bounds[0],point.bounds[1]])
            counter += 1
    return list_of_points


def raw2space(tripData):
    output = ''
    for dataEntry in tripData:
        lng = dataEntry[0]
        lat = dataEntry[1]
        new_entry = '{} {}'.format(lng, lat) + '\n'
        output += new_entry
    output = output[:-1]
    return output


with open('data/manhatten.geojson') as f:
    data = json.load(f)

for i in range(len(data['features'])):
    polygon = shape(data['features'][i]['geometry'])
    print(data['features'][i]['properties']['name'], 'added')
    complete_space_file = open('data/random/NYCdata-random-complete.txt', 'a')
    complete_space_file.write(raw2space(generate_random(polygon.area * 1e8, polygon)))
    complete_space_file.close()
