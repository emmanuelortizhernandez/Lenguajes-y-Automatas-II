file = open('file.txt', 'r')
#file2 = file.read()
#print(file2)
print("------------------------")
for l in file:
    data = l.split(' ')
    print(data)
    print("--->>>" + l)

file2 = file2.strip()
for palabra in file2.split(' '):
    if palabra.isalpha():
        print(palabra)
    else:
        print(">"+palabra+"<")
file.close()