def calculateMultiples(self, n):
    i=10
    while(i>0):
        print(n*i, end=" " if i>1 else "\n")
        i-=1
calculateMultiples(None, 5)