Day1=open('Day 1.txt','r')

content=Day1.readlines()

p=''
for i in content:
  p=p+str(i)

list1=[]
for i in content :
    list1=list1+[i.strip()]

list1

sums=[]
sum=0
for number in list1:
  if number=='':
    sums.append(sum)
    sum=0
  else: sum+= int(number)
print(sums)

sums=sorted(sums)

sums
print(sums[-1]+sums[-2]+sums[-3])
