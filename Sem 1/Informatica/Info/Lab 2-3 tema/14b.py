n = int(input("n = "))
s = 0

while (n > 0):
    if (n % 2 == 1):
        s += 1
    n = n // 2
    
    

print(s)