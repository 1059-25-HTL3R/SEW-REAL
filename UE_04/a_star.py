from copy import deepcopy

_author_ = "Benjamin Zwettler"
import MazeParser


def a_star(mazeinput):
    p = MazeParser.MazeParser(mazeinput)
    queue = [(p.getstartnode())]     # nodes to be inspected
    visited = []                        # already inspected nodes

    queue = queue.sort()
    print(p.getstartnode())





file_path = "/mnt/shared/schule/SEW-REAL/UE_04/Mazes/l1.txt"

with open(file_path, 'r') as file:
    file_content = file.read()
a_star(file_content)

