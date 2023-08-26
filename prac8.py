print("=============================================> 1 <====================================================")
import cd
print("--------------------------> a <-------------------------")
cd.dimh()
print("--------------------------> b <-------------------------")
cd.dpmp()
print("=============================================> 2 <====================================================")
print("sys:")
print(dir('sys'))
print("=============================================> 3 <====================================================")
print("--------------------------> a <-------------------------")
print("--------------------------> b <-------------------------")
num=8
print(num)
print("--------------------------> c <-------------------------")
import string
let=string.ascii_letters
print(let)
print("--------------------------> d <-------------------------")
dgt=string.digits
print(dgt)
print("--------------------------> e <-------------------------")
ca=string.punctuation
print(ca)
print("--------------------------> respuesta <-------------------------")
import random
sum=let+dgt+ca
res=[]
res.append(random.choice(string.ascii_lowercase))
res.append(random.choice(string.ascii_uppercase))
res.append(random.choice(string.digits))
res.append(random.choice(string.punctuation))
i=0
while i<4:
    res.append(random.choice(sum))
    i+=1
random.shuffle(res)
print(''.join(res))