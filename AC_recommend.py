from itertools import permutations
import pandas as pd


def find_movie_pairs(x):
    pairs = pd.DataFrame(list(permutations(x, 2)), columns=['movie_a', 'movie_b'])
    
    return pairs
