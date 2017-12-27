for i in range(9,0,-1):
    for j in range(9,0,-1):
        formula = '{1:1}x{0:1}={2:<2}'.format(i,j,i*j)
        print (formula,end=' ')
        print()
