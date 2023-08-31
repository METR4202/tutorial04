import csv

class Node():
  def __init__(self, state, parents: tuple, cost, heuristics_cost = 0):
    self.state = state
    self.parents = parents
    self.cost = cost
    self.cost_for_heap_sorting = self.cost + heuristics_cost

  def __lt__(self, other):
      return self.cost_for_heap_sorting < other.cost_for_heap_sorting

class MapEnv():
  def __init__(self, map_data_path: str, map_names_path: str, map_heuristics_path = None):
    self.data = ()
    self.heuristics = {}
    self.read_map(map_data_path, map_names_path, map_heuristics_path)
    # print(self.data)

  def next_states(self, city: str):
    return tuple(filter(lambda x: x[0] == city, self.data))

  def heuristics_cost(self, city: str):
    return self.heuristics[city]

  def read_map(self, map_data_path, map_names_path, map_heuristics_path):
    names = {}
    with open(map_names_path) as csvfile:
      names_reader = csv.reader(csvfile)
      for row in names_reader:
        names[row[0]]= row[1]

    data = []
    with open(map_data_path) as csvfile:
      data_reader = csv.reader(csvfile)
      for row in data_reader:
        data.append((names[row[0]], names[row[1]], int(row[2])))
        data.append((names[row[1]], names[row[0]], int(row[2])))

    self.data = tuple(data)

    if map_heuristics_path:
      with open(map_heuristics_path) as csvfile:
        heuristics_reader = csv.reader(csvfile)
        for row in heuristics_reader:
          self.heuristics[row[1]] = int(row[2])
