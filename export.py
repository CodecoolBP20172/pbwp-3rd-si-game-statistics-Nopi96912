from reports import *


def export_to_file(file_name):
    with open(file_name, 'w', newline='\n') as export:
        export.writelines(str(count_games("game_stat.txt"))+"\n")
        export.writelines(str(decide("game_stat.txt", 1998))+"\n")
        export.writelines(str(get_latest("game_stat.txt"))+"\n")
        export.writelines(str(count_by_genre("game_stat.txt", "RPG"))+"\n")
        export.writelines(str(get_line_number_by_title("game_stat.txt", "Command & Conquer"))+"\n")
        export.writelines(str(sort_abc("game_stat.txt"))+"\n")
        export.writelines(str(get_genres("game_stat.txt"))+"\n")
        export.writelines(str(when_was_top_sold_fps("game_stat.txt")))

export_to_file('export.txt')