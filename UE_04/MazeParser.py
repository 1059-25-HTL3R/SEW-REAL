#MazeParser.py
from typing import List, Tuple


class MazeParser:

    def __init__(self, maze):
        self.maze = maze
        self.exit_symbol = None
        self.border_symbol = None
        self.start_symbol = None
        self.nodes: List[Node] = []
        self.check_maze()
        self.parse()


    def check_maze(self):
        lines = self.maze.splitlines()
        symbols = self.check_symbols(lines)
        symbols = dict(sorted(symbols.items(), key=lambda item: item[1], reverse=True))
        symbols = list(symbols.keys())
        self.check_border(lines)
        symbols.remove(self.border_symbol)
        symbols.remove(self.exit_symbol)
        self.start_symbol = symbols[-1]
        if str(self.maze).count(self.start_symbol) > 1:
            raise "maze has no start symbol"

        print(self.maze)
        print("BORDER: " + self.border_symbol)
        print("EXIT: " + self.exit_symbol)
        print("START: " + self.start_symbol)

    def parse(self):
        lines = self.maze.splitlines()
        for y,line in enumerate(lines):
            for x, symbol in enumerate(line):
                neighbours =[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for neighbour in neighbours:
                    if neighbour[0] <0 or neighbour[1] < 0 or neighbour[0] > len(line)-1 or neighbour[1] > len(lines)-1:
                        neighbours.remove(neighbour)
                #adding costs to neighbors for current node
                costneighbours = []
                for neighbour in neighbours:
                    costneighbours.append(self.getcost((x,y), neighbour))
                node = Node((x, y), costneighbours)
                nodetype = None
                match symbol:
                    case self.exit_symbol:
                        nodetype = "exit"
                    case self.border_symbol:
                        nodetype = "border"
                    case self.start_symbol:
                        nodetype = "start"
                node.type = nodetype
                self.nodes.append(node)


    def getnodeneighbours(self,name):
        for node in self.nodes:
            if node.name == name:
                return node

        return None


    def check_symbols(self,lines):
        symbols = {}
        for line in lines:
            for symbol in line:
                if symbol not in symbols:
                    symbols[symbol] = 1
                else:
                    symbols[symbol] += 1
        if len(symbols) != 4:
            if len(symbols) >4:
                raise "maybe wrong maze syntax! -> (maze contains more than 4 symbols) "
        return symbols

    def check_border(self,lines):
        border = []
        border.append(lines[0])
        border.append(lines[len(lines)-1])
        lines = lines[1:-1]

        for line in lines:
            border.append(line[0])
            border.append(line[len(line)-1])

        symbols = {}
        for line in border:
            for symbol in line:
                if symbol not in symbols:
                    symbols[symbol] = 1
                else:
                    symbols[symbol] += 1

        if len(symbols) > 2:
            raise "border has more than 2 symbols"
        symbols = dict(sorted(symbols.items(), key=lambda item: item[1], reverse=True))
        self.exit_symbol = list(symbols.keys())[1]
        self.border_symbol = list(symbols.keys())[0]

    def getstartnode(self):
        for node in self.nodes:
            if node.type == "start":
                return node
        else:
            return None

    def getexitnodes(self):
        out = []
        for node in self.nodes:
            if node.type == "exit":
                out.append(node)

    def getcost(self,current, neighbour):
        return neighbour,1

    def cheapestfirst(self, e):
        return e[1]


    def aStar(self):
        queue:List[Tuple[Node,int]] = [(self.getstartnode(), 0)]
        visited = []

        while queue:
            queue.sort(key= self.cheapestfirst)
            current = queue.pop(0)

            currentChildren = current[0].getneighbours()

            for child in currentChildren:
                if child.type == "exit":
                    break
                else:
                    cost = self.getcost(current[0], child)
                if self.nodes.index(child) && :





class Node:
    def __init__(self, name, neighbours: list):
        self.name = name
        self.type = None
        self.neighbours: List[Node] = neighbours
        self.parent = None

    def getneighbours(self):
        return self.neighbours

    def getname(self):
        return self.name

    def __str__(self):
        return "---\nNODE: "+str(self.name) + "\n" + "Neighbours: "+str(self.neighbours)


