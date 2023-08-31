from dijkstra import dijkstra
from map_env import MapEnv, Node

env = MapEnv('data/map_data.csv', 'data/map_names.csv')

dijkstra(env, 'Perth', 'Brisbane')
