import os
import os.path
import re

AIM_DIRS = {
    "./"   :"MYSQL"   ,
}

class Topic:
    def __init__(self,dirName,fileName):
        self.index = fileName.split(".")[0]
        parts = self.index.split()
        if len(parts) > 0:
            self.index = parts[0]
            self.title = parts[-1]
        else:
            self.title = ""
        self.path = os.path.join(dirName,fileName)
        self.language = AIM_DIRS[dirName]

def indexCmp(x):
    index = x[0]
    if index.isdigit():
        return int(index)
    else:
        matchs = re.findall("[0-9]+",index)
        if(len(matchs) > 0):
            matchVal = int(matchs[0])
            return matchVal
        else:
            return 10e+7
            
datas = {}
for dirPath,lan in AIM_DIRS.items():
    for f in os.listdir(dirPath):
        if os.path.isdir(os.path.join(dirPath,f))\
        or "test" in f \
        or "include" in f:
            continue
        t = Topic(dirPath,f)
        if t.index not in datas:
            datas[t.index] = []
        datas[t.index].append(t)
datas = list(datas.items())
datas.sort(key = indexCmp)

with open("README.md",'w+') as out:
    out.write("编号|标题\n")
    out.write("---|---\n")
    for data in datas:
        indexStr = data[0]
        titleStr = "[%s](%s),"%(data[1][0].title,data[1][0].path)
        res = ("%s|%s\n")%(indexStr,titleStr)
        out.write(res)

