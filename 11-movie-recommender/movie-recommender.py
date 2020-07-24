%matplotlib inline
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings; warnings.simplefilter('ignore')




df = pd.read_csv("/content/drive/My Drive/my notebook/movie_dataset.csv")


movie_that_user_likes = input('please type one of your favorite movies: ')
based_on_features = ['keywords','cast','genres','director','tagline']

for basis in based_on_features:
	df[basis] = df[basis].fillna('')
 



def mix_features(row):
	try:
	  return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director'] + row['tagline']
	except:
		print('an error has occured',row)

df['mix_features'] = df.apply(mix_features,axis=1)


cv = CountVectorizer()
count_matrix = cv.fit_transform(df['mix_features'])

similarity_of_each_movie_with_another_based_on_custome_features = cosine_similarity(count_matrix)
#cosine similarity function gives us a float number between 0 and 1 which the bigger number shows more similarity between movies

error = False
def get_title(index):
	return df[df.index == index]["title"].values[0]

def get_index(title):
	try:
			return df[df.title == title]["index"].values[0]
	except:
				print('oops!! , either we do not have your movie in our dataset or you are typing it in a diffrent way! so give it a another try!!')
				error = True	
movie_that_user_likes_lowerd = movie_that_user_likes.lower()

index_of_movie = get_index(movie_that_user_likes_lowerd)

list_of_similar_movies = list(enumerate(similarity_of_each_movie_with_another_based_on_custome_features[index_of_movie]))

sorted_similar_movies_in_descending_order = sorted(list_of_similar_movies,key=lambda item:item[1] , reverse=True)


counter = 0
if error:
	print('The 25 top movies that we recommend you to watch are : ')
for favorite_movie in sorted_similar_movies_in_descending_order:
	if counter > 26: 
		break
	counter  = counter + 1
	if counter != 1: 
		print(get_title(favorite_movie[0]))