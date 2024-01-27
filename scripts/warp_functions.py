import numpy as np

def command_interpreter(matrix, command):
    if command == 'mirror_y':
        return mirror(matrix, 1)
    elif command == 'mirror_x':
        return mirror(matrix, 0)
    elif command == 'rot_180': 
        return rotate(matrix,2)
    elif command == 'rot_90':
        return rotate(matrix, 3)
    elif command == 'rot_270':
        return rotate(matrix, 1)
    return matrix

def resize(matrix, factor):
    return np.repeat(np.repeat(matrix,factor, axis=0), factor, axis=1)


#don't directly call the functions below. If this were a proper
#class think of these as private methods. 
def mirror(matrix, axis):
    #DOC: https://numpy.org/doc/stable/reference/generated/numpy.flip.html
    return np.flip(matrix, axis)

def rotate(matrix, ktimes:int):
    new_matrix = np.rot90(matrix, k=ktimes, axes=(0,1))
    return new_matrix

