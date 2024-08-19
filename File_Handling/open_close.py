file = open('demo.txt','w')

try:
    file.write('Hey there!, This is the demo file')
finally:
    file.close()

# with open('demo.txt','w') as file:
#     file.write('Happy Rakshabandhan')