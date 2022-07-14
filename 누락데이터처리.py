# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns

#데이터 가져오기
#df=pd.read_csv()
#df=sns.load_dataset()
missing_df=df.isnull()
for col in missing_df.columns:
    missing_count=missing_df[col].value_counts()
    try:
        print(col,': ',missing_count[True])
    except:
        print(col,': ',0)

#누락 데이터 제거
#누락 데이터가 thresh (500)개 만큼 있을 때 dropna를 사용하여 열 제거
df_thresh=df.dropna(axis=1,thresh=500)

#누락 데이터가 데이터가 없는 모든 행 삭제
df_a=df.dropna(subset=[],how='any',axis=0)

#평균으로 누락 데이터 바꾸기
mean_a=df[].mean(axis=0)
df[].fillna(mean_a,inplace=True)

#가장 많이 나타나는 값으로 바꾸기
most_freq=df[].value_counts(dropna=True).idxmax()
df[].fillna(most_freq,inplace=True)

#이웃하고 있는 값으로 바꾸기
df[].fillna(method='ffill',inplace=True)

hi
