empty_list = []
print("\n")

numbers = [1,2,3,4,5]
print(numbers)

triples = [1,2,3]*3
print(triples)

alist = [100,200,300,400,500]
alist = alist[::-1]
print(alist,"\n")

L = [4,5,1,2,9,7,10,8]
print("Original list :", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

L.sort()

print("Smallest elment is:", L[0])
print("largest element is:", L[-1])