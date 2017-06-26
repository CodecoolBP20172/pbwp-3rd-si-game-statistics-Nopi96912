from reports import *


def export_to_file(file_name, source_file):
    with open(file_name, 'w', newline='\n') as export:
        export.writelines(str(get_most_played(source_file))+"\n")
        export.writelines(str(sum_sold(source_file))+"\n")
        export.writelines(str(get_selling_avg(source_file))+"\n")
        export.writelines(str(count_longest_title(source_file))+"\n")
        export.writelines(str(get_date_avg(source_file))+"\n")
        export.writelines(str(get_game(source_file, 'Minecraft'))+"\n")
        export.writelines(str(count_grouped_by_genre(source_file))+"\n")
        export.writelines(str(get_date_ordered(source_file)))

export_to_file('export.txt', 'game_stat.txt')