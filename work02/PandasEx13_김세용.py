
# coding: utf-8

# In[1]:


import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학':[90,80,70], '영어':[98,89,95],
            '음악':[85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df,'\n')  # 데이터프레임 출력

# '음악', '체육' 점수 데이터를 선택. 변수 music_gym에 저장
music_gym = df[['음악','체육']]
print(music_gym, '\n')
print(type(music_gym), '\n')

# '수학' 점수 데이터만 선택. 변수 math2에 저장
math2 = df[['수학']]
print(math2, '\n')
print(type(math2))

