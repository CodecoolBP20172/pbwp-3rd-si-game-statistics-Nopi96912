import math


def list_from_file(file_name, place, type):
    data = []
    with open(file_name, 'r') as source_file:  # make a 2D list from the file, each line is one list
        for line in source_file:
            data.append(line.strip().split('\t'))
    temp = []
    counter = 0
    for item in data:  # make a list with one type elements 
        temp.append(type(data[counter][place]))
        counter += 1
    return data, temp, counter


def get_most_played(file_name):
    data, temp, counter = list_from_file(file_name, 1, float)
    return str(data[temp.index(max(temp))][0])


def sum_sold(file_name):
    data, temp, counter = list_from_file(file_name, 1, float)
    return sum(temp)


def get_selling_avg(file_name):
    data, temp, counter = list_from_file(file_name, 1, float)
    return (sum(temp) / len(temp))


def count_longest_title(file_name):
    data, temp, counter = list_from_file(file_name, 0, str)
    return int(len(max(temp, key=len)))


def get_date_avg(file_name):
    data, temp, counter = list_from_file(file_name, 2, float)
    return int(math.ceil(sum(temp) / len(temp)))


def get_game(file_name, title):
    data, temp, counter = list_from_file(file_name, 0, str)
    place = 0
    for item in temp:
        if item == title:
            new_list = data[place]
        place += 1
    new_list[1] = float(new_list[1])
    new_list[2] = int(new_list[2])
    return new_list
