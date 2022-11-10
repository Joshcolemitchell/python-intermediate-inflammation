import numpy as np
from functools import reduce
from multiprocessing import Pool

def sum_of_squares(sequence):
    
    
    integers = [int(x) for x in sequence if '#' not in x]
    squares = [x * x for x in integers]
        
    return reduce(lambda a, b: a + b, squares)


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(sum_of_squares(['12', '22', '100#', '23']))

