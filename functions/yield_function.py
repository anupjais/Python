def even_num_generator(num):
    for i in range(0,num+1, 2):
        yield i

# print(even_num_generator(10))
for num in even_num_generator(10):
    print(num,end=" ")