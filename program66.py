#generator
def generator():
    yield 1
    yield 2
    yield 3
res=generator() #creating an object for generator
print(res)
print(next(res)) #o/p-1
print(next(res)) #o/p-2
print(next(res)) #o/p-3
# print(next(res)) #StopIteration