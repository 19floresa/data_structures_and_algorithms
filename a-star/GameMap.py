class GameMap:
    def __init__(self, filename):
        with open(f"{filename}.txt", "r") as file:
            game_map = []
            for line in file:
                line = line.split(" ")
                line[-1] = line[-1].rstrip()
                line = [ l for l in line if l != ""]
                game_map.append(line)

            self.x = len(game_map[0])
            self.y = len(game_map)
            self.game_map = game_map
    
    def is_valid_position(self, new_x, new_y):
        (x, y) = self.get_game_map_dimensions()
        is_valid_x = (new_x >= 0) and (new_x < x)
        is_valid_y = (new_y >= 0) and (new_y < y)
        return is_valid_x and is_valid_y
    
    def movement_cost(self, new_x, new_y):
        obstacle = self.game_map[new_y][new_x]
        match (obstacle):
            case '.':
                return 1
            case ',':
                return 2
            case 'o':
                return 3
            case '=':
                return 50
            case _:
                return -1

    def is_goal_found(self, new_x, new_y):
        obstacle = self.game_map[new_y][new_x]
        match (obstacle):
            case '0':
                return False
            case '1':
                return False
            case '2':
                return True
            case '3':
                return False
            case _:
                raise ValueError(f"Unrecognized character ({obstacle})!");

    def is_diagonal(self, x, y, x2, y2):
        x_diff = x - x2
        y_diff = y - y2
        return (x_diff != 0)  and (y_diff != 0)
    
    def diagonal_multiplier(self, val):
        return val * 1.5

    def get_game_map_dimensions():
        return (self.x, self.y)

    def get_start_position():
        game_map = self.game_map
        for y in range(len(game_map)):
            row = game_map[y]
            for x in range(len(row)):
                col = row[x]
                if col == "0":
                    return (x, y)
        raise ValueError("Start position was not found: '0'.")

    def get_end_position():
        game_map = self.game_map
        for y in range(len(game_map)):
            row = game_map[y]
            for x in range(len(row)):
                col = row[x]
                if col == "2":
                    return (x, y)
        raise ValueError("End position was not found: '2'.")

    def get_size(self):
        (x, y) = self.get_game_map_dimensions()
        return x * y



n = GameMap("sample_input")
