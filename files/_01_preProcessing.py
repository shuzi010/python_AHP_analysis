'''전처리(preprocessing): csv 파일을 불러와서 일괄적으로 처리해야 하는 작업들 '''
import pandas as pd
from pandas.core.frame import Series

def readFiles():
    df = pd.read_csv('testdata.csv', sep='\,')     
#     print(len(df.index), len(df.columns))           
#     print(df['MatrixName_cell'])    #열 - 이름
#     print(df.ix[0:5])               #행 - 지정 따로 안해줘서 번호
#     print(df.ix[0,1])
#     colnames = df.columns           #열 이름들 따로 저장 
    return df

def switchNum(df):     # 답 번호를 척도로 일괄 변환 (1=1/9, 2=1/7, 3=1/5, 4=1/3, 5=1, 6=3, 7=5, 8=7, 9=9)
    switch = {1:1/9, 2:1/7, 3:1/5, 4:1/3, 5:1, 6:3, 7:5, 8:7, 9:9}
    for i in df.index:
        for j in df.columns:      
            v = df.ix[i,j]
            df.ix[i,j] = switch.get(v, df.ix[i,j])
    return df  

def setPersonsDF(dfScale): # 동적변수 만들어서 사람별로(row) 데이터 그룹 나누기
    data = dfScale.drop('MatrixName_cell', axis=1)
    dicPersons = locals() #-> returns dictionary
    for i in range(0, len(data.index)):
        dicPersons['%d'%i] = Series(data.ix[i]) #시리즈가 딕셔너리의 value에 들어감
        dicPersons['%d'%i].name = dfScale.ix[i,0] #시리즈에 네이밍
#         print(dicPersons['%d'%i], '%d'%i) # dict['key'] call the Value
    return dicPersons
        
def setHierachy(): #동적변수 다 받는거 *아닌가? 이거쓰면 getMatrix에서 h가 안불러와짐  
    #근린
    arg = [5,5,5,5,5,5,5,5,5,5,
           5,5,5,5,5,5,5,5,5,5]
    #도시
#     arg = [2,2,2,2,2,
#            3,3,3, 3,3,3,
#            2,
#            3,3,3,
#            3,3,3,
#            3,3,3,
#            4,4,4,4,4,4]
    return arg

def getHierachy():
    return setHierachy()