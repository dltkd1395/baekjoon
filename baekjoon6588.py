# 백준[6588번]
data=[]
def isprime(n):
  n += 1                            
  prime = [True] * n                
  for i in range(2, int(n**0.5)+1): 
    if prime[i]:                    
      for j in range(2*i, n, i):    
        prime[j] = False

  return prime


count=0
numbers=isprime(1000000)
while True:
  n=int(input())
  if n==0:
    break
  
  for i in range(3,n//2+1):
    if numbers[i] and numbers[n-i]:
      print('%d = %d + %d' %(n,i,n-i))
      break
  else:
    print('Goldbach\'s conjecture is wrong.')
