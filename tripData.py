#!/usr/bin/python
import json
import urllib.request
import sys

def raw2csv(tripData):
    output = 'lng, lat\n'
    for dataEntry in tripData:
        for segment in dataEntry['segments']:
            lng = segment[0]
            lat = segment[1]
            new_entry = '{}, {}'.format(lng, lat) + '\n'
            output += new_entry
    output = output[:-1]
    print(output)


def raw2space(tripData):
    for dataEntry in tripData:
        for segment in dataEntry['segments']:
            lng = segment[0]
            lat = segment[1]
            new_entry = '{} {}'.format(lng, lat) + '\n'
            output += new_entry
    output = output[:-1]
    print(output)


def space2index(space_file):
    index_dict = {}
    for line in space_file:
        line = line.strip()
        if line not in index_dict:
            index_dict[line] = 1
        else:
            index_dict[line] += 1
    return index_dict

def index2neighbor(index_file):
    pass

def main():
    args = sys.argv[1:]

    ''' input trip json data '''
    with urllib.request.urlopen('https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/trips/trips.json') as response:
        tripData = json.loads(response.read().decode('utf-8'))

    ''' operations on trip json data '''
    if not args:
        print('usage: [--csv/--space/--index] > output file')
        sys.exit(1)
    elif args[0] == '--csv':
        raw2csv(tripData)
    elif args[0] == '--space':
        raw2space(tripData)
    elif args[0] == '--index':
        space_file = open('data/index/tripData-index-complete.txt', 'r')
        index_dict = space2index(space_file)
        space_file.close()

        index_json = open('data/index/tripData-index.json', 'w')
        r = json.dumps(index_dict, sort_keys=True, indent=4)
        index_json.write(str(r))
        index_json.close()

        index_file = open('data/index/tripData-index.txt', 'w')
        for key in index_dict.keys():
            index_file.write(str(key)+'\n')
        index_file.close()
    elif args[0] == '--center':
        sys.exit(1)

if __name__ == '__main__':
    main()
