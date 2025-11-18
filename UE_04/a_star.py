from copy import deepcopy

_author_ = "Benjamin Zwettler"
import MazeParser


def a_star(mazeinput):
    p = MazeParser.MazeParser(mazeinput)
    queue = [(p.getstartnode(), 0)]     # nodes to be inspected
    visited = []                        # already inspected nodes

    queue = queue.sort()
    print(p.nodes[1])





file_path = "/mnt/shared/schule/SEW-REAL/UE_04/Mazes/l1.txt"

with open(file_path, 'r') as file:
    file_content = file.read()
a_star(file_content)

