"""
Collection of functions responsible for changint th orientation 
of an image in this assignment. The command_interpreter can be
considered as a public function. It interpretes what has to
be done and performs the correct operation, then returns the
modified image.
"""

import numpy as np

def command_interpreter(matrix, command):
    """
    "Public" function that gets called from the notebook, or
    wherever you want to implement this code. Then it reroutes
    the given image matrix and command to the correct function.
    If you add new functions, make sure to add it to the interpreter
    so it knows what to do.
    """
    if command is False:
        return matrix
    if command == 'mirror_y':
        return mirror(matrix, 1)
    if command == 'mirror_x':
        return mirror(matrix, 0)
    if command == 'rot_180':
        return rotate(matrix,2)
    if command == 'rot_90':
        return rotate(matrix, 3)
    if command == 'rot_270':
        return rotate(matrix, 1)
    raise RuntimeError(f"The command {command} could not be interpreted.")

def resize(matrix, factor:int):
    """
    This function will resize a numpy-image matrix by a given factor. 
    Stretching is applied over both axis at once. So a factor of 2 will
    be 4 times bigger than the original.
    NP DOC: https://numpy.org/doc/stable/reference/generated/numpy.repeat.html 
    """
    return np.repeat(np.repeat(matrix,factor, axis=0), factor, axis=1)


#don't directly call the functions below. If this were a proper
#class think of these as private methods.
def mirror(matrix, axis):
    """
    Function will mirror a numpy-image matrix over the given axis.
    NP DOC: https://numpy.org/doc/stable/reference/generated/numpy.flip.html
    """
    return np.flip(matrix, axis)

def rotate(matrix, ktimes:int):
    """
    Function will rotate a numpy-image matrix ktimes 90 degrees.
    NP DOC: https://numpy.org/doc/stable/reference/generated/numpy.rot90.html
    """
    new_matrix = np.rot90(matrix, k=ktimes, axes=(0,1))
    return new_matrix
