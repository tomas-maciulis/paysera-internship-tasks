import json

DATA_PATH = 'data.json'
DATA = json.loads(open(DATA_PATH, 'r').readlines()[0])

def count_points():
    points = 0

    for entry in DATA:
        match = entry.split(':')
        x = match[0]
        y = match[1]

        if x>y:
            points += 3
        elif x<y:
            pass
        else:
            points += 1

    return points

print('x team scored ' + str(count_points()) + ' points')
