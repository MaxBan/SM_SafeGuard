def getFiredman(intervals):
    length = len(intervals)
    total = 0
    flag = 0
    merge = []
    if length <= 1:
        print("wrong input")
        return
    intervals = sorted(intervals, key=lambda interval: interval[0])
    start = intervals[0][0]
    smallest = intervals[-1][1]
    for i in range(0, length):
        if flag==0 :
            if i != length - 1:
                impact = min(intervals[i + 1][0], intervals[i][1]) - start
            else:
                impact = intervals[-1][1] - start
            if impact < 0:
                impact = 0
                flag = 1
            smallest = min(smallest, impact)
            if i != length - 1:
                start = max(intervals[i + 1][0], intervals[i][1])
        if merge and intervals[i][0] <= merge[-1][1]:
            merge[-1][1] = max(merge[-1][1], intervals[i][1])
        else:
            merge.append(intervals[i])
    for item in merge :
        total += item[1] - item[0]
    return total - smallest

def getInput(num):
    input = open("./input/"+str(num)+".in", "r", encoding="utf-8")
    #input = open("./input/test.in", "r", encoding="utf-8")
    total = int(input.readline())
    for i in range(total) :
        intervals.append((input.readline()).split())
        intervals[-1][0],intervals[-1][1] = int(intervals[-1][0]),int(intervals[-1][1])
    input.close()
    return

def resOutput(num,res):
    output = open("./output/"+str(num)+".out", "w", encoding="utf-8")
    output.write(str(res))
    output.close()


if __name__=="__main__":
    fileNum = 10
    for i in range(10) :
        intervals = []
        getInput(i+1)
        res = getFiredman(intervals)
        resOutput(i+1,res)