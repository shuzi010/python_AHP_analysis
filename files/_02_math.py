from files._03_matrix import *
from files._01_preProcessing import getHierachy
from pandas.core.frame import DataFrame

# 한사람의 dict 데이터를 분석하여 한사람의 리스트 데이터 '[행렬집합, ci 집합, w 집합]'로 변환
def get_Mat_CI_W(dicPerson):
    # getList에서 넘긴 데이터를 받아줌(리스트) # dic타입 데이터를 -> list타입 데이터로 변환 
    # 행렬 계산은 넘파이(numpy) 라이브러리를 사용해야 할 수 있으며, 그럴려면 리스트 타입으로 변환해서 넘겨줘야 함
    listP = list(dicPerson)
 
    #Mat : 한 사람의 행렬 데이터 셋. 본 함수의 최종 리턴값
    Mat = []
    
    # 하이어라키 값들과 비교해서 2인경우, 3인경우, 4인경우, 5인경우로 나눠줘야함 (행렬 형태 결정)
    h = getHierachy(); #print(h)
    count = 0
    while count < len(listP):
        if h[count] == 2: 
            Mat.append(mat2x2(listP[count+0]))
            count += 1          #조합의 수 2C2
        elif h[count] == 3: 
            Mat.append(mat3x3(listP[count+0], 
                              listP[count+1], 
                              listP[count+2]
                              )
                       )
            count += 3          #조합의 수 3C2
        elif h[count] == 4: 
            Mat.append(mat4x4(listP[count+0], listP[count+1], 
                              listP[count+2], listP[count+3],
                              listP[count+4], listP[count+5],
                              )
                       )
            count += 6          #조합의 수 4C2
        elif h[count] == 5: 
            Mat.append(mat5x5(listP[count+0], listP[count+1], 
                              listP[count+2], listP[count+3],
                              listP[count+4], listP[count+5],
                              listP[count+6], listP[count+7],
                              listP[count+8], listP[count+9]
                              )
                       )
            count += 10         #조합의 수 5C2
        else: 
            print('해당행렬없음')
            break

    Mat = DataFrame(Mat, columns=['InnerMatrix', 'ci', 'W']); #print(Mat)
    return Mat
