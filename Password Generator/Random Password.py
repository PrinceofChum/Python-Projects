import string
import random

def randompassword():
    chars = string.ascii_letters + string.digits
    size = 3
    return ''.join(random.choice(chars) for x in range(size,15))

n = 0
while n < 10:
    print(randompassword())
    n=n+1   
