import numpy

cells = numpy.zeros((9,9))
cells[4][4] = 1

print("step",0)
print(cells)

for step in range(1,10):
    new_state = numpy.zeros((9,9))
    for line in range(0,9):
        for column in range(0,9):
            new_state[line][column] = cells[line][column]
            if line != 0:
                new_state[line][column] = new_state[line][column] + cells[line-1][column]
            if line != 8:
                new_state[line][column] = new_state[line][column] + cells[line+1][column]
            if column != 0:
                new_state[line][column] = new_state[line][column] + cells[line][column-1]
            if column != 8:
                new_state[line][column] = new_state[line][column] + cells[line][column+1]
            if new_state[line][column] >= 1:
                new_state[line][column] = 1 
    cells = new_state
    print("step",step)
    print(cells)