#Matthew Smith-Kennedy
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    import sys
    temper = int  # will hold input temp from user
    row_num = int
    col_num = int
    print ("Welcome to HeatDiff.\nHigher values will take longer to compute (up to a 2 minutes or so for 120).\nEnter temperature (range: 20-120):  ")
    temper = int(input())
    if (temper > 120 or temper < 20):
        print("Number out of range (20-120).  Please try again")
        sys.exit(0)
    row_num = temper + 2 #setting value to temper plus 2 extra rows (halo cells)
    col_num = temper + 2  #setting value to temper plus 2 extra rows (halo cells)
    state1 = np.zeros((row_num,col_num))
    state1[:,0] = float(temper)
    state2 = np.zeros((row_num,col_num))
    state2 = np.copy(state1)
    stopflag = False  #will be set to True when iterations reach 3000 or no change in state (whichever first)

    counter = int (0)
    message = ""
    while not stopflag:
        for i in range(1, row_num-1):    #ignores top and bottom row
            for j in range(1,col_num-1):  #ignores left and right column
                state2[i,j] = 0.25 * (state1[i - 1,j] + state1[i + 1, j] + state1[i,j - 1] + state1[i, j +1])

        if np.array_equal(state1,state2):
            stopflag = True
            message = "Halted on previous and next state equivalence reached"
        state1 = np.copy(state2)
        counter += 1
        if counter == 3000:
            stopflag = True
            message = "Halted on 3000 iterations reached"

    tempfloat = float(temper)
    eight = tempfloat / 8.0 #used for color calibration purposes
    tempfloat = float(temper)

    plt.figure(figsize= (6, 6), dpi = 80)

    size = int
    mark = ""
    if temper > 149:
        size = 3
        mark = '.'
    elif temper > 49:
        size = 4
        mark = '.'
    elif temper > 40:
        size = 4
        mark = 'o'
    else:
        size = 6
        mark = 'o'
    for i in range(1, row_num-1):    #ignores top and bottom row
        for j in range(1,col_num-1):  #ignores left and right column
            if state2[i, j] >= (tempfloat-eight):
                plt.plot([j], [i], marker = mark, color = 'darkred', markersize = size)
            elif state2[i, j] >= (tempfloat-2*eight):
                plt.plot([j], [i], marker = mark, color = 'red', markersize = size)
            elif state2[i, j] >= (tempfloat-3*eight):
                plt.plot([j], [i], marker = mark, color = 'orange', markersize = size)
            elif state2[i, j] >= (tempfloat-4*eight):
                plt.plot([j], [i], marker = mark, color = 'yellow', markersize = size)
            elif state2[i, j] >= (tempfloat-5*eight):
                plt.plot([j], [i], marker = mark, color = 'lawngreen', markersize = size)
            elif state2[i, j] >= (tempfloat-6*eight):
                plt.plot([j], [i], marker = mark, color = 'aqua', markersize = size)
            elif state2[i, j] >= (tempfloat-7*eight):
                plt.plot([j], [i], marker = mark, color = 'blue', markersize = size)
            else:
                plt.plot([j], [i], marker = mark, color = 'darkblue', markersize = size)
    plt.xlabel(message)

    plt.show()

    sys.exit(0)
