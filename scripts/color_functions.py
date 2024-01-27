import numpy as np

def command_interpreter(matrix, command, shift_amount = 0):
    if command in ('R', 'G', 'B'):
        return boost_colorchannel(matrix, command)
    elif command == 'N':
        return negative(matrix)
    elif command == 'S':
        return shift(matrix, shift_amount)
    return matrix

"""
    Every manipulation to the color channels of images are in this file
"""
############# COLOR MANIPULATION FUNCTIONS:
def boost_colorchannel(matrix, channel:str):
    """
    Function abstracted away, called by other functions with more
    explicit names as syntactic sugar. This function does all the 
    heavy lifting and shouldn't be public. Channels is modified to 
    be in range of 3 (RGB) if needed.
    matrix = 3D Numpy array ==> XY3
    channel = int ==> 0,1,2 referring to which RGB channel to boost
    """
    color_channels = 'RGB'
    if channel.upper() not in color_channels:
        raise Exception("Invalid color channel given")
    #normally you'd declare this as a private method with dunder,
    # for the sake of the exercise I only use functions.
    matrix_clone = matrix.copy()
    matrix_clone[:, :, color_channels.index(channel)] = 255
    return matrix_clone


def shift(matrix, shifts:int):
    """
    This function will roll through channels depending on the shifts parameter.
    RGB becomes GBR when shifts == 1; or BRG for shifts == 2
    matrix is a numpy array
    """
    shifted_image = np.roll(matrix, shifts, axis=-1)     #3rd dimension swap!!
    return shifted_image

def negative(matrix):
    """
    This function will return the negative of an image (think of old 
    rolls of film). 0 becomes 255, 1 becomes 254 etc...
    """
    new_matrix =np.absolute(matrix-[255, 255, 255])
    return new_matrix
