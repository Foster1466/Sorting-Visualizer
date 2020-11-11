import time
def partition(data, head, tail, drawData, timeTick):
    pivot= data[head]
    i, j= head, tail
    drawData(data, getColorArray(len(data), head, tail, i, j))
    time.sleep(timeTick)
    while i<j:
        while data[i] <= pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i < j:
            drawData(data, getColorArray(len(data), head, tail, i, j))
            time.sleep(timeTick)
            data[i], data[j]= data[j], data[i]
            drawData(data, getColorArray(len(data), head, tail, i, j))
            time.sleep(timeTick)
        
    data[head], data[j]= data[j], data[head]
    drawData(data, getColorArray(len(data), head, tail, i, j))
    time.sleep(timeTick)
    return j

# [10,2,4,21,6,63,245]


def quick_sort(data, head, tail, drawData, timeTick):
    if head<tail:
        j= partition(data, head, tail, drawData, timeTick)
    
        quick_sort(data, head, j, drawData, timeTick)
        quick_sort(data, j+1, tail, drawData, timeTick)
        
def getColorArray(datalen, head,tail, i, j):
    colorArray= []
    for x in range(datalen):
        if x < datalen:
            colorArray.append('red')
        
        if x==i or x==j:
            colorArray[x]= 'green'
        
        if x == head:
            colorArray[x]= 'blue'
    print(colorArray)
    return colorArray

