import numpy.linalg as lin
import numpy as np
''' 행렬 1*1 ~ 5*5
      a     b     c     d     e
a    aa    ab    ac    ad    ae
b    ba    bb    bc    bd    be
c    ca    cb    cc    cd    ce
d    da    db    dc    dd    de
e    ea    eb    ec    ed    ee 
'''    

class MAT:
    mat = []; CI = []; w = []
  
def mat2x2(ab):
    n = 2
    #1_척도 행렬 생성
    listSeg = [1, ab, 1/ab, 1] #[1, ab, Fraction(1,ab), 1]
    m = MAT()
    m.mat = np.array(listSeg)
    m.mat = np.array(listSeg).reshape((n,n)) 
    #2_상대가중치(m.w) 구하기: 척도행렬 제곱 후 
    mSqrt = np.dot(m.mat, m.mat)
    w0 = [mSqrt[0][0] + mSqrt[0][1],
          mSqrt[1][0] + mSqrt[1][1] ]
    w1 = np.array(w0).reshape((n,1))
    m.w = w1/sum(w0)
    #3_CR,CI => 2개 쌍대비교에서 CI는 무조건 0
    m.CI = 0    
    return [m.mat, m.CI, list(m.w)]#{ 'mat': m.mat, 'ci' : m.CI, 'w': m.w }
    
def mat3x3(ab, ac, bc):
    n = 3  
    #1_척도 행렬 생성
    listSeg = [[1, ab, ac],
               [1/ab, 1, bc],
               [1/ac, 1/bc, 1]
               ]
    m = MAT()
    m.mat = np.array(listSeg).reshape((n,n));
    #2_상대가중치(m.w) 구하기: 척도행렬 제곱 후 
    #                   -> 각 행별로 값을 합산한 값 (3x1) 
    #                   -> 3x1의 원소를 모두 더한 값(sum)으로 다시 각 값을 나눠줌
    #                      (=> 3개 원소의 합이 1이 되게 리스케일한 것임)
    mSqrt = np.dot(m.mat, m.mat) #==m.mat.dot(m.mat)
    w0 = [mSqrt[0][0] + mSqrt[0][1] + mSqrt[0][2],
          mSqrt[1][0] + mSqrt[1][1] + mSqrt[1][2],
          mSqrt[2][0] + mSqrt[2][1] + mSqrt[2][2]
          ]
    w1 = np.array(w0).reshape((n,1))
    m.w = w1/sum(w0)
    #3_일관성비율(CR) 및 일관성지수(CI) 구하기
    # 일관성지수(CI) = (m.mat 행렬 고유치중 최대값 - n ) / (n-1) [단, n은 지표 개수]
    # 고유벡터
    lins = lin.eig(m.mat)
    lamM = max(lins[0])
    lamO = float(lamM)
    lam = round(lamO, 4)
    m.CI = (lam-n)/(n-1) 
    return [m.mat, round(m.CI, 4), list(m.w)] #list(m.w)

def mat4x4(ab, ac, ad, bc, bd, cd):
    n = 4
    #1_척도 행렬 생성
    listSeg = [1, ab, ac, ad,
               1/ab, 1, bc, bd,
               1/ac, 1/bc, 1, cd,
               1/ad, 1/bd, 1/cd, 1
               ]  
    m = MAT()
    m.mat = np.array(listSeg).reshape((n,n));
    #2_상대가중치 구하기 
    mSqrt = np.dot(m.mat, m.mat) #==m.mat.dot(m.mat)
    w0 = [mSqrt[0][0] + mSqrt[0][1] + mSqrt[0][2] + mSqrt[0][3],
          mSqrt[1][0] + mSqrt[1][1] + mSqrt[1][2] + mSqrt[1][3],
          mSqrt[2][0] + mSqrt[2][1] + mSqrt[2][2] + mSqrt[2][3],
          mSqrt[3][0] + mSqrt[3][1] + mSqrt[3][2] + mSqrt[3][3]
          ]
    w1 = np.array(w0).reshape((n,1))
    m.w = w1/sum(w0)
    #3_일관성지수(CI)
    # 고유벡터
    lins = lin.eig(m.mat)
    lamM = max(lins[0])
    lamO = float(lamM)
    lam = round(lamO, 4)
    m.CI = (lam-n)/(n-1) 
    return [m.mat, round(m.CI, 4), list(m.w)]

def mat5x5(ab, ac, ad, ae, bc, bd, be, cd, ce, de):
    n = 5
    #1_척도 행렬 생성
    listSeg = [1, ab, ac, ad, ae,
               1/ab, 1, bc, bd, be,
               1/ac, 1/bc, 1, cd, ce,
               1/ad, 1/bd, 1/cd, 1, de,
               1/ae, 1/be, 1/ce, 1/de, 1]
    m = MAT()
    m.mat = np.array(listSeg).reshape((n,n));
    #2_상대가중치 구하기 
    mSqrt = np.dot(m.mat, m.mat)
    w0 = [mSqrt[0][0] + mSqrt[0][1] + mSqrt[0][2] + mSqrt[0][3] + mSqrt[0][4],
          mSqrt[1][0] + mSqrt[1][1] + mSqrt[1][2] + mSqrt[1][3] + mSqrt[1][4],
          mSqrt[2][0] + mSqrt[2][1] + mSqrt[2][2] + mSqrt[2][3] + mSqrt[2][4],
          mSqrt[3][0] + mSqrt[3][1] + mSqrt[3][2] + mSqrt[3][3] + mSqrt[3][4],
          mSqrt[4][0] + mSqrt[4][1] + mSqrt[4][2] + mSqrt[4][3] + mSqrt[4][4]
          ]
    w1 = np.array(w0).reshape((n,1))
    m.w = w1/sum(w0)
    #3_일관성비율(CR)/일관성지수(CI)
    lins = lin.eig(m.mat)
    lamM = max(lins[0])
    lamO = float(lamM)
    lam = round(lamO, 4)
    m.CI = (lam-n)/(n-1)
    return [m.mat, round(m.CI, 4), list(m.w)]