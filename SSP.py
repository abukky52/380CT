from random import randint, sample
from itertools import chain, combinations
from time import time

class SSP():
    def __init__(self, S=[], t=0):
        self.S = S
        self.t = t
        self.n = len(S)
        #
        self.decision = False
        self.total    = 0
        self.selected = []

    def subset_sum(sequence, sum_value):
        cols = sum_value + 1         # Plus 1 for 0 valued col.
        rows = len(sequence) + 1     # Plus 1 for 0 valued row.
        T = [[False for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            T[row][0] = True

        for index_i in range(1, rows):
            for index_j in range(1, cols):
                if index_j >= sequence[index_i - 1]:
                    T[index_i][index_j] = T[index_i - 1][index_j] or T[index_i - 1][index_j - sequence[index_i - 1]]
                else:
                    T[index_i][index_j] = T[index_i - 1][index_j]

        return T[rows - 1][cols - 1]

    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )

    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )

    ###

    def try_at_random(self):
        candidate = []
        total = 0
        while total != self.t:
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )
            

if __name__ == '__main__':
    sequence = [2, 3, 7, 8]
    assert True == subset_sum(sequence, 11)
    

