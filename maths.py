import numpy as np
import pandas as pd
from math import sqrt
from numpy.linalg import norm

# Calculating the cosine similarty between 2 vectors
def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    magn_a = sqrt(sum(x**2 for x in vector_a))
    magn_b = sqrt(sum(x**2 for x in vector_b))
    
    return dot_product / (magn_a * magn_b)
        
    
# Finding the k nearest neighbours according to their cosine similairty with the vector
def knn_cos(vector, dataset, k):
    similarities = []
    dict_indexes = []
    best_results = []
    
    for index in dataset.index:
        if vector.name == dataset.loc[index,:].name:
            continue
        similarities.append(cosine_similarity(vector, dataset.loc[index,:]))
        dict_indexes.append(index)
        
    for i in range(k):
        index = similarities.index(max(similarities))
        value = max(similarities)
        best_results.append((dict_indexes[index], value))
        similarities[similarities.index(value)] = 0
        
        
    return best_results
    