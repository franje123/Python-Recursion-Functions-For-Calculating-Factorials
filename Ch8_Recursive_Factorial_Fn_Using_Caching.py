#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#with caching, using my own dictionary
cache={}

def factorial(n):
    #base case
    if n<=1:
        return 1
    else:
        cache[n-1]=factorial(n-1)
        cache[n]=cache[n-1]*n     #we don't get to this line until previous line has got to n=1
        return cache[n]
    
    
num= int(input("What number? "))
print(num,'!= ',factorial(num))

#print out the dictionary
for key, value in cache.items():
    print(f'key:{key}, value:{value}')


