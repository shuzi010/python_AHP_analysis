from files._01_preProcessing import *
from files._02_math import *
from numpy.core.multiarray import arange
import os, math

try:
    #############################################################################################################################
    #__preProcessing 전처리
    #############################################################################################################################
    df = readFiles()                            # 01. 답안 파일 불러오기
    setHierachy()
    dfScale = switchNum(df)                     # 02. 번호를 척도로 일괄 변환
    dicPersons = setPersonsDF(dfScale)          # 03. 개인별로 데이터 프레임이 나눠진 Dictionary 1개 생성( 이름은 삭제됨. 계산용임)
    
    #############################################################################################################################
    # 개인들의 ci값만 출력(파일출력)
    #############################################################################################################################
    nameFrame = DataFrame(dfScale['MatrixName_cell'])               #이름만 넣은 DataFrame
    with open('_result01_응답자별CI.txt', mode='w', encoding=None) as f:
        for i in range(0, len(nameFrame)): 
            pMatCiW = get_Mat_CI_W(dicPersons['%d'%i])              # 돌아오는 건 Mat 이라는 df(인덱스= InnerMatrix, ci, W 세개) 
            pMatCiW['name'] = dfScale.ix[i,0]                       # df, name 콜럼 추가(인덱스= InnerMatrix, ci, W, name 네개)
            pNameCi = DataFrame(pMatCiW, columns= ['name', 'ci'])   # 'W', 'InnerMatrix' 빼고 이름이랑 ci만 출력
            pNameCi = str(pNameCi)
            f.write(pNameCi)
    
    #############################################################################################################################
    #__최종 가중치 출력
    #############################################################################################################################
    # 일관성지수에 따라 제외할 사람들의 번호를 다 넣어주세요(set type 자료형 이용)
    standard = (0.1, 0.2, 0.25, 0.3, 0.4)
    for ci in range(0, len(standard)):
        excluder = []
        for i in range(0, len(nameFrame)):
            pMatCiW = get_Mat_CI_W(dicPersons['%d'%i])            # 돌아오는 건 Mat 이라는 df(인덱스= InnerMatrix, ci, W 세개) 
            pMatCiW['name'] = dfScale.ix[i,0]                     # df, name 콜럼 추가(인덱스= InnerMatrix, ci, W, name 네개)
            pNameCi = DataFrame(pMatCiW, columns= ['name', 'ci']) # 'W', 'InnerMatrix' 빼고 이름이랑 ci만 출력
            
            for j in range(0, len(pNameCi)):
                if pNameCi.ci[j] >= standard[ci] :
                    excluder.append(i)                            # pNameCi.name[j] <- 누군지 이름 알려면 이걸로 확인하면 됨
        #print('ci값이 %f를 넘는 사람(n = %s):'%(standard[ci], len(set(excluder))), set(excluder))
    
    # dfScale에서 제외할 사람들의 행 데이터를 없애주세요
        listEx = list(set(excluder))
        dfScaleRe = dfScale.drop(listEx)
    
    # 나머지 사람들의 기하평균을 구해주세요
        finalData = dfScaleRe.drop('MatrixName_cell', axis=1)
        finalDataL = []
        for j in finalData.columns:
            total = 1        
            for i in finalData.index:
                total = total * finalData.ix[i,j]
            val = math.exp(math.log(total)/len(finalData.index))
            finalDataL.append(val)
    
    # ci값을 기준으로 최종 가중치를 산정하고, 
        Results = get_Mat_CI_W(finalDataL)
        ResultW = Results['W']; #print(ResltW[11][0])
        for i in range(0, len(ResultW)):
            for j in range(0, len(ResultW[i])):
                ResultW[i][j] = float(ResultW[i][j])
                ResultW[i][j] = round(ResultW[i][j], 4)
    
    # 그것을 텍스트 파일로 뽑아주세요
        if os.path.isfile("_result02_최종가중치.txt"):
            with open('_result02_최종가중치.txt', mode='a', encoding=None) as f:             
                f.write('\n\n하이어라키별 가중치(CI <= %0.2f, n = %d):\n'%(standard[ci], len(finalData.index)) + str(ResultW))
        else:
            with open('_result02_최종가중치.txt', mode='w', encoding=None) as f:    
                f.write('\n\n하이어라키별 가중치(CI <= %0.2f, n = %d):\n'%(standard[ci], len(finalData.index)) + str(ResultW))
    #############################################################################################################################

except Exception as e:
    print('에러: ', e)