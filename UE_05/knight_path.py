__author__ = "Benjamin Zwettler"
__email__ = "1059@htl.rennweg.at"
__license__ = "corprate"
import heapq
from typing import List
import time
class Node:
    def __init__(self, x=None, y=None):
        self.parent: Node = None
        self.x = x
        self.y = y
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

    def __lt__(self, other):
        return self.f < other.f  # für heapq
    def __repr__(self):
        return f'({self.x}, {self.y})'

def knight_path_find(maze_lines: List[str]):

    #simple direction list
    directions = [ (-2, -1),(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1),(1, -2),(-1, -2)]

    #gets all neighbores / children from a specific node
    def get_children(node: Node):
        children = []
        for dx, dy in directions:
            nx, ny = node.x + dx, node.y + dy #<- schreibweise von chat
            if 0 <= ny < len(maze_lines) and 0 <= nx < len(maze_lines[0]):
                if maze_lines[ny][nx] != '#':  # '#' = Wand
                    child = Node(nx, ny)
                    children.append(child)
        return children

    #calculates the manhatten h value
    def get_h(a: Node, b: Node):
        return abs(a.x - b.x) + abs(a.y - b.y)

    # recursivly reconstructs the path
    def get_path(node: Node):
        path = []
        while node:
            path.insert(0, node)
            node = node.parent
        return path
    # initialize the start and end node
    start = None
    escape = None
    # find the coordinates of the start and end node
    for y, line in enumerate(maze_lines):
        for x, c in enumerate(line):
            if c == 'x':
                start = Node(x, y)
                start.g = 0
                start.f = 0
            elif c == 'A':
                escape = Node(x, y)

    # if one of the start / end nodes werent found raise an error
    if not start or not escape:
        raise ValueError("Start oder Escape fehlt")

    # initialize the open and closeed dicts / list
    open_heap = []
    open_dict = {}
    closed_dict = {}

    #push start node on open list
    heapq.heappush(open_heap, (start.f, start))
    open_dict[(start.x, start.y)] = start

    while open_heap:
        current_f, current = heapq.heappop(open_heap)
        del open_dict[(current.x, current.y)]
        closed_dict[(current.x, current.y)] = current

        if current.x == escape.x and current.y == escape.y:
            return get_path(current)

        for child in get_children(current):
            child.parent = current
            child.g = current.g + 1
            child.h = get_h(child, escape)
            child.f = child.g + child.h

            pos = (child.x, child.y)

            if pos in closed_dict and closed_dict[pos].f <= child.f:
                continue

            if pos in open_dict and open_dict[pos].f <= child.f:
                continue

            heapq.heappush(open_heap, (child.f, child))
            open_dict[pos] = child

    return None


def main():
    with open('../UE_04/Mazes/l2.txt') as f:
        maze = f.readlines()
        start = time.perf_counter()
        print(knight_path_find(maze))
        end = time.perf_counter()
        print(end - start)
if __name__ == "__main__":
    main()


