def main():
    a=b=1
    n = int(input("enter the value:"))
    while a <n:
        a,b = a+b, a
        print(a, end=" ")
    return a
main()

amt =0
while True:
    n= int(input('enter number:'))
    if n==0:
        break
    amt+=n
print(amt)