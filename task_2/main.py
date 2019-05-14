import json

DATA_PATH = 'data.json'
try:
    DATA = json.loads(open(DATA_PATH, 'r').readlines()[0])
except:
    exit('invalid data')

def calculate_perimeter():
    perimeter = 0
    processed_data = []

    for entry in DATA:
        processed_data.append(list(entry))

    # ignore collisions
    for entry in processed_data:
        for symbol in entry:
            if symbol == 'X':
                perimeter += 4

    for i in range(len(processed_data)):
        for j in range(len(processed_data[i])):
            try:
                if processed_data[i][j] == 'X':
                        # horizontal collision
                    if processed_data[i][j+1] == 'X':
                        perimeter += -2

                        # vertical collision
                    if processed_data[i+1][j] == 'X':
                        perimeter += -2


            except Exception as e:
                pass

    return perimeter

print('perimeter of given islands is: ' + str(calculate_perimeter()))
