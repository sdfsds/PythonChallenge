file=open('text.txt')
txt=file.read().split(' ')
rez=[]
out=[]
for word in txt:
    if len(word)>6 and word[6]!=',' and word[6]!='.' :
       rez.append(word.title())
    else:rez.append(word)
    out=str(' '.join(rez))
print(out)
file=open('text.txt','w')
file.write(out)