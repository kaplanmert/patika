##Soru 1 

x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
yeni = []
def duzlestir(data):
    for eleman in data:
        if type(eleman) == list:
            duzlestir(eleman)
        else:
            yeni.append(eleman)
duzlestir(x)
print(yeni)


##Soru 2

y=[[1, 2], [3, 4], [5, 6, 7]]
new=list()
for i in sorted(y,reverse=True):
    new.append(sorted(i, reverse=True))
print(new)
