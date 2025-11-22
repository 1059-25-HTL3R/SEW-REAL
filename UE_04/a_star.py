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

    def get_h(a:Node, b:Node):
        return abs(a.x - b.x) + abs(a.y - b.y)
    def get_path(node:Node, path:List[Node]):
        if node.parent is None:
            return path.insert(0, node)
        else:
            path.insert(0, node)
            return get_path(node.parent, path)

    maze_lines = maze_lines
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    open:List[Node] = []
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
        print(open)
        open.sort(key=smallestf)
        current = open.pop(0)

        children:List[Node] = get_children(current)
        for child in children:
            child.parent = current

            if child.x == escape.x and child.y == escape.y:
                return get_path(current, [child])
            else:
                child.g = current.g + 1
                child.h = get_h(child, escape)
                child.f = child.g + child.h
                skip = False
                for node in open:
                    if node.x == child.x and node.y == child.y and node.f < child.f:
                        skip = True
                if skip:
                    continue
                skip  = False
                for node in closed:
                    if node.x == child.x and node.y == child.y and node.f < child.f:
                        skip = True
                if skip:
                    continue
                else:
                    open.append(child)
        closed.append(current)






class Node:
    def __init__(self):
        self.parent: Node = None
        self.x = None
        self.y = None
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0
    def __str__(self):
        return f'({self.x},{self.y})'

def smallestf(e:Node):
    return e.f


def main():

    with open('/mnt/shared/schule/SEW-REAL/UE_04/Mazes/l1.txt') as f:
        maze = f.readlines()
    print(a_star(maze))

if __name__ == "__main__":
    main()


