from django.shortcuts import render

#!pip install scikit-surprise
import pandas as pd
from surprise import SVD, accuracy 
from surprise import Reader, Dataset 
import surprise
import os
from .models import Treview

path = os.getcwd()
print(path)

#filepath = path + '\travel_recommend\travel\static\datafile\placerating.csv'
#user_id = 

def Cal_Knn(user_id):
    results =[]
    
    # 1. raw dataset
    #rating = pd.read_csv(filepath)
    rate  = Treview.objects.all()
    rates = []
    for r in rate:
        rates.append(r)

    rating = pd.DataFrame(rates)
     
    rating.head()   #   critic(user)   title(item)   rating
    
    print(user_id)
    rating['userId'].value_counts()
    rating['placeId'].value_counts()
    
    # 관광 vs 미관광
    tab = pd.crosstab(rating['userId'], rating['placeId'])
    #print(tab)
    
    # rating
    # 두 개의 집단변수를 가지고 나머지 rating을 그룹화
    rating_g = rating.groupby(['userId', 'placeId'])
    rating_g.sum()
    tab = rating_g.sum().unstack() # 행렬구조로 변환
    #사용자 2이 가지 않은 곳, 1,15, 39....
    
    # 2. rating 데이터셋 생성
    reader = Reader(rating_scale= (1, 5)) # 평점 범위
    data = Dataset.load_from_df(df=rating, reader=reader)
    # rating이라는 데이터프레임은 reader(1~5)의 평점 범위를 가진다.
    #print(data)
    
    # 3. train/test set
    train = data.build_full_trainset() # 훈련셋
    test = train.build_testset() # 검정셋
    
    # 4. model 생성
    option = {'name': 'pearson'}
    model = surprise.KNNBaseline(sim_options=option)
    model.fit(train) # model 생성
    
    # 5. user_id 입력
    #user_id = 1 # 추천대상자
    item_ids = range(0, 2106) # placeId 범위
    actual_rating = 0 # 평점
    
    predict_result = []
    
    for item_id in item_ids :
        if not actual_rating in tab:
            actual_rating = 0
            a = model.predict(user_id, item_id, actual_rating)
            predict_result.append(a)
    
    ddff = pd.DataFrame(predict_result)
    #print(ddff)
    
    # 유저 1 추천 여행지 상위 5개
    result = ddff.sort_values(by='est', ascending=False)[:5]
    
    result.to_csv()
    print(result)
    results.append(result)
    return result