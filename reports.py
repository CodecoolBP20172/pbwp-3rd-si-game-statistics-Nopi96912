def count_games(file_name='game_stat.txt'):
    with open(file_name, 'r') as source_file:
        return sum(1 for line in source_file)


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False


def get_latest(file_name='game_stat.txt'):
    data = []
    with open(file_name, 'r') as source_file:
        for line in source_file:
            data.append(line.strip().split('\t'))
    year = []
    counter = 0
    for item in data:
        year.append(int(data[counter][2]))
        counter += 1
    latest = year.index(max(year))
    return str(data[latest][0])


def count_by_genre(file_name, genre):
    data = []
    with open(file_name, 'r') as source_file:
        for line in source_file:
            data.append(line.strip().split('\t'))
    genre_list = []
    counter = 0
    for item in data:
        genre_list.append(data[counter][3])
        counter += 1
    genre_dict = dict((i, genre_list.count(i)) for i in genre_list)
    return genre_dict.get(genre)


def get_line_number_by_title(file_name, title):
    data = []
    with open(file_name, 'r') as source_file:
        for line in source_file:
            data.append(line.strip().split('\t'))
    title_list = []
    counter = 0
    for item in data:
        title_list.append(data[counter][0])
        counter += 1
    return int(title_list.index(title)) + 1