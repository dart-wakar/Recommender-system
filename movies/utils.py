import pandas as pd
import numpy as np

class RecommendedArray:
    def recommender(n):
        df = pd.read_csv("../myReco.csv")
        list_of_movies = df.iloc[n-1,:]
        array_of_movies = np.array(list_of_movies)
        return array_of_movies
