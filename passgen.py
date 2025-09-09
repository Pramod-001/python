import random

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','*','@','^','+']

l = int(input("No.of letters in the password : "))
n = int(input("No.of numbers in the password : "))
s = int(input("No.of symbols in the password : "))

final = ''
password = []
for i in range(0,l) :
    lpass = random.choice(letter)
    final +=lpass
    password.append(lpass)

for i in range(0,n) :
    npass = random.choice(number)
    final+=npass
    password.append(npass)

for i in range(0,s) :
    spass = random.choice(symbols)
    final +=spass
    password.append(spass)

print(final)
random.shuffle(password)
pwd = ''
for i in password :
    pwd += i
print(pwd)