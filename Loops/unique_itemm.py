list = [1,2,4,5,1,2,4,2,4,2,6]
uni = set()
for ele in list:
    if ele in uni:
        # print(ele,"is a dubplicate")
        continue
    else:
        uni.add(ele)
print(uni)