fh = open("file.txt""r")
print(fh)
riga=fh.readline()
while(riga!=''):
    print(riga,end='')
    riga=fh.readline()