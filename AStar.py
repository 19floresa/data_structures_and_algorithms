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

    def reconstruct_path(self, came_from, current):
        pass

    def find_neighbors(self, current):
        game_map = self.game_map
        ( x, y ) = current.get_position()
        offsets = [ [ -1, 1  ], [ 0,  1 ], [ 1, 1  ], 
                    [ -1, 0  ],            [ 1, 0  ],
                    [ -1, -1 ], [ 0, -1 ], [ 1, -1 ], ]
        neighbors = []
        for offset in offsets:
            [ x_offset, y_offset ] = offset
            new_x = x + x_offset
            new_y = y + y_offset
            if (game_map.is_valid_position(new_x, new_y)):
                neighbors.append(offset)
        return neighbors

    def find_shortest_path(self):
        (x, y) = self.start
        (x2, y2) = self.end
        game_map = self.game_map
        open_set = self.min_heap
        size = game_map.size()

        h = self.heuristic(x, y, x2, y2)
        new_node = Node(0, x, y, h)
        new_node_g_score = self.find_g_score_index(x, y)
        open_set.push(new_node)

        came_from = MinHeap()

        g_score = [ math.inf for n in range(size) ]
        g_score[new_node_g_score] = 0

        f_score = [ math.inf for n in range(size) ]
        f_score[new_node_g_score] = new_node.get_heuristic()

        while not open_set.is_empty():
            current = open_set.pop()
            (x, y) = current.get_position()
            if ((x == x2) and (y == y2)):
                self.reconstruct_path(came_from, current)
                return
            current_neighbors = self.find_neighbors(current)
            for neighbor in current_neighbors:
                
            


        return None # Failure - Shortest path was not found
