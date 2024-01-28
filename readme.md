# Image manipulateion in Numpy: 
Downloadable from: [GitHub](https://github.com/Frederic-P/Image-manipulation-in-Numpy)

## About
Collection of numpy functions used in a notebook to show some of the basic image manipulations
you can do with Numpy

## Installation: 
1) Download the GitHub repository, or clone it as you would with every other GitHub project.
2) Install and active the virtual environment (environment.yaml)
3) Run the notebook
4) Play with all the cells. 

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
     - **description**: This is a list with rows*cols elements in it. Each element describes a cell with three different parameters. The first element in the cell-list is a grow factor. The second element in the cell-list are all modifications done on the color channel. The final element in the cell-list are all modifications done which have to do with warping/rotating the image. 

### available cell-commands: 

#### Color commands: 

#### Warp/rotation commands: 

#### example of a 2*2 matrix: 
````
recipe = {
    'rows': 2, 
    'cols': 2, 
    'cells': [
        [1, False, False],
        [1, 'R', 'mirror_y'];
        [1, 'N', 'rot_270'],
        [1, 'S_2', False]
    ]
}
````
