cities={
    'beijing':{
        'country':'China',
        'population':6000000,
        'chief':'mao',
        },
    'nanjing':{
        'country':'China',
        'population':7000000,
        'chief':'zhou',
        },
    'dongjing':{
        'country':'japan',
        'population':500000,
        'chief':'zhu',
        }
}
for city,content in cities.items():
    print("The "+city+" is a city of"+content['country']+",it has "+str(content['population'])+" people,and it's chief is "+
          content['chief'])
    print("\n")