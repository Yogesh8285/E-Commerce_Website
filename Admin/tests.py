from django.test import TestCase

# Create your tests here.

list = [1,5,4,3,11,12,13,15,17]

n = list[0]

for i in range (len(list)):
    for j in range(i+1,len(list)):
        if(n > list[j]):
            n = list[j]
            op = list[j+1]
    n = list[i]
print(op)