from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
from bubbleSort import bubble_sort
from quickSort1 import quick_sort
from mergeSort import merge_sort
from insertionSort import insertion_sort
from selectionSort import selection_sort
from heapSort import heap_sort

root= Tk()
root.title('Sorting Visualizer')
root.maxsize(900, 600)
root.config(bg= 'black')

selected_alg= StringVar()
data= []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height= 380
    c_width= 600
    x_width= c_width/ (len(data) + 1)               # Width of rectangles
    offset= 30                                      # To prevent starting at the border
    spacing= 10                                     # To create spacing b/w the bars
    normalizedData= [ i / max(data) for i in data]  #To make sure any scale of data fits inside canvas
    for i, height in enumerate(normalizedData):
        # Top left
        x0= i * x_width + offset + spacing
        y0= c_height - height * 350
        # Bottom right
        x1= (i + 1) * x_width + offset
        y1= c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill= colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text= str(data[i]))
    root.update_idletasks()


def Generate():
    global data
    minVal= int(minEntry.get())
    maxVal= int(maxEntry.get())
    size= int(sizeEntry.get())
    
    data= []
    for i in range(size):
        data.append(random.randrange(minVal, maxVal+1))


    drawData(data, ['red' for x in range(len(data))])

def startAlgorithm():
    global data
    if not data: return
    
    
    if algMenu.get() == 'Quick sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        
    elif algMenu.get() == 'Bubble sort':
        bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Merge sort':
        merge_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Insertion sort':
        insertion_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Selection sort':
        selection_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Heap sort':
        heap_sort(data, len(data), drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])
    

# Frame/base layout
UI_frame= Frame(root, width= 600, height= 200, bg= 'grey')
UI_frame.grid(row=0, column=0, padx=10, pady= 5)

canvas= Canvas(root, width= 600, height= 380, bg= 'white')
canvas.grid(row=1, column=0, padx= 10, pady= 5)

# UI area
# Row[0]
Label(UI_frame, text= "Algorithm", bg= 'grey').grid(row=0, column=0,  padx= 5, pady= 5, sticky= W)
algMenu= ttk.Combobox(UI_frame, textvariable= selected_alg, values= ['Bubble sort', 'Selection sort', 'Insertion sort', 'Quick sort', 'Merge sort',  'Heap sort'])
algMenu.grid(row= 0, column=1, padx= 5, pady= 5)
algMenu.current(0)

speedScale= Scale(UI_frame, from_= 0.1, to= 2.0, length= 200, digits= 2, resolution= 0.2, orient= HORIZONTAL, label= 'Select speed [s]')
speedScale.grid(row= 0, column=2, padx= 5, pady= 5)
Button(UI_frame, text= 'Start', command= startAlgorithm, bg= 'red').grid(row= 0, column=3,  padx= 5, pady= 5)

# Row[1]
sizeEntry= Scale(UI_frame, from_= 3, to= 20,  resolution= 1, orient= HORIZONTAL, label= 'Data size')
sizeEntry.grid(row=1, column=0,  padx= 5, pady= 5)

minEntry= Scale(UI_frame, from_= 0, to= 10,  resolution= 1, orient= HORIZONTAL, label= 'Min Value')
minEntry.grid(row=1, column=1,  padx= 5, pady= 5)

maxEntry= Scale(UI_frame, from_= 10, to= 100,  resolution= 1, orient= HORIZONTAL, label= 'Max Value')
maxEntry.grid(row=1, column=2,  padx= 5, pady= 5)

Button(UI_frame, text= 'Generate', command= Generate, bg= 'white').grid(row= 1, column=3,  padx= 5, pady= 5)

root.mainloop()


'''
[1,2,5,6,1,0]
'''

#conda install spyder=4.1.5
