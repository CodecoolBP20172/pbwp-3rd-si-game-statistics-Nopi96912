from reports import *


def export_to_file(file_name, source_file):
    with open(file_name, 'w', newline='\n') as export:
        export.writelines(str(count_games(source_file))+"\n")
        export.writelines(str(decide(source_file, 1998))+"\n")
        export.writelines(str(get_latest(source_file))+"\n")
        export.writelines(str(count_by_genre(source_file, "RPG"))+"\n")
        export.writelines(str(get_line_number_by_title(source_file, "Command & Conquer"))+"\n")
        export.writelines(str(sort_abc(source_file))+"\n")
        export.writelines(str(get_genres(source_file))+"\n")
        export.writelines(str(when_was_top_sold_fps(source_file)))

export_to_file('export.txt', 'game_stat.txt')