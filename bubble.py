li=[23,94,87,97,88]
for i in range(len(li)):
    for j in range(1,len(li)-i):
         if li[j] > li[j-1]:
              li[j],li[j-1]=li[j-1],li[j]
print((li))              