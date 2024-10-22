s= input().split()
s2=[]
for c in s:
    s2.append(int(c))
mx=max(s2)
mn=min(s2)
smi=s2.index(mx)
sni=s2.index(mn)
s2[sni], s2[smi] = s2[smi], s2[sni]
print(*s2)
    
