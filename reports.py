def count_games(file_name='game_stat.txt'):
    with open(file_name, 'r') as source_file:
        return sum(1 for line in source_file)


def decide(file_name, year):
    if str(year) in open(file_name).read():
        return True
    else:
        return False