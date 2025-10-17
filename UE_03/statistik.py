__author__ = "Benjamin Zwettler"

import subprocess
import matplotlib.pyplot as plt
from dateutil import parser
#get data

data = subprocess.run(["git -C /mnt/shared/Crill-IOS-Scripting/ log --pretty=format:\"%an;%ad\" --date=rfc2822"],shell=True, capture_output=True).stdout.decode("utf-8")
#print(data)
data = data.split("\n")
points = {}
for line in data:
    line_split = line.split(";")
    name = line_split[0]
    date = parser.parse(line_split[1]).date()
    day = date.weekday()
    time = parser.parse(line_split[1]).time().hour
    print(name +" \n "+ str(date) + "\n  " + str(time) + "\n  " + str(day) )
    if (day, time) in points:
        points[(day, time)] += 1
    else:
        points[(day, time)] = 1

print(points)




fig, ax = plt.subplots()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlabel('Uhrzeit')
ax.set_ylabel('Wochentag')
ax.set_aspect(24/7)

# Achsenbeschriftung
xticks = list(range(0, 24, 2))
xlabels = [str(x) for x in xticks]
plt.xticks(xticks, xlabels)
plt.yticks([1,2,3,4,5,6,7],
       [r'$Mo$', r'$Di$',r'$Mi$',r'$Do$',r'$Fr$',r'$Sa$',r'$So$'])
# Titel
ax.set_title("Zwettler")



plt.show()