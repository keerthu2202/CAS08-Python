n=input("ENTER THE DIGITS --> ")
d={}
d["1"]='0'
d["2"]='abc'
d["3"]='def'
d["4"]='ghi'
d["5"]='jkl'
d["6"]='mno'
d["7"]='pqrs'
d["8"]='tuv'
d["9"]='wxyz'
l=[]
for a in n:
    for b in n:
        if len(n)==1:
                for i in d[n[0]]:
                    l.append(i)
                break
        if a!=b:
            for i in d[a]:
                for j in d[b]:
                    l.append(j+i)
            break
        break
print(l)
