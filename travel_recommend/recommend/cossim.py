import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def cosinePlace(placename,way):
    path = os.getcwd()
    
    rating = pd.read_csv(path + '/travel_recommend/travel/static/datafile/placerating.csv')
    place = pd.read_excel(path + '/travel_recommend/travel/static/datafile/국내여행지.xlsx')
    
    print(rating.tail())
    print(place.tail())
    
    # print(len(place))
    rate = []
    count = []
    for i in range(1,len(place) + 1):
        sum = 0
        k = 0
        try:
            for j in rating[rating['placeId']==i]['rating'].values:
                # print(j)
                sum += j
                k += 1
            rate.append(np.round(sum / k,4))
            count.append(k)
        except:
            # print(i)
            rate.append(sum)
            count.append(k)
    place['index'] = list(np.arange(1,2108))
    place['vote_average'] = rate
    place['vote_count'] = count
    del place['검색지유형1']
    del place['검색지유형2']
    del place['장르']
    place=place.rename(columns = {'검색지명':'title','검색지유형3':'genre'})
    place = place.set_index(['index'])
    # print(place.head())
    
    place1 = place['지역(시군구)'].values.tolist()
    place2 = place['지역(시도)'].values.tolist()
    placeconcat = []
    for i in range(len(place1)):
        placeconcat.append(place2[i]+ ' ' + place1[i])

    # print(placeconcat[:6])
    place['area'] = placeconcat
    del place['지역(시군구)']
    del place['지역(시도)']
    # print(place.tail())
    
    cnt_vect = CountVectorizer(min_df = 0, ngram_range=(1,2))
    genres_vect = cnt_vect.fit_transform(place['genre'])
    areas_vect = cnt_vect.fit_transform(place['area'])
    
    genre_sim = cosine_similarity(genres_vect, genres_vect)
    area_sim = cosine_similarity(areas_vect, areas_vect)
    # print(genre_sim[:10])
    # print(area_sim[:10])
    
    genre_sim_idx = genre_sim.argsort()[::-1]
    area_sim_idx = area_sim.argsort()[::-1]
    # print(genre_sim_idx)
    # print(area_sim_idx)
    
    if way == 'genre':
        sim = genre_sim_idx
    elif way == 'area':
        sim = area_sim_idx
    
    def find_sim_place(df, sorted_idx, title_name, top_n=5):
        title_place = df[df['title'] == title_name]
        title_place_idx = title_place.index.values
        top_sim_idx = sorted_idx[title_place_idx, :top_n]
        # print(top_sim_idx)
        
        top_sim_idx = top_sim_idx.reshape(-1,)
        similar_place = df.iloc[top_sim_idx]
        
        return similar_place

    similar_place = find_sim_place(place, sim, placename)
    print(similar_place[['title','area','genre','vote_average','vote_count']].index.tolist())
    
    C = place['vote_average'].mean()
    m = place['vote_count'].quantile(0.6)
    
    def weighted_vote_average(record):
        v = record['vote_count']
        R = record['vote_average']
        
        return ((v / (v + m) * R) + ((m / (m + v)) * C))

    place['weighted_vote'] = place.apply(weighted_vote_average, axis = 1)
    
    def find_sim_place2(df, sorted_idx, title_name, top_n=5):
        title_place = df[df['title'] == title_name]
        title_idx = title_place.index.values
        
        similar_idx = sorted_idx[title_idx, :(top_n * 2)]
        similar_idx = similar_idx.reshape(-1,)
        
        similar_idx = similar_idx[similar_idx != title_idx]
        return df.iloc[similar_idx].sort_values(by=['weighted_vote'], ascending=False)[:top_n]

    similar_place = find_sim_place2(place, sim, placename)
    print(similar_place[['title','area','genre','weighted_vote']])
    cossimlist = similar_place[['title','area','genre','weighted_vote']]
    
    return cossimlist