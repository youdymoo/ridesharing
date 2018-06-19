#!/usr/bin/python
import json
import urllib.request
import sys

def raw2csv(tripData):
    output = 'lng,lat\n'
    for dataEntry in tripData:
        for segment in dataEntry['segments']:
            lng = segment[0]
            lat = segment[1]
            new_entry = '{},{}'.format(lng, lat) + '\n'
            output += new_entry
    output = output[:-1]
    print(output)


def raw2space(tripData):
    output = ''
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


def center2csv(center_file):
    output = 'lng,lat\n'
    for line in center_file:
        lng, lat = (line.strip()).split()
        new_entry = '{},{}'.format(lng, lat) + '\n'
        output += new_entry
    return output


def index2neighbor(neighbor_file):
    count = 0
    neighbor_dict = {}
    neighbor_list = []
    for line in neighbor_file:
        if count == 0:
            index_name = line.strip()
            count += 1
        elif count == 7:
            neighbor_dict[index_name] = neighbor_list
            neighbor_list = []
            count = 0
        else:
            neighbor_list.append(line.strip())
            count += 1
    return neighbor_dict       


def main():
    args = sys.argv[1:]

    ''' input trip json data '''
    with urllib.request.urlopen('https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/trips/trips.json') as response:
        tripData = json.loads(response.read().decode('utf-8'))

    ''' operations on trip json data '''
    if not args:
        print('usage: [--csv/--space/--index/--neighbor] > output file')
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
        center_file = open('data/center/tripData-center-complete.txt', 'r')
        output = center2csv(center_file)
        center_file.close()
        center_csv =  open('data/center/tripData-center-complete.csv', 'w')
        center_csv.write(output)
        center_csv.close()
    elif args[0] == '--neighbor':
        neighbor_file = open('data/neighbor/tripData-neighbor.txt', 'r')
        neighbor_dict = index2neighbor(neighbor_file)
        neighbor_file.close()
        
        neighbor_json = open('data/neighbor/tripData-neighbor.json', 'w')
        r = json.dumps(neighbor_dict, sort_keys=True, indent=4)
        neighbor_json.write(str(r))
        neighbor_json.close()


if __name__ == '__main__':
    main()
