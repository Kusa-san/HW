x = {'first':[1,2,3],'second':'me','third':50.2,'forth':0,'fifith':[4,5,5]}

print(f"\n{x}\n\nx after swap is :\n")

y=[]
for i in x:
    y.append(x[i])

list_length = len(y)

for i in range(list_length // 2):

    temp = y[i]
    y[i] = y[list_length - i - 1]
    y[list_length - i - 1] = temp

for i in range(len(y)):

    z=0

    for i in x:
        x[i]=y[z]
        z+=1

print(x,"\n")