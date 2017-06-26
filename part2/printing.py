import pprint
from reports import *


pp = pprint.PrettyPrinter(width=80, compact=True)
pp.pprint(get_most_played("game_stat.txt"))
pp.pprint(sum_sold("game_stat.txt"))
pp.pprint(get_selling_avg("game_stat.txt"))
pp.pprint(count_longest_title("game_stat.txt"))
pp.pprint(get_date_avg("game_stat.txt"))
pp.pprint(get_game("game_stat.txt", 'Minecraft'))
pp.pprint(count_grouped_by_genre("game_stat.txt"))
pp.pprint(get_date_ordered("game_stat.txt"))