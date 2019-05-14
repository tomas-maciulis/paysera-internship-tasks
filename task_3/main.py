from cow_object import cow_object as cow


def count_cows(years):
    try:
        years = int(years)
    except:
        return None

    cow_array = []
    cow_array.append(cow())

    for i in range(years):
        for j in range(len(cow_array)):
            cow_array[j].add_one_year()
            if cow_array[j].get_age() >= 3:
                cow_array.append(cow())

    return len(cow_array)

year = open('data.txt', 'r').readlines()[0]
print(count_cows(year))
