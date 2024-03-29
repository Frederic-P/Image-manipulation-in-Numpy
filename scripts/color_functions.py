"""
Collection of functions responsible for modifying the color 
channels of this assignment. The command_interpreter can be
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
    if command in ('R', 'G', 'B'):
        return boost_colorchannel(matrix, command)
    if command == 'N':
        return negative(matrix)
    if command in ('S_1', 'S_2'):
        shift_amount = int(command.split('_')[1])
        return shift(matrix, shift_amount)
    #throw an error if the command is not recognized:
    raise RuntimeError(f"The command {command} could not be interpreted.")

#normally you'd declare this as a private method with dunder,
# for the sake of the exercise I only use functions.
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
        raise RuntimeError("Invalid color channel given")

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
    new_matrix = np.absolute(matrix - [255, 255, 255])
    return new_matrix
