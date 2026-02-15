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
        return math.sqrt((x_dif + x_dif) + (y_dif + y_dif))

    def find_g_score_index(self, x, y):
        game_map = self.game_map
        (h, v) = game_map.get_game_map_dimensions()
        return (y * h) + x

    def decode_g_score_index(self, g_score):
        game_map = self.game_map
        (h, v) = game_map.get_game_map_dimensions()
        y = g_score // h 
        x = g_score - (y * h)
        return (x, y)


    def reconstruct_path(self, came_from, current, start):
        total_path = []
        (x, y) = current.get_position()
        (x2, y2) = start.get_position()
        while (x != x2) and (y != y2):
            idx = self.find_g_score_index(x, y)
            last_pos = came_from[idx]
            (last_x, last_y) = self.decode_g_score_index(last_pos)
            total_path.append([last_x, last_y])
            x = last_x
            y = last_y
        self.game_map.write_shortest_path(total_path)

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
        size = game_map.get_size()
        start_node = Node(0, x, y, 0)

        h = self.heuristic(x, y, x2, y2)
        new_node = Node(0, x, y, h)
        new_node_g_score = self.find_g_score_index(x, y)
        open_set.push(new_node)

        came_from = [ -1 for n in range(size) ]

        g_score = [ math.inf for n in range(size) ]
        g_score[new_node_g_score] = 0

        f_score = [ math.inf for n in range(size) ]
        f_score[new_node_g_score] = new_node.get_heuristic()

        while not open_set.is_empty():
            current = open_set.pop()
            (x, y) = current.get_position()
            if ((x == x2) and (y == y2)):
                self.reconstruct_path(came_from, current, start_node)
                return
            current_g_score_index = self.find_g_score_index(x, y)
            current_g_score = g_score[current_g_score_index]
            current_neighbors = self.find_neighbors(current)
            for neighbor in current_neighbors:
                [ neighbor_x, neighbor_y ] = neighbor
                d = game_map.movement_cost(neighbor_x, neighbor_y)
                # Found non traversible object
                if d == -1:
                    if game_map.is_goal_found(neighbor_x, neighbor_y):
                        self.reconstruct_path(came_from, current, start_node)
                        return
                    continue
                # Diagonal Cost
                if game_map.is_diagonal(x, y, neighbor_x, neighbor_y):
                    d = game_map.diagonal_multiplier(d)
                # Calculate g score of neighbor
                tentative_g_score = current_g_score + d
                neighbor_g_score_index = self.find_g_score_index(neighbor_x, neighbor_y)
                if tentative_g_score < g_score[neighbor_g_score_index]:
                    # calculate f score
                    cost_heuristic = self.heuristic(x, y, neighbor_x, neighbor_y)
                    came_from[neighbor_g_score_index] = current_g_score_index
                    g_score[neighbor_g_score_index] = tentative_g_score
                    f_score[neighbor_g_score_index] = tentative_g_score + cost_heuristic
                    if not open_set.find_node(neighbor_x, neighbor_y):
                        new_node = Node(d, neighbor_x, neighbor_y, cost_heuristic)
                        open_set.push(new_node)

        return None # Failure - Shortest path was not found

a_star = AStar("sample_input")
a_star.find_shortest_path()