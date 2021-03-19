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
travel = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data/placerating.csv")

# define x, y 
idx_reviewer = travel.groupby('userId').size().reset_index()
print(idx_reviewer.shape)


user2idx = dict(zip(idx_reviewer.userId, idx_reviewer.index.values ))
idx_places = travel.groupby('placeId').size().reset_index()
idx_places.shape

place2idx = dict(zip(idx_places.placeId, idx_places.index.values))
idx2place = dict(zip(idx_places.index.values, idx_places.placeId))

travel['place_idx'] = [place2idx.get(p) for p in travel.placeId]
travel['user_idx'] = [user2idx.get(u) for u in travel.userId]


travel.loc[:, ['user_idx', 'place_idx', 'rating']].values

n_users = len(user2idx)
n_places = len(place2idx)

from keras.layers import Input, Embedding, LSTM, Dense
from keras.models import Model
import numpy as np

sequence_length = 2000
embedding_demension = 1000

user_in = Input(shape=(1,), dtype='int64', name='user_in')
u = Embedding(n_users, 20, input_length=1,embeddings_regularizer=l2(1e-5))(user_in)
u = Dense(64, activation='relu')(u)
user_out = Dense(1, activation='sigmoid', name='user_out')(u)

place_in = Input(shape=(1,), dtype='int64', name='place_in')
p = Embedding(n_places, 20, input_length=1,embeddings_regularizer=l2(1e-5))(place_in)
p = Dense(64, activation='relu')(p)
place_out = Dense(1, activation='sigmoid', name='place_out')(p)



conc = Concatenate([user_out, place_out])
conc = Dot(axes=2 )([u,p])
print(type(conc))
conc = Flatten()(conc)
#conc = Reshape((1,u, p), input_shape=(user_in, place_in))(conc)
#conc = Conv1D(filters=32,kernel_size=5 ,padding='valid')(conc)
#conc = GlobalMaxPool1D()(conc)
conc = Dense(32, activation='relu')(conc)
conc = BatchNormalization()(conc)
con_out = Dense(1, activation='sigmoid')(conc)

# x = Dot(axes=2)([u,p])
# x = Flatten()(x)
model = Model([user_in, place_in], outputs=con_out)
#model = Model([user_in, place_in], outputs=[user_out, place_out] )
model.compile('Adam',loss='binary_crossentropy', metrics=['acc'])

model.summary()

from IPython.display import Image
from keras.utils.vis_utils import model_to_dot

Image(model_to_dot(model,show_shapes=True, show_layer_names=False).create(prog='dot', format='png'))

data_set_mat = travel.loc[:, ['user_idx', 'place_idx', 'rating']].values

history = model.fit(x=[data_set_mat[:,0], data_set_mat[:,1]], y=data_set_mat[:,2], 
                    batch_size=64, epochs=10, validation_split=0.1, verbose=2)

place_dist = euclidean_distances(X=model.layers[3].get_weights()[0])


def get_place_recomm(beer_nm, place_dist, idx2place, topN=10):
    q_b_idx = place2idx[beer_nm]
    beer_dists = place_dist[q_b_idx]
    orders = np.argsort(beer_dists)
    return(zip(beer_dists[orders[:topN]], [idx2place[i] for i in orders[:topN]]))

rec = get_place_recomm(1,place_dist, idx2place, topN=10)
tuple(rec)