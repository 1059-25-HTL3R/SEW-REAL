
import MazeParser


file_path = "/mnt/shared/schule/SEW-REAL/UE_04/Mazes/l1.txt"

with open(file_path, 'r') as file:
    file_content = file.read()

p = MazeParser.MazeParser(file_content)

p.aStar()

