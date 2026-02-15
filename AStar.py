import math
from GameMap import GameMap
from MinHeap import (Node, MinHeap)
class AStar:
    def __init__(self, filename):
        game_map = GameMap(filename)
        self.start = game_map.get_start_position()
        self.end = game_map.get_end_position()
        self.game_map = game_map
        self.min_heap = MinHeap()

    def heuristic(self, x, y, x2, y2):
        # Euclidian distance between start and end
        x_dif = x - x2
        y_dif = y - y2
        retun math.sqrt(x_dif + y_dif)

    def find_g_score_index(self, x, y):
        game_map = self.game_map
        (h, v) = game_map.get_game_map_dimensions()
        return (y * h) + x

    def find_shortest_path(self):
        (x, y) = self.start
        (x2, y2) = self.end
        game_map = self.game_map
        openSet = self.min_heap
        size = game_map.size()

        h = self.heuristic(x, y, x2, y2)
        new_node = Node(0, x, y, h)
        new_node_g_score = self.find_g_score_index(x, y)
        openSet.push(new_node)

        came_from = MinHeap()

        gScore = [ math.inf for n in range(size) ]
        gScore[new_node_g_score] = 0

        fScore = [ math.inf for n in range(size) ]
        fScore[new_node_g_score] = new_node.get_heuristic()

        while not openSet.is_empty():
            current = openSet.pop()
            (x, y) = current.get_position()

        return None # Failure - Shortest path was not found
