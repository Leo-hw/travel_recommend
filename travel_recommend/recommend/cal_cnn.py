# CNN
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import *
from keras.regularizers import *
from keras.models import *
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from keras.regularizers import *
from sklearn.metrics.pairwise import euclidean_distances

# load data
rating = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data/placerating.csv")
travel = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data/국내여행지_중복제거_utf.csv")

# define x, y 
# 나이 
age = []
for i in range(1000):
  nage=np.random.randint(20, 60)
  age.append(nage)
print(age)
len(age)

# 성별
gen = []
for i in range(1000):
  ngen = np.random.randint(1,9)
  
  if ngen % 2 == 1:
    ngens = '남'
    
  else:
    ngens = '여'
  gen.append(ngens)

print(gen)

# 직업
occ = []
for i in range(1000):
  nocc = np.random.randint(1, 16)
  #print(nocc)
  if nocc == 1:
    noccs = '학생'
  elif nocc == 2:
    noccs = '경영'
  else:
    noccs= '기타'
  occ.append(noccs)
print(occ)

'''
# 장르 추가는 따로 할 피료 없을듯
genre=[]
for i in range(1000):
  genr = np.random.randint(0,80)
  genre.append(genr)
print(genre)
'''

# 사용자 데이터 프레임
user = pd.DataFrame()
user['user'] = rating['userId'].unique()
user['genre'] = genre
user['age'] = age
user['occ'] = occ
user['gen'] = gen


user.head()
user = user.drop(columns='genre')
user = user.rename(columns={'user' : 'userId'})

# merge => for CF
travel = travel.rename(columns={'Unnamed: 0' : 'placeId'})
travel.drop('Unnamed: 8', axis = 1 ,inplace=True)
travel.drop('Unnamed: 9', axis = 1 ,inplace=True)
travel.drop('Unnamed: 10', axis = 1 ,inplace=True)
travel.drop('Unnamed: 11', axis = 1 ,inplace=True)
travel.drop('Unnamed: 12', axis = 1 ,inplace=True)
travel.drop('Unnamed: 13', axis = 1 ,inplace=True)
travel.drop('Unnamed: 14', axis = 1 ,inplace=True)
travel.drop('Unnamed: 15', axis = 1 ,inplace=True)

travel_user = pd.merge(travel, user_rating,on = 'placeId')
user_travel = pd.merge(user_rating, travel, on = 'placeId')


travel_user_rating = travel_user.pivot_table('rating', index='검색지명', columns='userId')
user_travel_rating = user_travel.pivot_table('rating', index='userId', columns='검색지명')

from sklearn.metrics.pairwise import cosine_similarity
item_based_collabor = cosine_similarity(travel_user_rating)
print(item_based_collabor.head())


def get_item_based_collabor(*args):
      #item_based_collabor['args']
  res = item_based_collabor.isin(args)
  print(res)
  result = res.sort_values(ascending = False)[:5] 
  print(result)
  return result
get_item_based_collabor()


### for CNN
from keras.layers import Input, Embedding, LSTM, Dense, Conv1D, GlobalMaxPool1D
from keras.models import Model
import numpy as np

sequences_length = 2000
embedding_demension = 1000

# input err #120 TypeError: '<=' not supported between instances of 'str' and 'int'
user_in = Input(shape=(5, ), dtype='int64', name = 'user_in')
u = Embedding(user, 20, input_length=1, embeddings_regularizer=l2(1e-5))(user_in)
u = Dense(64, activation='relu')(u)
user_out = Dense(1, activation='sigmoid', name='user_out')(u)


place_in = Input(shape=(16,), dtype='int64', name='place_in')
p = Embedding(travel, 20, input_length=1,embeddings_regularizer=l2(1e-5))(place_in)
p = Dense(64, activation='relu')(p)
place_out = Dense(1, activation='sigmoid', name='place_out')(p)

concat = Concatenate([user_out, place_out])
concat = Dot(axes=2)([u,p])
concat = Flatten(concat)

concat = Dense(32, activation='relu')(concat)
concat = BatchNormalization()(concat)
con_out = Dense(1, activation='sigmoid')(concat)

model = Model([user_in, place_in], outputs=con_out)
model.compile('Adam', loss = 'binary_crossentropy', metrics=['acc'])
model.summary()
