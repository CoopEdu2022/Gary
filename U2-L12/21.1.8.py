a=open('1.txt', 'r+')
b=a.read()
a.close()
a=open('11.txt', 'w')
a.writelines(b)