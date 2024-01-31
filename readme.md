# Image manipulation in Numpy: 
Downloadable from: [GitHub](https://github.com/Frederic-P/Image-manipulation-in-Numpy)

## About
Collection of Numpy functions used in a notebook to show some of the basic image manipulations
you can do with Numpy

## Overview of key files/folders:
```
root
|___data
|   |___raw_data
|           -logo_alfa_romeo.jpg
|___documentation
|       -assignment.pdf
|___scripts
|       -color_functions.py
|       -warp_functions.py
-.gitignore
-.environment.yaml
-.notebook_demo.ipynb
-.readme.md
-.settings.json
```

- **scripts** holds two python function where all the actual functionality is implemented. Code is organized into two files, each centred on a single aspect of image manipulation (color channels & warping/rotating).
- **data/raw_data** The notebook will look in this folder for a given image.
- **documentation** what were the deliverables?
- **environment.yaml** Yaml file required to recreate the python virtual environment locally
- **notebook_demo.ipynb** showcase of the functions and how to implement it. Contains brief markdown and comments. Full explanation is in this readme.md file
- **settings.json** settings file where the image filename is being read from.

## Installation: 
1) Download the GitHub repository, or clone it as you would with every other GitHub project.
2) Install and activate the virtual environment (environment.yaml). For this you'll need to have [Anaconda](https://docs.anaconda.com/free/navigator/index.html) installed.
- Open an Anaconda PowerShell prompt and use `cd` to navigate to the directory where you cloned this repository to. The commands below assume you are in the root-directory of the codebase. To install the environment use: `conda env create -f environment.yaml` Wait for the installation process to complete. You'll know if the process is complete when the Anaconda PowerShell shows you the commands to activate and deactivate the newly installed environemnt.
- once installed type: `conda activate env_project_numpy` to activate this environment; you need to use this Kernel for all modules to work. 
- once activated open the notebook using the `jupyter notebook` command and open the notebook named **notebook_demo.ipynb** in the browserwindow that pops up. 
3) Run the notebook
4) Play with all the cells

## Modifying an image; making an image recipe:
The core of the notebook is a function called `convert_recipe_to_image_matrix` it expects a `dict` typed object with three keys:
1) rows: 
    - **type**: INT
    - **description**: The amount of rows the output grid should have. 
2) cols: 
    - **type**: INT
    - **description**: The amount of columns the output grid should have. 
3) cells:
     - **type**: LIST
     - **description**: This is a list with rows*cols elements in it. Each element describes a cell with three different parameters and should be of the type list. The first element in the cell-list is a grow factor. The second element in the cell-list are all modifications done on the color channel. The final element in the cell-list are all modifications done which have to do with warping/rotating the image. For a detailed explanation about these three elements see the following section *available cell-commands*.


### available cell-commands: 

#### Grow factor: 
The grow factor is a positive integer. If you want to keep your cell to the same size the original image was, you use a grow factor of 1 in your recipe. If you provide a grow factor of 2 your image will grow 2² times. 2 times horizontally and two times vertically. A grow factor 2 will thus result in 4 cells being used. 

To accommodate for this size increase you need to define x amount of cells in your recipe with grow factor 0. These cells with grow factor 0 should be the cells that are 'taken over' by growing one other cell and position the topleft corner of the grown cell in your grid. See example 3 in the notebook for a concrete implementation. The formula to calculate the x-required amount of cells with grow factor 0 is: (grow_factor*grow_factor)-1

#### Color commands: 
Color commands are case-sensitive and are part of the cell recipe. The position of color commands is on index 1 of your recipe. Should you not wish to modify the color channels. Provide ```False``` in your recipe at index 1.

All color commands are available through the convenience function **command_interpreter()**, which means you can simply rely on adding them to the cell-recipe without worrying about code. There's no need for you to directly call any of the functions in color_functions.py module.

- '**R**': Returns an image where the red channel of the image is set to 255 for every pixel in the image.
- '**G**': Returns an image where the green channel of the image is set to 255 for every pixel in the image.
- '**B**': Returns an image where the blue channel of the image is set to 255 for every pixel in the image.
- '**N**': Returns a negative of the image (think of old filmstock photography).
- '**S_1**: Returns an image where the channels are shifted by one position. (R becomes G, G becomes B, B becomes R)
- '**S_2**: Returns an image where the channels are shifted by two positions. (R becomes B, G becomes R, B becomes G)

example: make an image of 1 cell using S_2:
```
example_S_2 = {
    'cols': 1,
    'rows': 1,
    'cells': [[1, 'S_2', False] ]
}
```

##### Extending Color commands: 
You can extend the color commands module with the following procedure: 
1) Write a new function in the color_functions.py file, give it a unique name. At a bare minimum it should accept the Numpy 3D array as a parameter. The return value should be the modified matrix you'd want to use elsewhere.
2) Append an if-statment to the `command_interpreter()` function which looks for the given command and reroutes the given image matrix to your custom function. 
    - Caveat: The command to look for, cannot be used by other commands already present in the code.



#### Warp/rotation commands: 
Warp commands are case-sensitive and are part of the cell recipe. The position of warp commands is on index 2 of your recipe. Should you not wish to warp your image. Provide `False` in your recipe at index 2. Warp commands are supported for all square images, images which are rectangular will throw an error when doing operations where the shape of the operation differs from the original matrix.

Most warp-commands are directly available through the convenience function ***command_interpreter()**, which means you can simply rely on adding them to the cell-recipe without worrying about code. There's no need for you to directly call these functions directly in warp_functions.py. 
- '**mirror_y**': Returns an image mirrored over the y axis.
- '**mirror_x**': Returns an image mirrored over the x axis.
- '**rot_180**': Returns an image which has turned 180°.
- '**rot_90**': Returns an image which has turned 90° clockwise.
- '**rot_270**': Returns an image which has turned 270° clockwise.

The warp_functions.py module has one function which has to be called directly. This is the **sliding_puzzle_image_generator(matrix, rows, cols)** function. It generates the start of an old puzzle with n*m-1 tiles and one blacked out tile (https://en.wikipedia.org/wiki/Sliding_puzzle). This function takes three arguments:
1) a 3D Numpy-array of the image you want to shuffle
2) rows (int): the amount of rows you want to see in your shuffled image
3) cols (int): the amount of columns you want to see in your shuffled image

This function will return a 3D array with a shape that is at least equal to the given shape, or slightly bigger to ensure every sliding puzzleblock is of the exact same size.

##### Extending warp functionalities: 
Extending warp functionalities is exactly the same as extending the color functionalities with the exception of warp functions which potentially return a larger grid. 

#### example of a 2*2 matrix: 
````
recipe = {
    'rows': 2, 
    'cols': 2, 
    'cells': [
        [1, False, False],
        [1, 'R', 'mirror_y'],
        [1, 'N', 'rot_270'],
        [1, 'S_2', False]
    ]
}
````
# Image copyright: 
borrowed from: https://fr.wikipedia.org/wiki/Alfa_Romeo#/media/Fichier:Logo_Alfa_Romeo_(2015).svg 