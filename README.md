# hopfield_nn_for_sudoku
Hopfield Neural Network to solve simple sudoku

This file has a python code for a single layer hopfield neural network to solve a sudoku algorithm.
The neural network consists of 729 neurons arrnaged in a single layer. 

Each neuron represents a cell in the sudoku represented as i,j and 'k' is the value that is there in the cell.
So, each cell with a pre-filled value is represented as (i,j,k), where cell i,j in the sudoku board has 'k' value in it.
So, every 9 consecutive neurons of the 729 neurons represents cell i,j of the sudoku with value k in it.
So, initial stste is as foolows:-

Cell i,j with pre-filled value k is given input 1 at neuron i*81+j*9+k.
Cell i,j with empty value is having 0 at all neurons representing it.

Since, this is a hopfield neural network, each neuron has ddefault input + learning rate(denoted by 'alpha')*inputs from output of few other cells

So, for each cell, we define domain of that cell as all cells in same i, same j, same k, and same 3x3 sqaure.
So, each neuron has default input + output of other neurons in its domain as input to this neuron.

Finally, energy function for those neurons which already have a value will have a unit change in their energy after 1 iteration, as the activation function for each neuron is linear function.

So, neurons with zero energy after 1 or 2 iterations are ones that require change, and 'k' of these neurons are values to be put in the neuron i,j.

How to compile and run:-

Just download the file and run it.
