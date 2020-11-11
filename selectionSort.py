import time

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        minpos= i
        
        for j in range (i, len(data)):
            
            drawData(data, getColorArray(data, minpos,i, j, is_swapping= True))
            time.sleep(timeTick)
            
            if data[j] < data[minpos]:
                minpos= j
                
            drawData(data, getColorArray(data, minpos,i, j, is_swapping= True))
            time.sleep(timeTick)
            
        data[i], data[minpos]= data[minpos], data[i]
        
        drawData(data, getColorArray(data, minpos,i, j, is_swapping= True))
        time.sleep(timeTick)
        
        
def getColorArray(data, currmin,i, j, is_swapping):
    colorArray= []
    
    for index in range(len(data)):
        if index < i:
            colorArray.append('green')
        elif index == currmin:
            colorArray.append('red')
        elif index == j:
            colorArray.append('blue')
        else:
            colorArray.append('white')
            
            
    return colorArray
            