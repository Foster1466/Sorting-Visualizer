import time

def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
   if left<right:
        middle= (left+right)//2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)
        
    
def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)
    leftPart= data[left:middle+1]
    rightPart= data[middle+1:right+1]
    
    left_idx= right_idx= 0
    
    for data_idx in range(left, right+1):
        if left_idx < len(leftPart) and right_idx < len(rightPart):
            if leftPart[left_idx] <= rightPart[right_idx]:
                data[data_idx] = leftPart[left_idx]
                left_idx += 1
            else:
                data[data_idx] = rightPart[right_idx]
                right_idx += 1
            
        elif left_idx < len(leftPart):
            data[data_idx] = leftPart[left_idx]
            left_idx += 1
        else:
            data[data_idx] = rightPart[right_idx]
            right_idx += 1
            
    drawData(data, ['green' if x>= left and x<= right else 'white' for x in range(len(data))])
    time.sleep(timeTick)
            
            
def getColorArray(length, left, middle, right):
    colorArray= []
    
    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colorArray.append('yellow')
            else:
                colorArray.append('pink')
        else:
            colorArray.append('white')
            
    return colorArray