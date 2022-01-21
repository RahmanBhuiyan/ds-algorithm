a=[[1,2],[2,3]]
b=[[3,4],[5,6]]

for i in range(len(a)):
    for j in range(len(b)):
        multification=a[i][j]*b[j][i]
        print(multification)
        