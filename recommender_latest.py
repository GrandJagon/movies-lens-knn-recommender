import pandas as pd
import numpy as np
from utility_matrix import utility_matrix, search_for, dict_from_df
from maths import knn_cos

ratings = pd.read_csv("ml-latest-small/ratings.csv", sep=',', usecols=range(3), encoding='latin-1')
movies = pd.read_csv("ml-latest-small/movies.csv", sep=',', usecols=range(2), encoding='latin-1')

movies_dict = dict_from_df(movies)


# Creating df aggregating movies and user per number of rating which will allow us to filter the movies and users that did
# perform enough ratings
movieStats = ratings.groupby('movieId').agg({'rating' : np.size})
userStats = ratings.groupby('userId').agg({'rating' : np.size})

# Choosing the rating threshold for movies and users to be taken in consideration in the recommending
popularMovies = list(set(movieStats.query('rating >= 50').index))
activeUsers = list(set(movieStats.query('rating >= 20').index))

df_popular_movies = ratings[ratings.movieId.isin(popularMovies)]
df_active_users = ratings[ratings.userId.isin(activeUsers)]

# Creating utility matrix and imputing all na with zeros
utility_matrix = utility_matrix(df_active_users)
utility_matrix.fillna(0, inplace = True)

def get_reco(title, utility_matrix, moviesDict, k):
    movie_index = search_for(moviesDict, title)
    recommendations = knn_cos(utility_matrix.loc[movie_index,:], utility_matrix, k)
    
    print("Looking for recommendation for "+moviesDict[movie_index])
    
    for result in recommendations:
        print(str(movies_dict[result[0]])+" ID -> "+str(result[0])+" ---> "+str(result[1]))
        
    print("------------------------------------------------------------------------------")
    
    
    
get_reco("Shining", utility_matrix, movies_dict, 10)

    