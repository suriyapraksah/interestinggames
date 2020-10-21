# interestinggames
name1=input("Enter the name of first person:")
name2=input("Enter the name of second person:")
a=len(name1)
b=len(name2)
c=list(name2)
d=list(name1)
count=a+b
for i in d:
    for j in c:
        if i==j:
            count-=2
            c.pop(c.index(j))
            break
print("count:",count)
i=6
s="FLAMES"
s1=list(s)
if count!=0:
  while 1<i<=6:
    a=count%i
    if a==0:
        s1.pop(-1)
    else:
        s1.pop(a-1)
        s1=s1[a-1:]+s1[:a-1]
    i=i-1
print(s1)
'''F-Friend
   L-Love
   A-Affection
   M-Marriage
   E-Enemy
   S-Sister'''
