import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_distances, cosine_similarity
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'    # with this can handle more merories, avoid kernel dead error.

def generate_table():
    recipes = pd.read_csv('../organized_recipes.csv')
    recipes = recipes[['id','name']]
    ratings = pd.read_csv('../cleaned_reviews.csv')
    ratings = ratings[['user_id', 'recipe_id', 'rating']]
    df = pd.merge(ratings, recipes, how='inner', left_on='recipe_id', right_on='id').drop(columns='id')
    review_count = df.groupby('recipe_id').count()
    selected_recipes = review_count[(review_count['rating'] > 4) & (review_count['rating'] < 9)].index
    df = df.set_index('recipe_id').loc[selected_recipes,:]
    df.reset_index(inplace=True)
    # clear up the memeories
    del ratings
    ratings = pd.DataFrame()
    del recipes
    recipes = pd.DataFrame()
    #### Clear up end ####
    pivot = pd.pivot_table(df, index='name', columns='user_id', values='rating')
    sparse_pivot = sparse.csr_matrix(pivot.fillna(0))
    dists = pairwise_distances(sparse_pivot, metric='cosine')
    similarities = cosine_similarity(sparse_pivot)
    recommender_df = pd.DataFrame(dists, columns=pivot.index, index=pivot.index)
    return recommender_df


def recommender(user_input2):
    df = generate_table()
    names = df[df.index.str.contains(user_input2)].index
    chosen_recipe2 = pd.DataFrame()
    for name in names:
        # chosen_recipe2 = pd.concat([chosen_recipe2, df[[name]].sort_values(by=name, ascending=True).head(6)])
        chosen_recipe2 = pd.concat([chosen_recipe2, df[[name]].sort_values(by=name, ascending=True).head(6).set_axis(['Pairwise_distances'], axis=1)])
    return chosen_recipe2
