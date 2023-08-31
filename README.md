# Tutorial 04

Graph search using Dijkstra's algorithm and A* for finding the shortest path from Perth to Brisbane.

![AU Map](resources/map.png)

### Dependencies
Python3. No additional dependencies required.

### Running

    python main.py

### Map Data
The distances between cities are given in [map_data.csv](data/map_data.csv) in the format of `start_ind, end_ind, distance`. The cities are indexed based on the table in [map_names.csv](data/map_names.csv).

The heuristics data arein [map_heuristics.csv](data/map_heuristics.csv) and unfortunately, it only contains heuristics with respect to Brisbane, so the A* search will only work if the goal city is set to Brisbane.