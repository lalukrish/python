line=input("enter the line:")
count={}
sentence=line.split()
for word in sentence:
    if word in count:
        count[word]+=0
    else:
        count[word]=0
        for k,v in count.items():
            print(k,v)
