import random
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase=uppercase.lower()
digits="0123456789"
symbols="#@*%$&+"
upper,lower,syms,nums=True,True,True,True
all=""
if upper:
    all+=uppercase
if lower:
    all+=lowercase
if syms:
    all+=symbols
if nums:
    all+=digits
 
length=20
amount=10
for x in range(amount):
    password="".join(random.sample(all,length))
    print(password)
