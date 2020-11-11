import time

def heapify(data, n, i, drawData, timeTick):            # n- len of list, i- index of parent node
    largest= i
    left= i*2+1
    right= i*2+2
    drawData(data, getColorArray(len(data), n, largest, left, right))
    time.sleep(timeTick)
    if left < n and data[left] > data[largest]:
        largest= left
    if right < n and data[right] > data[largest]:
        largest= right
        
    drawData(data, getColorArray(len(data), n, largest, left, right))
    time.sleep(timeTick)
    
    if largest != i:
        data[largest], data[i]= data[i], data[largest]
        drawData(data, getColorArray(len(data), n, largest, left, right))
        time.sleep(timeTick)
        heapify(data, n, largest, drawData, timeTick)
        
def heap_sort(data, n, drawData, timeTick):
    for i in range(n//2 -1, -1, -1):
        heapify(data, n, i, drawData, timeTick)
    
    for i in range(n-1, 0, -1):
        data[i], data[0]= data[0], data[i]
        
        heapify(data, i, 0, drawData, timeTick)


def getColorArray(datalen, length, largest, left, right):
    colorArray= []
    
    for i in range(datalen):
        if i == largest:
            colorArray.append('red')
        elif i == left:
            colorArray.append('blue')
        elif i == right:
            colorArray.append('blue')
        elif i >= length:
            colorArray.append('green')
        else:
            colorArray.append('white')
        
    return colorArray