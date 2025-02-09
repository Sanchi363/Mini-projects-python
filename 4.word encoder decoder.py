import random
import string
def randoms():
    c=string.ascii_letters
    r=''.join(random.choice(c) for _ in range(3))
    return r
print("Select 1 for encoding and 0 for decoding")
a=int(input("Tell us whether you want to encode or decode:"))
if(a):
    str=input("Enter the word you want to encode:")
    if(len(str)<3):
        final=str[::-1]
        print(f"Encoded word :{final}")
    else:
        m=str[len(str)-1]
        l=list(str)
        l2=[]
        l2.append(m)
        for i in range(0,(len(str)-1)):
            l2.append(l[i])    
        b=randoms()
        e=randoms()
        s=''.join(l2)
        s=b+s
        final=s+e
        print(f"Encoded word :{final}")
else:
    str=input("Enter the string you want to decode:")
    if(len(str)<3):
        final=str[::-1]
        print(f"The decoded word is {final}") 
    else:
        m=str[4:(len(str)-3)]
        b=str[3]
        final=m+b
        print(f"The decoded word is {final}")    