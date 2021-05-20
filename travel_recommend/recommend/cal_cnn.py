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
# 직업
occ = []
for i in range(1000):
  nocc = np.random.randint(1, 16)
  #print(nocc)
  if nocc == 1:
    noccs = '학생'
  elif nocc == 2:
    noccs = '경영,사무'
  elif nocc == 3:
    noccs = '영업, 고객상담'
  elif nocc == 4:
    noccs = '생산, 제조'
  elif nocc == 5:
    noccs = '전문직'
  elif nocc == 6:
    noccs ='IT, 인터넷'
  elif nocc == 7:
    noccs = '교육'
  elif nocc == 8:
    noccs = '미디어'
  elif nocc == 9:
    noccs = '특수계층, 공공'
  elif nocc == 10:
    noccs = '건설'
  elif nocc == 11:
    noccs = '유통, 무역'
  elif nocc == 12:
    noccs = '서비스'
  elif nocc == 13:
    noccs = '디자인'
  elif nocc == 14:
    noccs = '의료'
  elif nocc == 15:
    noccs = '주부'
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

genre=[]
for i in range(1000):
  genr = np.random.randint(0,80)
  genre.append(genr)
print(genre)

# 사용자 데이터 프레임
user = pd.DataFrame()
user['userid'] = rating['userId'].unique()
user['genre'] = genre
user['age'] = age
user['occ'] = occ
user['gen'] = gen


user.head()
#user = user.drop(columns='genre')
user = user.rename(columns={'user' : 'userId'})

# user feature - occ/age/genre/gen
# user label - userid/rating/placeid

# place id 에 대한 각 userid 의 .rating 값.


user_rating = pd.merge(user, rating, on = 'userId')

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

travel_rating = pd.merge(travel, rating, on = 'placeId')

### for CNN
from keras.layers import Input, Embedding, LSTM, Dense, Conv1D, GlobalMaxPool1D, MaxPool1D, concatenate
from keras.models import Model, Sequential
from tensorflow.keras import models, layers
import numpy as np
from tensorflow import keras

def baseline_cnn(activation = 'relu'):
      max_tlen = len(max(travel_rating))
  max_ulen = len(max(user_rating))

  # tset_size = int(travel_rating.size)
  # uset_size = int(user_rating.size)

  tset_size = 1000
  uset_size = 1000
  #EMBDDING_DIMS = 5

  Uinput = Input(shape=(max_ulen, uset_size))
  Tinput = Input(shape=(max_tlen, tset_size))

  NUM_FILTERS = 1000
  FILTER_LENGTH1 = 5
  FILTER_LENGTH2 = 5

  # define input1
  #input1 = Embedding()
  model = Model
  '''  
  encode_u= Conv1D(filters=NUM_FILTERS, kernel_size=FILTER_LENGTH1, activation='relu', padding='valid', strides=1)(Uinput) 
  #encode_u = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH1, activation='relu', padding='valid', strides=1)(encode_u) 
  encode_u = GlobalMaxPooling1D()(encode_u) 

  encode_t = Conv1D(filters=NUM_FILTERS, kernel_size=FILTER_LENGTH2, activation='relu', padding='valid', strides=1)(Tinput) 
  #encode_t = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH1, activation='relu', padding='valid', strides=1)(encode_t) 
  encode_t = GlobalMaxPooling1D()(encode_t) 

  encode_combined = keras.layers.concatenate([encode_u, encode_t]) 

  # Merging subnetworks
  FC1 = Dense(1024, activation='relu')(encode_combined) 
  FC2 = Dropout(0.1)(FC1) 
  FC2 = Dense(512, activation='relu')(FC2) 
  
  # Final Dense layer and compliation
  predictions = Dense(1, kernel_initializer='normal')(FC2) 

  combinedModel = Model(inputs=[Uinput, Tinput], outputs=[predictions]) 
  combinedModel.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy']) 
  print(combinedModel.summary()) 
  '''
  
  return model