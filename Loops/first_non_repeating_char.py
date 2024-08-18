word = input("Enter somthing : ")
for ch in word:
    if word.count(ch) == 1:
        print(ch)
        break
    # else:
    #     print("No non-repeating character.")