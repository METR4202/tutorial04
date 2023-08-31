import heapq
import time
from typing import Dict

from map_env import MapEnv, Node


def dijkstra(env: MapEnv, start: str, goal: str):
  t0 = time.time()

  visited: Dict[str, int] = {start: 0}

  heap = [Node(start, (), 0)]
  heapq.heapify(heap)

  nodes_expanded = 0

  while heap:
    node = heapq.heappop(heap)

    if node.state == goal:
      print(
        f"Found the goal in {len(node.parents)} steps and {time.time() - t0}s. Visited {len(visited)} nodes and expanded {nodes_expanded}, nodes in the heap {len(heap)}")
      print(f"Path {node.parents} -> {goal}")
      print(f"Path cost {node.cost}")
      return node.parents, node.cost

    for new_state in env.next_states(node.state):
      next_city = new_state[1]
      cost = new_state[2]
      new_cost = cost + node.cost

      if next_city not in visited.keys() or visited[next_city] > new_cost:
        visited[next_city] = new_cost
        heapq.heappush(heap, Node(next_city, node.parents + (node.state,), new_cost))

    nodes_expanded += 1
