s=input()
split_str=s.split()
output=""
for i in range(0,len(split_str),1):
    output+=split_str[i].capitalize()
    if i!=len(split_str)-1:
        k=len(output)
        while s[k]==" ":
            output+=" "
            k+=1
print(output)