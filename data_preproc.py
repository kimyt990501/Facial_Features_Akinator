import pandas as pd

import warnings
warnings.filterwarnings('ignore')

info = pd.read_csv('C:\\Users\\user\\Desktop\\github_repo\\Facial_Features_Akinator\\data\\player_info.csv', encoding='euc-kr', index_col=False)
info = info.drop(['Unnamed: 0'], axis=1)
#info.columns = ['name', 'birth']
#print(info)

samsung = pd.read_csv('C:\\Users\\user\\Desktop\\github_repo\\Facial_Features_Akinator\\data\\samsung_face.csv', index_col=False)
samsung = samsung.drop(['Unnamed: 0'], axis=1)
#print(samsung)

'''
info_sub = pd.read_csv('C:\\Users\\user\\Desktop\\imgtest\\data\\player_info_sub.csv', encoding='euc-kr', index_col=False)
info_sub = info_sub.drop(['Unnamed: 0'], axis=1)
info_sub.columns = ['birth', 'position', 'height']
'''

result = pd.merge(info, samsung, on='birth', how='inner')
#result = pd.merge(result, info_sub, on='birth', how='inner')
print(result)

# 포지션 판별 칼럼 추가
result['catcher'] = result['position'].apply(lambda x: 1 if x == '포수' else 0)
result['pitcher'] = result['position'].apply(lambda x: 1 if x == '투수' else 0)
result['outfielder'] = result['position'].apply(lambda x: 1 if x == '외야수' else 0)
result['infielder'] = result['position'].apply(lambda x: 1 if x == '내야수' else 0)
result = result.drop(['position'], axis=1)

result.to_csv('C:\\Users\\user\\Desktop\\github_repo\\Facial_Features_Akinator\\data\\samsung_facialfeatures.csv', encoding='euc-kr', index=False)