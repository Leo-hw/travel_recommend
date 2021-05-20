from django.shortcuts import render

#!pip install scikit-surprise
import pandas as pd
from surprise import SVD, accuracy 
from surprise import Reader, Dataset 
import surprise
import os
from .models import Travel, Treview, Usert


def Cal_Knn(user_id):
    #results =[]
    
    user = Usert.objects.all()
    travel = Travel.objects.all()
    
    travels = travel.values('tourid', 'city', 'town', 'site', 'genre1', 'genre2','genre3')
    #print(travels)
    '''
    qs = SomeModel.objects.select_related().filter(date__year=2012)
    q = qs.values('date', 'OtherField')
    df = pd.DataFrame.from_records(q)
    '''
    
    # 1. raw dataset
    rate  = Treview.objects.all()
    rates = rate.values('user_no', 'placeid', 'rating', 'review_no')
    
    #rating = pd.DataFrame(data = rate, columns=['treview_no', 'user_no', 'placeid', 'rating'])
    rating = pd.DataFrame.from_records(rates) 
    #print(rating.head())   #   critic(user)   title(item)   rating
    
    print(user_id)
    #print('리뷰 id 갯수',rating['user_no'].value_counts())
    #print('placeid 갯수', rating['placeid'].value_counts())
    
    # 관광 vs 미관광
    tab = pd.crosstab(rating['user_no'], rating['placeid'])
    #print('1')
    #print(tab)
    
    # rating
    # 두 개의 집단변수를 가지고 나머지 rating을 그룹화
    rating_g = rating.groupby(['user_no', 'placeid'])
    #rating_g.sum()
    tab = rating_g.sum().unstack() # 행렬구조로 변환
    print(tab)
    #사용자 2이 가지 않은 곳, 1,15, 39....
    
    
    # 2. rating 데이터셋 생성
    print('실행')
    ### 여기 밑에 가 문제다
    #reader = Reader(line_format='rating["user_no"] rating["placeid"] rating["rating"]', rating_scale=(0.5, 5))

    ### 여기 surprise 에서 reader 에 들어가는 게 문제인거 같은데??
    # 그 전에 쓴 거 보고 확인해봐야겠다... uuid 랑 이iid랑 float(r) 이 들어가는 건데, 왜 그런건지 모르겠넹
    reader = Reader(rating_scale= (0.5, 5)) # 평점 범위
    data = Dataset.load_from_df(df=rating, reader=reader)
    # rating이라는 데이터프레임은 reader(1~5)의 평점 범위를 가진다.
    print('2', data)
    
    # 3. train/test set
    train = data.build_full_trainset() # 훈련셋
    test = train.build_testset() # 검정셋
    print('3', train.head())

    # 4. model 생성
    option = {'name': 'pearson'}
    model = surprise.KNNBaseline(sim_options=option)
    model.fit(train) # model 생성
    
    # 5. user_id 입력
    #user_id = 1 # 추천대상자
    item_ids = range(0, 2106) # placeid 범위
    actual_rating = 0 # 평점
    
    predict_result = []
    
    for item_id in item_ids :
        if not actual_rating in tab:
            actual_rating = 0
            a = model.predict(user_id, item_id, actual_rating)
            predict_result.append(a)
    
    ddff = pd.DataFrame(predict_result)
    print(ddff)
    
    # 유저 1 추천 여행지 상위 5개
    result = ddff.sort_values(by='est', ascending=False)[:5]
    
    #result.to_csv()
    print(result, type(result))
    #results.append(result)
    return result