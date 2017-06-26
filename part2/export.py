from reports import *


def export_to_file(file_name):
    with open(file_name, 'w', newline='\n') as export:
        export.writelines(str(get_most_played("game_stat.txt"))+"\n")
        export.writelines(str(sum_sold("game_stat.txt"))+"\n")
        export.writelines(str(get_selling_avg("game_stat.txt"))+"\n")
        export.writelines(str(count_longest_title("game_stat.txt"))+"\n")
        export.writelines(str(get_date_avg("game_stat.txt"))+"\n")
        export.writelines(str(get_game("game_stat.txt", 'Minecraft'))+"\n")
        export.writelines(str(count_grouped_by_genre("game_stat.txt"))+"\n")
        export.writelines(str(get_date_ordered("game_stat.txt")))

export_to_file('export.txt')