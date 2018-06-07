import random

output = '['
# suburb
for i in range(4000):
	lng = random.randrange(-74042, -73706)/1000
	lat = random.randrange(40572, 40913)/1000
	new_entry = '{' + "lng: {}, lat: {}".format(lng, lat) + '}'
	output += new_entry + ','

# downtown
for i in range(10000):
	lng = random.randrange(-74011, -73981)/1000
	lat = random.randrange(40716, 40756)/1000
	new_entry = '{' + "lng: {}, lat: {}".format(lng, lat) + '}'
	output += new_entry + ','

lng = random.randrange(-74042, -73706)/1000
lat = random.randrange(40572, 40913)/1000
new_entry = '{' + "lng: {}, lat: {}".format(lng, lat) + '}'
output += new_entry + ']'
print(output)