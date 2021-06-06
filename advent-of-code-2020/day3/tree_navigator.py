class OutOfSlopeBounds(Exception):
    pass


class TreeMap:
    def __init__(self, tree_map, x_delta):
        self.map = tree_map
        self.x_delta = x_delta
        self.y_len = len(tree_map)
        self.x_len = len(tree_map[0])

    def is_tree_here(self, x_pos, y_pos):
        if y_pos >= self.y_len:
            raise OutOfSlopeBounds

        x_index = x_pos % self.x_len

        return self.map[y_pos][x_index] == '#'

    def count_trees_hit(self):
        x_pos = 0
        y_pos = 0
        tree_count = 0

        while True:
            try:
                if self.is_tree_here(x_pos, y_pos):
                    tree_count += 1

                x_pos += self.x_delta
                y_pos += 1

            except OutOfSlopeBounds:
                break

        return tree_count


def count_trees_hit(tree_map, x_delta):
    tm = TreeMap(tree_map, x_delta)
    return tm.count_trees_hit()


def count_trees_hit_delta_3(tree_map):
    tm = TreeMap(tree_map, 3)
    return tm.count_trees_hit()
