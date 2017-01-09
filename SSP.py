import random
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

    def attempt_random(self, S, n, t):
        if (t == 0):
            return True
            print("Subset has correct sum")
        if (n == 0 and t!=0):
            return False
            print("No subset has correct sum")

        if (S[n-1] > sum):
            return instance.attempt_random(S, n-1, t)
        else:
            return instance.attempt_random(S, n-1, t or instance.attempt_random
        
  

            

instance = SSP()
instance.random_yes_instance(4)
print( instance )
