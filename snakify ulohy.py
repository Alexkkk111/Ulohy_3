# a=[int(i) for i in input('Enter a sequence:').split()]
# for i in a:
#     if i==min(a):
#         m=min(a)#=1
#         ma=max(a)
#         x=a.index(max(a))#2
#         y=a.index(min(a))
#         a[x]=m
#         a[y]=ma
#         break
# for i in a:
#     print(str(i), end=' ')
# print('-----')

# a = [int(x) for x in input().split()]
# listx = []
# listdone=[]
# for i in range(len(a)-1):
#     if a[i] in listdone:
#         continue
#     else:
#         listdone.append(a[i])
#         unique = True
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             unique=False
#     if unique==True:
#         listx.append(a[i])
# if a[-1] not in listdone:
#     listx.append(a[-1])
# listx=[str(i) for i in listx]
# print(' '.join(listx))

# lol=[[int(x) for x in input().split()] for row in range(8)]
# #print(lol)
# attack=False
# for i in range(len(lol)):
#     for j in lol[i+1:]:
#         if lol[i][0]==j[0] or lol[i][1]==j[1] or abs(lol[i][0]-j[0])==abs(lol[i][1]-j[1]):
#             attack==True
# if attack==True:
#     print('YES')
# else:
#     print('NO')
