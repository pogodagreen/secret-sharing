from random import randrange

if __name__ == '__main__':
    n=5
    t=n
    tab=[]
    k=1000
    s=345
    for i in range(0,n-1):
        tab.append(randrange(0,k-1))
    tab.append(s)
    for i in range(0, n-1):
        tab[n-1]-=tab[i]
    tab[n-1]=tab[n-1]%k
    print(tab)
    x=0
    for i in range(0, n):
        x+=tab[i]
    x=x%k
    print(x)