from numpy import *

# def get_matrix()
#     eq=input('Enter equations')
#     i=0
#     mat=[]
#     const_col=[]
#     while(eq[i]!='='):
#         row=[]
#         if(type(eq[i])==float):
#             row.append(eq[i])
#         if(eq[i]=='='):
#             const_col.append

def get_matrix():
    mat = []
    size = int(input('Enter number of variables or equations'))
    for i in range(size):
        print('Enter coefficients of %dth row' % (i+1))
        row = []
        for j in range(size + 1):
            row.append(float(input()))
        mat.append(row)
    return mat,size
    # for row in range(size):
    #     for column in range(size + 1):
    #         print(mat[row][column], end=" ")
    #     print()

def forw_elim():
    mat,size=get_matrix()
    for i in range(size)
        r=mat[0]/mat[0][0]
# get_matrix()
