import heapq
from typing import List, Tuple

def a_star(maze_lines:List[str]):
    def get_children(node: Node):
        children = []
        for direction in directions:
            new_x = node.x + direction[0]
            new_y = node.y + direction[1]

            if new_y < 0 or new_y > len(maze_lines):
                continue
            if new_x < 0 or new_x > len(maze_lines[0]):
                continue
            child_node = Node()
            child_node.x = new_x
            child_node.y = new_y
            children.append(child_node)
        return children


    maze_lines = maze_lines
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    open = []
    closed = []

    start:Node = None
    escape:Node = None

    for y,line in enumerate(maze_lines):
        for x,c in enumerate(line):
            if c == 'x':
                node = Node()
                node.x = x
                node.y = y
                start = node
            elif c== 'A':
                node = Node()
                node.x = x
                node.y = y
                escape = node

    if not start or not escape:
        raise ValueError('start and/or escape is missing')

    open.append(start)

    while open:
        open.sort(key=smallestf)
        current = open.pop(0)

        children = get_children(current)













class Node:
    def __init__(self):
        self.parent: Node = None
        self.x = None
        self.y = None
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

def smallestf(e:Node):
    return e.f


