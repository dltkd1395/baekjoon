# 백준[1339]

alpha_num=int(input())
alpha_lst=[]
for _ in range(alpha_num):
  alpha_lst.append(input())

alpha_dic={}

for each_alpha in alpha_lst:
  count = 0 
  for i in each_alpha:
    if i not in alpha_dic:
      alpha_dic[i]=10**(len(each_alpha)-count-1)
    elif i in alpha_dic:
      alpha_dic[i]+=10**(len(each_alpha)-count-1)
    count+=1
dic_lst=sorted(list(alpha_dic.values()), reverse=True)
sum=0
for i in range(len(dic_lst)):
  sum+=dic_lst[i]*(9-i)

print(sum)
