"""
Collection of functions responsible for changing the orientation/layout
of an image in this assignment. The command_interpreter can be
considered as a public function. It interpretes what has to
be done and performs the correct operation, then returns the
modified image for functions where the resulting array will have the 
exact same size as the input array or where the shape of the output array
can be expressed as an integer multiple of the given cell. Functions which 
modify the shape's aspect ratio. Or functions where a cell is stretched by a
non-integer amount need to be called directly and aren't part of the
command_interpreter convenience function.
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
        check_square(matrix)
        return rotate(matrix, 3)
    if command == 'rot_270':
        check_square(matrix)
        return rotate(matrix, 1)
    raise RuntimeError(f"The command {command} could not be interpreted.")

def check_square(matrix):
    """
    Raise an error if a non-square image is passed to a function which alters
    the shape of a given matrix.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise NotImplementedError("Non-square images are not supported at the moment.")

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

def sliding_puzzle_image_generator(matrix, rows, cols):
    """
    Remember those old puzzles of n*m squares where one square was missing? 
    You had to slide the little squares back and forth untill you came back
    to the original image. This function will generate such as shuffled 
    image with the topleft square removed from the original (it'll show up
    as a black cell somehwere in the shuffled grid.)
    This function takes three arguments:
        0: The image matrix read in numpy (3D array)
        1: the amount of rows to subdivide the image
        2: the amount of cols to subdivide the image
    So to make a puzzle with 24 cells + 1 black cell you need to call
    it direclty: warp.sliding_puzzle_image_generateo(<your_numpy_arr>, 5, 5).
    This function does not have a convenience command.
    """
    # take a copy to prevent unwanted changes to the global np_image
    img = matrix.copy()
    # to solve non-integer results of divinding width/ rows and vert/cols:
    # make a new shape with increased dimensions.
    base_shape = matrix.shape
    base_hor = base_shape[0]
    base_vert = base_shape[1]
    # create a new grid so that dividing them over xy axis will result in integers!
    new_hor = np.ceil(base_hor/rows)*rows
    new_vert = np.ceil(base_vert/cols)*cols
    # fill the new grid using full with topleft pixel values of img
    # np.full: https://numpy.org/doc/stable/reference/generated/numpy.full.html
    new_shape = np.full((int(new_hor), int(new_vert),3), img[0][0], dtype=int)
    # calculate offset from the left and the top: 
    left_offset = int((new_hor - base_hor)//2)
    top_offset = int((new_vert - base_vert)//2)
    # use the two offset values to put img in new_shape with topleft pixel at both offset values: 
    new_shape[left_offset:left_offset + img.shape[0], top_offset:top_offset + img.shape[1], :] = img
    # np.array_split: https://numpy.org/doc/stable/reference/generated/numpy.array_split.html 
    new_shape = np.array_split(new_shape, rows, axis=0)
    for row in range(len(new_shape)):
        new_shape[row] = np.array_split(new_shape[row], cols, axis=1)
    # 'delete' the topleft cell and make it black:
    new_shape[0][0] = np.zeros((new_shape[0][0].shape[0], new_shape[0][0].shape[1], 3), dtype=int)
    boxes = []
    for row in new_shape:
        for box in row:
            boxes.append(box)
    np.random.shuffle(boxes)
    boxnp = np.array(boxes)
    # iterate over boxnp and override the new_shape grid:
    one_box_size = boxnp[0].shape
    b = 0   # iterate over all boxes in the shuffled deck
    output_shape = np.full((
        int(rows*one_box_size[0]),
        int(cols*one_box_size[1]),
        one_box_size[2]
        ), img[0][0], dtype=int)
    for i in range(rows):
        for j in range(cols):
            output_shape[i * one_box_size[0] : (i + 1) * one_box_size[0],
                        j * one_box_size[1] : (j + 1) * one_box_size[1]] = boxnp[b]
            b+=1
    return output_shape
