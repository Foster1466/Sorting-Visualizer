import time

def insertion_sort(data, drawData, timeTick):
    for j in range(1, len(data)):
        key= data[j]
        i= j-1
        drawData(data, getColorArray(data, i, j))
        time.sleep(timeTick)
        
        while i>=0 and data[i] > key:
            data[i+1],data[i]= data[i], data[i+1]
            
            drawData(data, getColorArray(data, i, j))
            time.sleep(timeTick)
            
            i= i-1
        '''
        drawData(data, getColorArray(data, i, j))
        time.sleep(timeTick)'''
    
    drawData(data, ['green' for x in range(len(data))])
    time.sleep(timeTick)
    return data


def getColorArray(data, i, j):
    colorArray= []
    
    for index in range(len(data)):
        if index < j:
            if index == i and i >= 0:
                colorArray.append('green')
            if index == j-1:
                colorArray.append('red')
            else:
                colorArray.append('green')
        else:
            colorArray.append('white')
    return colorArray