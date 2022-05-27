#n1 = int(input('enter n1'))
#n2 = int(input('enter n2:'))
def ops(n1,n2):
    n3=n1*n2
    if (n3)>1000:
        print('The result is p',(n3))
    else:
        print('The result is s',(n1+n2))
    return
ops(7,8)

pre=0
for i in range(0,10):
    j=pre+i
    pre=i
    print('current number',i,'previous number',pre,'sum:',j)

s = 'chaitrakrishnamurthy'
size =len(s)
print('printing only even index')
for i in range(0,size-1,2):
    print(s[i])

#we can convert string to list and perform slicing to get the characters at specified position

s1='ridhirao'

s5 = list(s1)
for i in s5[0::2]:
    print(i)

def remove_chars(str1,n):
    print("original string:",str1)
    x=str1[n:]
    return x

print("removing characters from string")
print(remove_chars("chaitrakrishnamurthy",4))




