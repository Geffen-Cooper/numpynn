''' This file defines the class for sigmoid activation layers'''

import numpy as np
import math
from ..layer import Layer

class ReLULayer(Layer):
    # need the dimension of the input activations
    def __init__(self, input_dimension):
        self.dim = input_dimension

        # store activations for backprop
        self.A = np.zeros(self.dim) 

    # g(Z)
    def forward(self, Z):
        # make sure the dimensions match
        if Z.shape != self.A.shape:
            print(f'Expected shape is {self.A.shape} and Z is {Z.shape}')
            raise AssertionError("matrix dimensions invalid")
        
        self.A = np.maximum(Z,0)
        return self.A

    # multiply elementwise the derivative of the activation function by the upstream gradient and return
    def backward(self, dL_dA):
        # activation of relu is just 1 or 0
        dA_dZ = self.A > 0
        return np.multiply(dA_dZ, dL_dA) # dL_dZ = dL_dA*dA_dZ

    def update_parameters(self, eta, reset=True):
        # has no parameters
        pass

    def __str__(self):
        return f'A: shape --> {self.A.shape}\n'