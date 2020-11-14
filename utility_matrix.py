import numpy as np
import pandas as pd

# Returning ready-to-use utility matrix to feed to the recommender
def utility_matrix(dataset):       
    rating_matrix = dataset.pivot_table(index = ['movieId'], columns = ['userId'], values = 'rating' )
    
    return rating_matrix

# Creating index : title dict
def dict_from_df(df):
    movies_dict = {df.iloc[i]['movieId'] : df.iloc[i]['title'] for i in range(len(df))}
        
    return movies_dict
    
# Searching the dictionary and returning index from title    
def search_for(dictionary, value):
    for k in dictionary:
            if value in dictionary[k]:
                print("The index for "+value+" is "+str(k))
                return k
    print("No entry found")
    return None



    
    
    
    
    
    
    
    
    

