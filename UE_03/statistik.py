__author__ = "Benjamin Zwettler"

import subprocess

#get data

data = subprocess.run(["git -C /mnt/shared/Crill-IOS-Scripting/ log --pretty=format:\"%an;%ad\" --date=rfc2822"],shell=True, capture_output=True).stdout.decode("utf-8")
print(data)
