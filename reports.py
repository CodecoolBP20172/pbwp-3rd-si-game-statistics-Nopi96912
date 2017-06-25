def count_games(file_name='game_stat.txt'):
    with open(file_name, 'r') as source_file:
        return sum(1 for line in source_file)


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False


def get_latest(file_name):
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