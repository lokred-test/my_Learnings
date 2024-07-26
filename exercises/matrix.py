row=int(input("row:"))
col=int(input("col:"))
mtx1=[[int(input())for j in range(col)]for i in range(row)]
print(mtx1)

# print(mtx1[0][0]+mtx1[1][0])

# for i in range(row):
#     for j in range(col):
#         print(format(mtx1[i][j],"<3"),end="")

mtx2=[[int(input())for j in range(col)]for i in range(row)]
print(mtx2)

result=[[0 for j in range(col)]for i in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j]=mtx1[i][j]+mtx2[i][j]
print(result)


