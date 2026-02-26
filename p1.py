import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data
ratings = pd.DataFrame({
    'userId':[1,1,2,2,3,3],
    'movieId':[10,20,10,30,20,40],
    'rating':[4,5,5,3,2,4]
})
movies = pd.DataFrame({
    'movieId':[10,20,30,40],
    'title':['Inception','The Matrix','Interstellar','The Dark Knight']
})

# User–movie matrix + similarity
user_movie = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
sim = cosine_similarity(user_movie)
sim_df = pd.DataFrame(sim, index=user_movie.index, columns=user_movie.index)

# Recommend movies
def recommend(user, n=2):
    scores = {}
    for u in sim_df[user].sort_values(ascending=False).index[1:]:
        for m,r in user_movie.loc[u].items():
            if user_movie.loc[user,m]==0: scores[m]=scores.get(m,0)+r
    top = sorted(scores,key=scores.get,reverse=True)[:n]
    return movies[movies['movieId'].isin(top)]['title'].tolist()

print("Recommendations for User 1:", recommend(1))
