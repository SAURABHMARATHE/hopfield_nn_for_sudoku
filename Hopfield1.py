import numpy as np
from scipy.special import expit

class Hopfield_Neuron:
  input=0.0
  output=0.0
  energy=0.0
  prev_energy=0.0
  alpha=1.0 # alpha is put to 1, because this neural network solves simple sudoku boards in 2 iterations of energy_update function
  i=0
  j=0
  k=0
  
  def __init__(self, i, j, k, cell_value): #constructor to initialize values for each neuron
    self.i = i
    self.j = j
    self.k = k
    self.input = cell_value
  
  def energy_function(self,output_for_each_neuron):
    # Energy = (sum of all node values) + (alpha * (sum of all nodes * domain complements))
    self.prev_energy=self.energy
    
    i = self.i
    j = self.j
    k = self.k
    temp = 0.0
    temp2 = 0.0
    
    # First term
    temp= temp + self.input
    # temp=-1*temp
    
    # Second term
    for i2 in range(0,9):
      if(i2!=i):
        temp2 = temp2 + output_for_each_neuron[i2][j][k]
    for j2 in range(0,9):
      if(j2!=j):
        temp2 = temp2 + output_for_each_neuron[i][j2][k]
    for k2 in range(0,9):
      if(k2!=k):
        temp2 = temp2 + output_for_each_neuron[i][j][k2]
    
    box_num = (int)(i/3) * 3 + (int)(j/3) 
    r_start = (int)(box_num/3) * 3
    c_start = (box_num%3) * 3
    for i2 in range(r_start,r_start+3):
      for j2 in range(c_start,c_start+3):
          if(i2!=i or j2!=j): # Do not consider cells considered in previous for loops
            temp2=temp2 + output_for_each_neuron[i2][j2][k]
          
    self.energy=temp + self.alpha * temp2  
    #self.output=expit(self.energy)  #to be used when activation funstion is sigmoid function
    self.output=self.energy
    return self.energy
  

class Hopfield_Network:
  
  sudoku_board=[[[0] * 9 for _ in xrange(9)]for _ in xrange(9)] # Initialize 9x9x9 matrix full of zeros
  output_for_each_neuron=[[[0] * 9 for _ in xrange(9)]for _ in xrange(9)] # Initialize 9x9x9 matrix full of zeros
  
  def __init__(self, sudoku_input_board):
                
    # Set sudoku_board with values 0 or 1 given input board
    for i in range(0,9):
      for j in range(0,9):
        value = sudoku_input_board[i][j]
        if(value!=0):
          self.sudoku_board[i][j][value-1]=1

          
    # Generate array of Hopfield_Neuron objects
    self.hn = []
    self.energy_update=[]
    for i in range(0,9):
      for j in range(0,9):
        for k in range(0,9):
          self.hn.append(Hopfield_Neuron(i, j, k, self.sudoku_board[i][j][k]))
          self.energy_update.append(0.0)

          
  def energy_update_func(self):
    # Find and store gain difference for each neuron
    for i in range(0,729):
      self.energy_update[i]=self.hn[i].energy_function(self.output_for_each_neuron) - self.hn[i].prev_energy
    
    for i in range(0,9):
      for j in range(0,9):
        for k in range(0,9):
          index = (i*81) + (j*9) + k
          self.output_for_each_neuron[i][j][k]=self.hn[index].output
    
          
  def stable_state_detector(self):
    # See if gain is not high
    for i in range(0,729):
      if(self.energy_update[i]<0.5):
        return False # Not near answer
    return True # Near or is the answer
  
  
  def run_neural_nw(self):
    # Network continues running if at least one neuron's gain is too high
    #while self.stable_state_detector()!=True: #to be used for complex sudoku puzzles with co-processor
    self.energy_update_func()
    self.energy_update_func()
    self.search()		
    self.display()  
  

  def search(self):
    for i in range(0,9):
    	for j in range(0,9):
            value_to_put=0
            for k in range(0,9):
        	if self.energy_update[i*81+j*9+k]<1: # Get k with min energy
                    value_to_put=k
                    print "Value %d should be put in cell %d, %d" % (value_to_put+1,i,j)
                    self.sudoku_board[i][j][k]=1
          
  def display(self):      #function to display final solved sudoku board
      for i in range(0,9):
        print ""
        for j in range(0,9):
          for k in range(0,9):
              if self.sudoku_board[i][j][k]==1:
                      print k+1, 
                          
  
def main():
  # Sample input
  sudoku_puzzle = [
    [8,9,1,2,7,4,5,6,3], # Simple sudoku board with 66 cells files and 15 cells empty
    [6,0,3,1,8,5,9,0,0],
    [4,5,7,6,3,9,0,0,2],
    [5,0,6,4,1,7,2,3,0],
    [7,4,2,9,0,3,8,1,6],
    [3,1,0,0,2,6,0,5,4],
    [9,3,8,5,4,0,6,7,0],
    [1,6,4,7,9,0,3,2,5],
    [0,7,5,3,6,1,4,9,8]
  ]
  
  
  # Create Sudoku AI and run it
  Sudoku_AI = Hopfield_Network(sudoku_puzzle)
  Sudoku_AI.run_neural_nw()

if __name__ == "__main__":
  main()






















