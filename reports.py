def count_games(file_name):
    with open(file_name, 'r') as source_file:
        return sum(1 for line in source_file)


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False


def list_from_file(file_name, place, type):
    data = []
    with open(file_name, 'r') as source_file:
        for line in source_file:
            data.append(line.strip().split('\t'))
    temp = []
    counter = 0
    for item in data:
        temp.append(type(data[counter][place]))
        counter += 1
    return data, temp, counter


def get_latest(file_name):
    data, temp, counter = list_from_file(file_name, 2, int)
    latest = temp.index(max(temp))
    return str(data[latest][0])


def count_by_genre(file_name, genre):
    data, temp, counter = list_from_file(file_name, 3, str)
    genre_dict = dict((i, temp.count(i)) for i in temp)
    return genre_dict.get(genre)


def get_line_number_by_title(file_name, title):
    try:
        data, temp, counter = list_from_file(file_name, 0, str)
        return int(temp.index(title)) + 1
    except ValueError:
        return 'This game is not in the list'


def sort_abc(file_name):
    data, temp, counter = list_from_file(file_name, 0, str)
    new_list = []
    while temp:
        minimum = min(temp)
        for item in temp:
            if item < minimum:
                minimum = item
        new_list.append(minimum)
        temp.remove(minimum)
    return new_list