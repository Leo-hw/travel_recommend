import os
import pandas as pd

def Weather(cityname):
    path = os.getcwd()
    print(path)
    
    # db에 입력 필요. => model 에서 불러와야함.
    files=os.listdir(path + '/travel_recommend/travel/static/weather')
#     filename = path + '/weather'
    filename = 'C:/work/new/team3project/travel_recommend/travel/static/weather'
    #print(files)
    
    for f in files:
        if f.startswith(cityname):
            weather = pd.read_excel(filename + '/' + f, index_col=0)
            print(f)
    print(weather)
    weather['date'] = pd.to_datetime(weather['date'])
    print(weather['date'])
    
    return weather



