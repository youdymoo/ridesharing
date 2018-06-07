#!/usr/bin/python
import json
import urllib.request

with urllib.request.urlopen('https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/trips/trips.json') as response:
	tripData = json.loads(response.read().decode('utf-8'))

output = '['
for dataEntry in tripData:
	for segment in dataEntry['segments']:
		lng = segment[0]
		lat = segment[1]
		new_entry = '{' + "lng: {}, lat: {}".format(lng, lat) + '}'
		output += new_entry + ','
output = output[:-1]
output += ']'
print(output)