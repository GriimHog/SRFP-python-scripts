import array
from math import sqrt
5
ln = int(input("Enter how many numbers to check : "))
numar = array.array('i', [])
for i in range(ln):
    numar.append(int(input("Enter next number : ")))
for num in numar:
    for nums in range(2, int(sqrt(num))):
        if num % nums == 0:
            break
    else:
        print(num)
