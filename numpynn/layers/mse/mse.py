''' This file defines the class for MSE (mean squared error) loss layer'''

import numpy as np
import math
from ..layer import Layer

class MSELayer(Layer):
    # L(Y,Y_hat)
    def forward(self, Y_hat, Y):
        # make sure the dimensions match
        if (Y_hat.shape != Y.shape):
            print(f'===> Expected shape is {Y.shape} and Y,Y_hat are {Y.shape},{Y_hat.shape}')
            raise AssertionError("matrix dimensions invalid")
        
        # store the output and expected output for backprop
        self.Y = Y
        self.Y_hat = Y_hat
        
        # Note that in general we should apply the MSE to the columns since
        # each sample output is a column vector. However, since the loss is averaged
        # over a batch and the MSE is summed anyways, we can just sum all losses in the matrix
        return 1/(Y.shape[0]*Y.shape[1])*np.sum(np.square(Y-Y_hat))

    # this is the most upstream gradient dL_dY
    def backward(self):
        return 2/(self.Y.shape[0]*self.Y.shape[1])*(self.Y_hat-self.Y)

    def update_parameters(self, eta, reset=True):
        # has no parameters
        pass

    def __str__(self):
        return f'Y_hat: shape --> {self.Y_hat.shape}\n'