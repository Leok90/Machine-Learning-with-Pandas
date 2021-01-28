
# coding: utf-8

# In[1]:


# Series - 1차원 배열
# DataFrame - 2차원 배열, 표 형태
import numpy as np
import pandas as pd


# In[2]:


# Series 자료형 생성
obj = pd.Series([3,6,9,12])
obj


# In[3]:


# 1차원 데이터는 Series 사용
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0])
print(s)


# In[4]:


# 기본 숫자 인덱스 대신 문자 인덱스 사용 가능
obj = pd.Series([3,6,9,12], index=['a','b','c','d'])
obj


# In[5]:


emp={'김철수':5000, '김철호':7000, '한상민':4000, '문대용':4500}
obj = pd.Series(emp)
obj
# key, value 확인


# In[6]:


# 2차원 리스트를 매개변수로 전달하여 dataframe 생성
a = pd.DataFrame([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(a)


# In[25]:


# 원하는 데이터 추출하기
import pandas as pd

# 키, 몸무게, 유형 데이터프레임 생성하기
tbl = pd.DataFrame({"gender":['f','m','m','f','f'],
                   'height':[170,180,155,143,154],
                   'weight':[80.0,70.4,65.5,45.9,51.2]
                   })

# 몸무게 목록 추출하기
print('몸무게 목록',end='\n\n')
print(tbl['weight'], end='\n\n')

# 몸무게와 키 목록 추출하기
print('몸무게와 키 목록',end='\n\n')
print(tbl[['weight','height']],end='\n\n')

print('--- height가 160 이상',end='\n\n')
print(tbl[tbl['height']>=160],end='\n\n')

print('--- gender가 m',end='\n\n')
print(tbl[tbl['gender']=='m'],end='\n\n')

print('--- 키로 정렬',end='\n\n')
print(tbl.sort_values(by='height'),end='\n\n')

print('--- 몸무게로 정렬',end='\n\n')
print(tbl.sort_values(by='weight', ascending=False))


# In[26]:


# 데이터프레임
# Dictionary 형태로 데이터 저장
data = {'names':['김철수','이철호','김영희','박민수','송철호'],
       'points':[1.5, 1.7, 3.6, 2.4, 2.9],
       'year':[2014,2015,2016,2017,2018]
       }

# 데이터프레임으로 변환
df=pd.DataFrame(data)

# 표 형태의 데이터로 출력됨
df


# In[27]:


# 값 확인(2차원 ndarray로 출력됨)
df.values


# In[28]:


# 인덱스와 컬럼 이름을 바꿀 수 있다.
df.index.name = 'Num'
df.columns.name = 'Info'
df


# In[29]:


# 컬럼과 인덱스에 key 이름을 지정할 수 있다.
df2 = pd.DataFrame(data, columns=['year','names','points','penalty'],
                  index=['one','two','three','four','five'])
df2


# In[30]:


# penalty는 새로운 필드이므로 NaN(Not a Number)로 표시됨
# NaN 컬럼은 어떤 연산도 처리되지 않으므로 대체값을 지정하는 것이 필요함
df2.fillna(0)


# In[31]:


df2.values


# In[32]:


# 계산 가능한 컬럼에 대해 기본통계량을 계산하여 출력
# 데이터셋을 전반적으로 살펴보고 싶을 때 유용함
df2.describe()


# In[33]:


import pandas as pd
import numpy as np

data = {'names':['김철수','이철호','김영희','박민수','송철호'],
       'year':[2014,2015,2016,2017,2018],
       'points':[1.5, 1.7, 3.6, 2.4, 2.9]}

df = pd.DataFrame(data, columns=['year','names','points','penalty'],
                 index=['one','two','three','four','five'])
df


# In[34]:


# year 컬럼만 선택, 인덱스와 함께 표시됨
# 하나의 열, 행을 선택하면 Series 형으로 출력됨
df['year']


# In[35]:


# 위와 같은 방법
df.year


# In[36]:


# 복수개의 열
df[['year','points']]


# In[37]:


# NaN 필드에 0.5를 대입
df['penalty'] = 0.5
df


# In[38]:


# 각각 다른 값을 입력할 경우(우변에 리스트 또는 ndarray로 작성)
df['penalty'] = [0.1, 0.2, 0.3, 0.4, 0.5]
df


# In[39]:


# 새로운 컬럼을 추가할 경우
df['ages'] = np.arange(10,15)
df


# In[40]:


# 필드 삭제
del df['ages']
df


# In[41]:


# 데이터프레임의 인덱스와 컬럼 이름 정의
df.index.name = 'Order'
df.columns.name = 'Info'
df


# In[42]:


# 숫자 인덱스 사용 : 0~2 인덱스
df[0:3]


# In[43]:


# 행 선택
df.loc['two']


# In[44]:


# two~four 인덱스 범위
df.loc['two':'four']


# In[45]:


# loc[행,열]
# two~four 행 중에서 points 열 선택
df.loc['two':'four','points']


# In[46]:


# 전체 행 중에서 year, names 필드만 선택
df.loc[:,['year','names']]


# In[47]:


# 인덱스 3행(네번째행)
df.iloc[3]


# In[48]:


# 행, 열에 대한 범위 인덱싱
# 3~4행, 0~1열
df.iloc[3:5, 0:2]


# In[49]:


# 원하는 인덱스 명시 가능
df.iloc[[0,1,3],[1,2]]


# In[50]:


# 모든 행의 1~3열
df.iloc[:, 1:4]


# In[51]:


# 1행 1열의 값
df.iloc[1,1]


# In[52]:


# boolean 인덱싱
# year가 2014보다 큰 데이터를 선택하려면?
df['year'] > 2014

# boolean Series가 출력된다. 마스크라고 함


# In[53]:


# True가 나온 행들만 선택
df.loc[df['year'] > 2014, :]


# In[54]:


import numpy as np
import pandas as pd

# 인덱스와 컬럼에 대한 정보가 없으면 0부터 시작하는 인덱스와 컬럼으로 설정된다.
# 6행 4열의 데이터프레임, randn() 정규분포 난수 발생
df = pd.DataFrame(np.random.randn(6,4))
df


# In[55]:


# 컬럼과 인덱스 설정
df.columns = ['A','B','C','D']
df.index = pd.date_range('20180301',periods=6)
df.index


# In[56]:


df


# In[57]:


# 컬럼 삭제
# drop 함수는 기본적으로 행을 삭제한다..
# axis에 1을 주게 되면 컬럼을 삭제한다.
df.drop('D', axis=1)
df

# 좌변에 새로운 데이터프레임에 할당해야 함


# In[58]:


df3 = df.drop('D', axis=1)
df3


# In[59]:


# 여러 컬럼 삭제
df.drop(['B','C'], axis=1)


# In[60]:


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'weight':[80.0, 70.4, 65.5, 45.9, 51.2],
    'height':[170, 180, 155, 143, 154]
})
df


# In[61]:


# 세로방향 합(각 열의 합)
df.sum(axis=0)


# In[62]:


# 가로방향 합(각 행의 합)
df.sum(axis=1)


# In[63]:


# height 열의 평균
df['height'].mean()


# In[64]:


# height 열의 분산(평균으로부터 얼마나 떨어져 있는지)
df['height'].var()


# In[65]:


# 새로운 데이터프레임 생성
df3 = pd.DataFrame(np.random.randn(4,3), columns=['b','d','e'],
                  index=['서울','인천','대구','부산'])
df3


# In[66]:


# 람다식 정의 : x가 입력되면 최대값에서 최소값을 뺀 값을 리턴한다.
func = lambda x : x.max() - x.min()

# 데이터프레임의 각 열(세로방향)에 func 함수를 적용한다.
# apply(함수이름)
df3.apply(func, axis=0)


# In[67]:


# 일반 함수 정의 : x가 입력되면 최대값에서 최소값을 뺀 값을 리턴한다.
def func(x):
    return x.max() - x.min()

# 데이터프레임의 각 열(세로방향)에 func 함수를 적용한다.
df3.apply(func, axis=0)


# In[68]:


# 데이터프레임의 각 행(가로방향)에 func 함수를 적용한다.
df3.apply(func, axis=1)

