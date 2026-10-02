import random
l = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
z = '1234567890'
s = '!@#$%^8*'
pas = ''.join((random.sample(l, 3) + random.sample(z, 3) + random.sample(s, 2)))
n = random.sample(pas, 8)
print(''.join(n))