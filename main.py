from a_star import a_star
from dijkstra import dijkstra
from map_env import MapEnv

env = MapEnv('data/map_data.csv', 'data/map_names.csv', 'data/map_heuristics.csv')

print("\n\nDijkstra Search:")
dijkstra(env, 'Perth', 'Brisbane')

print("\n\nA* Search:")
a_star(env, 'Perth', 'Brisbane')
